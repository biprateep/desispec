.. code-block:: console

    $> desi_pipe top --once
    ----------------+---------+---------+---------+---------+---------+---------+
       Task Type    | waiting | ready   | running | done    | failed  | submit  |
    ----------------+---------+---------+---------+---------+---------+---------+
    preproc         |        0|      690|        0|        0|        0|        0|
    psf             |      180|        0|        0|        0|        0|        0|
    psfnight        |       60|        0|        0|        0|        0|        0|
    traceshift      |      510|        0|        0|        0|        0|        0|
    extract         |      510|        0|        0|        0|        0|        0|
    fiberflat       |      180|        0|        0|        0|        0|        0|
    fiberflatnight  |       60|        0|        0|        0|        0|        0|
    sky             |      330|        0|        0|        0|        0|        0|
    starfit         |      110|        0|        0|        0|        0|        0|
    fluxcalib       |      330|        0|        0|        0|        0|        0|
    cframe          |      330|        0|        0|        0|        0|        0|
    spectra         |       53|        0|        0|        0|        0|       NA|
    redshift        |       53|        0|        0|        0|        0|       NA|
    ----------------+---------+---------+---------+---------+---------+---------+
