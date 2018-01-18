""" Class to organize QA for a full DESI production run
"""

from __future__ import print_function, absolute_import, division

import numpy as np
import glob, os
import warnings

from desispec.io import get_exposures
from desispec.io import get_files
from desispec.io import read_meta_frame
from desispec.io import specprod_root
from desispec.io import get_nights
from .qa_multiexp import QA_MultiExp

from desiutil.log import get_logger

# log = get_logger()


class QA_Prod(QA_MultiExp):
    def __init__(self, specprod_dir=None):
        """ Class to organize and execute QA for a DESI production

        Args:
            specprod_dir(str): Path containing the exposures/ directory to use. If the value
                is None, then the value of :func:`specprod_root` is used instead.
        Notes:

        Attributes:
            qa_exps : list
              List of QA_Exposure classes, one per exposure in production
            data : dict
        """
        if specprod_dir is None:
            specprod_dir = specprod_root()
        self.specprod_dir = specprod_dir
        # Init
        QA_MultiExp.__init__(self, specprod_dir=specprod_dir)
        # Load up exposures
        nights = get_nights(specprod_dir=self.specprod_dir)
        for night in nights:
            self.mexp_dict[night] = {}
            for exposure in get_exposures(night, specprod_dir = self.specprod_dir):
                # Object only??
                frames_dict = get_files(filetype = str('frame'), night = night,
                                        expid = exposure, specprod_dir = self.specprod_dir)
                self.mexp_dict[night][exposure] = frames_dict

    def load_data(self, inroot=None):
        """ Load QA data from disk
        """
        from desispec.io.qa import load_qa_prod
        #
        if inroot is None:
            inroot = self.specprod_dir+'/QA/'+self.prod_name+'_qa'
        self.data = load_qa_prod(inroot)

    def make_frameqa(self, make_plots=False, clobber=False):
        """ Work through the Production and make QA for all frames

        Parameters:
            make_plots: bool, optional
              Remake the plots too?
            clobber: bool, optional
        Returns:

        """
        # imports
        from desispec.qa.qa_frame import qaframe_from_frame
        from desispec.io.qa import qafile_from_framefile

        # Loop on nights
        nights = get_nights(specprod_dir=self.specprod_dir)
        for night in nights:
            for exposure in get_exposures(night, specprod_dir = self.specprod_dir):
                # Object only??
                frames_dict = get_files(filetype = str('frame'), night = night,
                        expid = exposure, specprod_dir = self.specprod_dir)
                for camera,frame_fil in frames_dict.items():
                    # Load frame
                    qafile, _ = qafile_from_framefile(frame_fil)
                    if os.path.isfile(qafile) and (not clobber):
                        continue
                    qaframe_from_frame(frame_fil, make_plots=make_plots)

    def slurp(self, make_frameqa=False, remove=True, **kwargs):
        """ Slurp all the individual QA files into one master QA file
        Args:
            make_frameqa: bool, optional
              Regenerate the individual QA files (at the frame level first)
            remove: bool, optional
              Remove

        Returns:

        """
        from desispec.qa import QA_Exposure
        from desispec.io import write_qa_prod
        log = get_logger()
        # Remake?
        if make_frameqa:
            self.make_frameqa(**kwargs)
        # Loop on nights
        nights = get_nights(specprod_dir=self.specprod_dir)
        # Reset
        log.info("Resetting qa_exps in qa_prod")
        self.qa_exps = []
        # Loop
        for night in nights:
            # Loop on exposures
            for exposure in get_exposures(night, specprod_dir = self.specprod_dir):
                frames_dict = get_files(filetype = str('frame'), night = night,
                                        expid = exposure, specprod_dir = self.specprod_dir)
                if len(frames_dict) == 0:
                    continue
                # Load any frame (for the type and meta info)
                key = list(frames_dict.keys())[0]
                frame_fil = frames_dict[key]
                frame_meta = read_meta_frame(frame_fil)
                qa_exp = QA_Exposure(exposure, night, frame_meta['FLAVOR'],
                                     specprod_dir=self.specprod_dir, remove=remove)
                qa_exp.load_meta(frame_meta)
                # Append
                self.qa_exps.append(qa_exp)
        # Write
        outroot = self.specprod_dir+'/QA/'+self.prod_name+'_qa'
        write_qa_prod(outroot, self)

    def __repr__(self):
        """ Print formatting
        """
        return ('{:s}: specprod_dir={:s}'.format(self.__class__.__name__, self.specprod_dir))
