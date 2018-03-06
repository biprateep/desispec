#
# See top-level LICENSE.rst file for Copyright information
#
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys
import os
import re
import time
import traceback
from ..defs import (task_name_sep, task_state_to_int, task_int_to_state)

from desiutil.log import get_logger

task_classes = None


def task_type(name):
    """Given a task name, find the type from the list of available ones.

    Args:
        name (str): the name of the task.

    Returns:
        str: the type of the task.

    """
    global task_classes
    avail = list(task_classes.keys())

    # We sort by string length, so that shorter types contained in the name
    # of longer ones do not match first.
    savail = list(sorted(avail, key=len)[::-1])

    tt = None
    for av in savail:
        if re.search(av, name) is not None:
            tt = av
            break
    return tt


# This class is named "BaseTask", not "TaskBase" to avoid regex matching with
# the automatic loading found in _taskclass.py.

class BaseTask(object):
    """Base class for tasks.

    This defines the interfaces for the classes representing pipeline tasks.
    This class should not be instantiated directly.

    """
    def __init__(self):
        self._type = "base"
        self._cols = [] # database columns
        self._coltypes = []
        self._name_fields  = [] # name fields. note that name fields have to be included in cols
        self._name_formats = [] # name field formats

    def _name_split(self, name):
        fields = name.split(task_name_sep)
        if (len(fields) != len(self._name_fields)+1) or (fields[0] != self._type):
            raise RuntimeError("name \"{}\" not valid for a {}".format(name,self._type))
        ret = dict()
        for i,k in enumerate(self._name_fields) :
            # first part of the name is the type, like fibermap-YYYYMMDD-EXPID
            if re.match(r".*d.*", self._name_formats[i]) is not None:
                # This is an integer field
                ret[k] = int(fields[i+1])
            else:
                ret[k] = fields[i+1]
        return ret


    def name_split(self, name):
        """Split a task name into its properties.

        Args:
            name (str): the task name.

        Returns:
            dict: dictionary of properties.

        """
        return self._name_split(name)


    def _name_join(self, props):
        ret=self._type
        for field,fieldformat in zip(self._name_fields,self._name_formats) :
            ret += format(task_name_sep)
            ret += format(props[field], fieldformat)
        return ret


    def name_join(self, props):
        """Construct a task name from its properties.

        Args:
            props (dict): dictionary of properties.

        Returns:
            str: the task name.

        """
        return self._name_join(props)


    def _paths(self, name):
        raise NotImplementedError("You should not use a BaseTask object "
            " directly")
        return None


    def paths(self, name):
        """The filesystem path(s) associated with this task.

        Args:
            name (str): the task name.

        Returns:
            list: the list of output files generated by this task.

        """
        return self._paths(name)


    def _create(self, db):
        """See BaseTask.create.
        """
        with db.conn as cn:
            cur = cn.cursor()
            createstr = "create table {} (name text unique".format(self._type)
            for col in zip(self._cols, self._coltypes):
                createstr = "{}, {} {}".format(createstr, col[0], col[1])
            createstr = "{})".format(createstr)
            cur.execute(createstr)
        return


    def create(self, db):
        """Initialize a database for this task type.

        This may include creating one or more tables.

        Args:
            db (pipeline.DB): the database instance.

        """
        self._create(db)
        return


    def _insert(self, cursor, props):
        """See BaseTask.insert.
        """
        name = self.name_join(props)
        colstr = '(name'
        valstr = "('{}'".format(name)

        #cmd='insert or replace into {} values ("{}"'.format(self._type, name)
        for k, ktype in zip(self._cols, self._coltypes):
            colstr += ', {}'.format(k)
            if k == "state":
                if k in props:
                    valstr += ', {}'.format(task_state_to_int[props["state"]])
                else:
                    valstr += ', {}'.format(task_state_to_int["waiting"])
            else:
                if ktype == "text":
                    valstr += ", '{}'".format(props[k])
                else:
                    valstr += ', {}'.format(props[k])
        colstr += ')'
        valstr += ')'

        cmd = 'insert into {} {} values {}'.format(self._type, colstr, valstr)
        print(cmd, flush=True)
        cursor.execute(cmd)
        return


    def insert(self, cursor, props):
        """Insert a task into a database.

        This uses the name and extra keywords to update one or more
        task-specific tables.

        Args:
            cursor (DB cursor): the database cursor of an open connection.
            props (dict): dictionary of properties for the task.

        """

        log = get_logger()
        log.debug("inserting {}".format(self.name_join(props)))

        self._insert(cursor, props)
        return


    def _retrieve(self, db, name):
        """See BaseTask.retrieve.
        """
        ret = dict()
        with db.conn as cn:
            cur = cn.cursor()
            cur.execute(\
                "select * from {} where name = '{}'".format(self._type,name))
            row = cur.fetchone()
            if row is None:
                raise RuntimeError("task {} not in database".format(name))
            ret["name"] = name
            for i,k in enumerate(self._cols[1:]) :
                if k == "state" :
                    ret[k] = task_int_to_state(row[i])
                else :
                    ret[k] = row[i]
        return ret


    def retrieve(self, db, name):
        """Retrieve all task information from the DB.

        This may include additional information beyond the contents of the
        task name (e.g. from other tables).

        Args:
            db (pipeline.DB): the database instance.
            name (str): the task name.

        Returns:
            dict: dictionary of properties for the task.

        """
        return self._retrieve(db, name)


    def _state_set(self, db, name, state):
        """See BaseTask.state_set.
        """
        start = time.time()
        with db.conn as cn:
            cur = cn.cursor()
            cur.execute("begin transaction")
            cur.execute("update {} set state = {} where name = '{}'"\
                .format(self._type, task_state_to_int[state], name))
            cur.execute("commit")
        stop = time.time()
        log  = get_logger()
        log.debug("took {} sec for {}".format(stop-start,name))
        return


    def _state_get(self, db, name):
        """See BaseTask.state_get.
        """

        st = None
        with db.conn as cn:
            cur = cn.cursor()
            cur.execute(\
                "select state from {} where name = '{}'"\
                .format(self._type,name))
            row = cur.fetchone()
            if row is None:
                raise RuntimeError("task {} not in database".format(name))
            st = task_int_to_state[row[0]]

        return st


    def state_set(self, db, name, state):
        """Set the state of a task.

        This should not be called repeatedly if you are setting the state of
        many tasks.  It is more efficient to do that in a single SQL command.

        Args:
            db (pipeline.DB): the database instance.
            name (str): the task name.

        """
        self._state_set(db, name, state)
        return


    def state_get(self, db, name):
        """Get the state of a task.

        This should not be called repeatedly for many tasks- it is more
        efficient to get the state of many tasks in a single custom SQL query.

        Args:
            db (pipeline.DB): the database instance.
            name (str): the task name.

        Returns:
            str: the state.

        """
        return self._state_get(db, name)


    def _deps(self, name, db, inputs):
        raise NotImplementedError("You should not use a BaseTask object "
            " directly")
        return None


    def deps(self, name, db=None, inputs=None):
        """Get the dependencies for a task.

        This gets a list of other tasks which are required.

        Args:
            name (str): the task name.
            db (pipeline.DB): the optional database instance.
            inputs (dict): optional dictionary containing the only input
                dependencies that should be considered.

        Returns:
            dict: a dictionary of dependencies.  The keys are arbitrary and
                the values can be either scalar task names or lists of tasks.

        """
        if (db is not None) and (inputs is not None):
            raise RuntimeError("Cannot specify both a DB and an input dict")
        return self._deps(name, db, inputs)


    def _run_max_procs(self, procs_per_node):
        raise NotImplementedError("You should not use a BaseTask object "
            " directly")
        return None


    def run_max_procs(self, procs_per_node):
        """Maximum number of processes supported by this task type.

        Args:
            procs_per_node (int): the number of processes running per node.

        Returns:
            int: the maximum number of processes.

        """
        return self._run_max_procs(procs_per_node)


    def _run_time(self, name, procs_per_node, db):
        raise NotImplementedError("You should not use a BaseTask object "
            " directly")
        return None


    def run_time(self, name, procs_per_node, db=None):
        """Estimated runtime for a task at maximum concurrency.

        Args:
            name (str): the name of the task.
            procs_per_node (int): the number of processes running per node.
            db (pipeline.DB): the optional database instance.

        Returns:
            int: estimated minutes of run time.

        """
        return self._run_time(name, procs_per_node, db)


    def _run_defaults(self):
        raise NotImplementedError("You should not use a BaseTask object "
            " directly")
        return None


    def run_defaults(self):
        """Default options.

        This dictionary of default options will be written to the options.yaml
        file in a production directory.  The options will then be loaded from
        that file at run time.

        Changes to this function will only impact newly-created productions,
        and these options will be overridden by any changes to the options.yaml
        file.

        Returns:
            dict: dictionary of default options.

        """
        return self._run_defaults()


    def _run_cli(self, name, opts, procs):
        raise NotImplementedError("You should not use a BaseTask object "
            " directly")
        return None


    def run_cli(self, name, opts, procs, launch=None, log=None):
        """Return the equivalent command-line interface.

        Args:
            name (str): the name of the task.
            opts (dict): dictionary of runtime options.
            procs (int): The number of processes to use.
            launch (str): optional launching command.
            log (str): optional log file for output.

        Returns:
            str: a command line.

        """
        comstr = self._run_cli(name, opts, procs)
        if launch is not None:
            comstr = "{} {} {}".format(launch, procs, comstr)
        if log is not None:
            comstr = "{} >{} 2>&1".format(comstr, log)
        return comstr


    def _run(self, name, opts, comm):
        raise NotImplementedError("You should not use a BaseTask object "
            " directly")
        return


    def run(self, name, opts, comm=None):
        """Run the task.

        Args:
            name (str): the name of this task.
            opts (dict): options to use for this task.
            comm (mpi4py.MPI.Comm): optional MPI communicator.

        Returns:
            int: the number of processes that failed.

        """
        log = get_logger()
        nproc = 1
        rank = 0
        if comm is not None:
            nproc = comm.size
            rank = comm.rank

        # at debug level, write out the equivalent commandline that was used
        if rank == 0:
            lstr = "(run by pipeline with {} procs)".format(nproc)
            com = self.run_cli(name, opts, nproc)
            log.debug("{}: {}".format(lstr, com))

        failed = 0
        try:
            self._run(name, opts, comm)
        except:
            msg = "FAILED: task {} process {}".format(name, rank)
            log.error(msg)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value,
                exc_traceback)
            log.error("".join(lines))
            failed = 1

        failcount = 0
        if comm is None:
            failcount = failed
        else:
            failcount = comm.allreduce(failed)

        if failcount > 0:
            if rank == 0:
                log.error("{} of {} processes raised an exception"\
                    .format(failcount, nproc))

        return failcount


    def run_and_update(self, db, name, opts, comm=None):
        """Run the task and update DB state.

        The state of the task is marked as "done" if the command completes
        without raising an exception and if the output files exist.

        Args:
            db (pipeline.db.DB): The database.
            name (str): the name of this task.
            opts (dict): options to use for this task.
            comm (mpi4py.MPI.Comm): optional MPI communicator.

        Returns:
            int: the number of processes that failed.

        """
        nproc = 1
        rank = 0
        if comm is not None:
            nproc = comm.size
            rank = comm.rank

        failed = self.run(name, opts, comm)

        if rank == 0:
            if failed > 0:
                self.state_set(db, name, "fail")
            else:
                outputs = self.paths(name)
                done = True
                for out in outputs:
                    if not os.path.isfile(out):
                        done = False
                        failed = nproc
                        break
                if done:
                    self.state_set(db, name, "done")
                else:
                    self.state_set(db, name, "fail")
        return failed
