===================
desispec Change Log
===================

0.34.5 (unreleased)
-------------------

* No changes yet.

0.34.4 (2020-04-21)
-------------------

* Add `desi_proc --batch-opts ...` option for specifying extras like
  queue reservation (direct push to master).

0.34.3 (2020-04-17)
-------------------

* Run desi_proc arc and flat jobs on max 10 nodes instead of 5 (PR `#958`_).

.. _`#958`: https://github.com/desihub/desispec/issues/958

0.34.2 (2020-04-16)
-------------------

* Include `data/spec-arc-lamps.dat` with installed data.
* Mask high readnoise CCD amps (PR `#957`_).

.. _`#957`: https://github.com/desihub/desispec/issues/957

0.34.1 (2020-04-15)
-------------------

* Expanded scan range for y traceshifts from +-3 to +-10 A
  (commit 26279d8 direct to master)
* Improved traceshift robusteness for very large shifts of arcs (PR `#954`).
* Added scripts for creating bad pixels masks from darks (PR `#946`_).
* etc/desispec.module use desi_spectro_calib tag 0.1.1 (PR `#955`_).
* import specter only if needed to run, not requiring it just to
  import desispec.io (PR `#955`_).

Note: `python setup.py install` of this version incorrectly doesn't copy
`data/spec-arc-lamps.dat` into the final installed data directory;
that is fixed in next version, and was fixed by hand in NERSC 0.34.1 install.

.. _`#946`: https://github.com/desihub/desispec/issues/946
.. _`#954`: https://github.com/desihub/desispec/issues/954
.. _`#955`: https://github.com/desihub/desispec/issues/955

0.34.0 (2020-04-13)
-------------------

Compatibility notes:

  * Requires desiutil >= 2.0.3 (PR `#951`_).
  * Backwards incompatible change to sky model format (PR `#939`_.

Changes:

* Refactor S/N fit for QA (PR `#917`_)
* Speed up QA (PR `#917`_)
* Don't mask extreme mask fiberflat >2 or <0.1 in routine autocalib_fiberflat
  because the fiberflat includes the throughput difference between
  spectrographs (push to master to address issue `#897`_).
* Modify overscan methods.  Default is to no longer analyze the ORSEC region
  (PR `#838`_).
* Fix sky subtraction with ivar=0 (PR `#920`_).
* Tweaks for logging nightly redshifts and srun (PR `#921`_).
* Added calib config management utilities (PR `#926`_).
* Coadd robustness when missing a camera (PR `#927`_).
* Shorter desi_proc job names (PR `#928`_).
* Set fiberstatus to mask fibers in bad regions of CCDs (PR `#930`_).
* Fix code generating fits reserved keyword warnings (PR `#933`_, `#935`_).
* Try fibermap header if primary header doesn't have RA,DEC (PR `#934`_).
* Force assemble_fibermap for nights before or during 20200310 (PR `#936`_).
* Don't fit traceshifts in y for dome and twilight flats (PR `#937`_).
* Calculate sky model throughput corrections when making sky model instead
  of while applying model.  Note: changes data model.  (PR `#939`_).
* Improve averaging of fiberflats (PR `#940`_).
* Fix incorrect multiple calls to bary_corr depending upon MPI parallelism,
  and merge extract main and main_mpi (PR `#943`_).
* Propagate MJD to spectra fibermap (PR `#944`_).
* Generate spectra files by default and don't coadd across cameras (PR `#945`_).
* Allow coadding across cameras of coadds (PR `#948`_).
* Implement fibermaps per camera (PR `#949`_).
* Use desiutil.iers.freeze_iers instead of desisurvey; requires desiutil>=2.0.3
  (PR `#951`_).
* Module file users desi_spectro_calib tag 0.1

.. _`#838`: https://github.com/desihub/desispec/issues/838
.. _`#897`: https://github.com/desihub/desispec/issues/897
.. _`#917`: https://github.com/desihub/desispec/issues/917
.. _`#920`: https://github.com/desihub/desispec/issues/920
.. _`#921`: https://github.com/desihub/desispec/issues/921
.. _`#926`: https://github.com/desihub/desispec/issues/926
.. _`#927`: https://github.com/desihub/desispec/issues/927
.. _`#928`: https://github.com/desihub/desispec/issues/928
.. _`#930`: https://github.com/desihub/desispec/issues/930
.. _`#933`: https://github.com/desihub/desispec/issues/933
.. _`#934`: https://github.com/desihub/desispec/issues/934
.. _`#935`: https://github.com/desihub/desispec/issues/935
.. _`#936`: https://github.com/desihub/desispec/issues/936
.. _`#937`: https://github.com/desihub/desispec/issues/937
.. _`#939`: https://github.com/desihub/desispec/issues/939
.. _`#940`: https://github.com/desihub/desispec/issues/940
.. _`#943`: https://github.com/desihub/desispec/issues/943
.. _`#944`: https://github.com/desihub/desispec/issues/944
.. _`#945`: https://github.com/desihub/desispec/issues/945
.. _`#948`: https://github.com/desihub/desispec/issues/948
.. _`#949`: https://github.com/desihub/desispec/issues/949
.. _`#951`: https://github.com/desihub/desispec/issues/951

0.33.0 (2020-03-05)
-------------------

* Metadata bookkeeping for early CMX data (PR `#857`_)
* Improved PSF handling in desi_proc (PR `#858`_)
* Modeling scattered light (PR `#859`_, `#861`_, `#862`_)
* desi_proc --calibnight option (PR `#860`_)
* expanding flux calib stdstar bits (PR `#862`_)
* new assemble_fibermap script (PR `#864`_, `#902`_)
* improved sky subtraction and flux calibration robustness (PR `#865`_)
* new desi_group_tileframes script; coadd frames directly (PR `#866`_)
* flux calibration improvements (PR `#868`_, `#871`_, `#880`_, `#898`_)
* more efficient desi_proc --batch parallelism packing (PR `#869`_)
* new desi_proc_dashboard script (PR `#870`_, `#901`_)
* new desi_dailyproc script (PR `#872`_, `#881`_, `#895`_)
* more robustness to missing inputs (PR `#875`_, `#876`_, `#883`_)
* groundwork for improving cosmics masking (PR `#878`_)
* enable barycentric correction in desi_proc (PR `#879`_)
* new plot_spectra script (PR `#890`_)
* new desi_nightly_redshifts script (PR `#892`_)
* Generate QA for a given night + QA bug fixes (PR `#894`_)
* coadd metadata propagation (PR `#900`_)
* don't use FIBERSTATUS!=0 spectra in coadds (PR `#903`_)
* desi_proc more control options for minisv2 run (PR `#904`_)
* Two hotfixes to master to re-enable daily processing:

  * make assemble_fibermap more robust to missing input columns
    in the platmaker coordinates files.
  * better packing of extraction MPI ranks

.. _`#857`: https://github.com/desihub/desispec/pull/857
.. _`#858`: https://github.com/desihub/desispec/pull/858
.. _`#859`: https://github.com/desihub/desispec/pull/859
.. _`#860`: https://github.com/desihub/desispec/pull/860
.. _`#861`: https://github.com/desihub/desispec/pull/861
.. _`#862`: https://github.com/desihub/desispec/pull/862
.. _`#864`: https://github.com/desihub/desispec/pull/864
.. _`#865`: https://github.com/desihub/desispec/pull/865
.. _`#866`: https://github.com/desihub/desispec/pull/869
.. _`#868`: https://github.com/desihub/desispec/pull/868
.. _`#869`: https://github.com/desihub/desispec/pull/869
.. _`#870`: https://github.com/desihub/desispec/pull/870
.. _`#871`: https://github.com/desihub/desispec/pull/871
.. _`#872`: https://github.com/desihub/desispec/pull/872
.. _`#875`: https://github.com/desihub/desispec/pull/875
.. _`#876`: https://github.com/desihub/desispec/pull/876
.. _`#878`: https://github.com/desihub/desispec/pull/878
.. _`#879`: https://github.com/desihub/desispec/pull/879
.. _`#880`: https://github.com/desihub/desispec/pull/880
.. _`#881`: https://github.com/desihub/desispec/pull/881
.. _`#883`: https://github.com/desihub/desispec/pull/883
.. _`#890`: https://github.com/desihub/desispec/pull/890
.. _`#892`: https://github.com/desihub/desispec/pull/892
.. _`#894`: https://github.com/desihub/desispec/pull/894
.. _`#895`: https://github.com/desihub/desispec/pull/895
.. _`#898`: https://github.com/desihub/desispec/pull/898
.. _`#900`: https://github.com/desihub/desispec/pull/900
.. _`#901`: https://github.com/desihub/desispec/pull/901
.. _`#902`: https://github.com/desihub/desispec/pull/902
.. _`#903`: https://github.com/desihub/desispec/pull/903
.. _`#904`: https://github.com/desihub/desispec/pull/904

0.32.1 (2019-12-27)
-------------------

* Integration test simulate past not current date to workaound
  pixsim header mismatch with :envvar:`DESI_SPECTRO_CALIB` calibrations.
  (direct push to master).

0.32.0 (2019-12-22)
-------------------

* Adding more desi_proc options (PR `#848`_, `#850`_).
* Support PSF bootstrapping with broken fibers (PR `#849`_).
* Hot fixes to desi_proc crashes (pushed directly to master).
* Increase cframe task from 1 min to 2 min (direct to master).
* Adapt to new spectrograph SMn naming (PR `#853`_).
* Workaround fitsio bug by setting blank keywords to ``None``;
  adapt to new fiberassign file names (PR `#855`_).

.. _`#848`: https://github.com/desihub/desispec/pull/848
.. _`#849`: https://github.com/desihub/desispec/pull/849
.. _`#850`: https://github.com/desihub/desispec/pull/850
.. _`#853`: https://github.com/desihub/desispec/pull/853
.. _`#855`: https://github.com/desihub/desispec/pull/855


0.31.0 (2019-10-31)
-------------------

First CMX release with bug fixes for on-sky data.

* Use rrdesi --no-mpi-abort feature (PR `#823`_).
* Added code to generate pixflats (PR `#824`_).
* Support extractions of data without fibermaps (PR `#825`_).
* Propagate FIBERMAP into preproc files (not just frames)
  (PR `#825`_ and `#829`_).
* Allow extraction wavelenghts slightly off CCD (PR `#836`_).
* PSF I/O pause before merging (PR `#836`_).
* Add `bin/desi_proc` single-exposure processing script (PR `#837`_).
* Use OBSTYPE instead of FLAVOR for desi_qproc (PR `#839`_).
* Bug fix for desi_proc double application of fiberflat (PR `#841`_).
* desi_proc options for non-default PSF and fiberflat (PR `#842`_).
* Correct fibermap to match what petal we are in (PR `#843`_).
* Update database loading to match current data model (PR `#844`_).
* Added desi_proc --batch option (PR `#845`_).

.. _`#823`: https://github.com/desihub/desispec/pull/823
.. _`#824`: https://github.com/desihub/desispec/pull/824
.. _`#825`: https://github.com/desihub/desispec/pull/825
.. _`#829`: https://github.com/desihub/desispec/pull/829
.. _`#836`: https://github.com/desihub/desispec/pull/836
.. _`#837`: https://github.com/desihub/desispec/pull/837
.. _`#839`: https://github.com/desihub/desispec/pull/839
.. _`#841`: https://github.com/desihub/desispec/pull/841
.. _`#842`: https://github.com/desihub/desispec/pull/842
.. _`#843`: https://github.com/desihub/desispec/pull/843
.. _`#844`: https://github.com/desihub/desispec/pull/844
.. _`#845`: https://github.com/desihub/desispec/pull/845

0.30.0 (2019-10-17)
-------------------

* qproc updates (PR `#787`_).
* QL bias (PR `#789`_).
* Heliocentric corrections (PR `#790`_).
* Update photometric filter usages (PR `#791`_).
* Add gain output option to desi_compute_gain
* Modify overscan subtraction algorithm in desi.preproc.preproc (PR `#793`_).
* Cleanup timing parameters (PR `#794`_).
* Pipeline docs (PR `#797`_).
* Correct for dark trail in raw images (PR `#798`_).
* `yaml.load()` to `yaml.save_load()` (PR `#801`_).
* help numba know the types (PR `#802`_).
* desi_pipe getready fix (PR `#803`_).
* Move raw data transfer scripts to desitransfer_ (PR `#804`_).
* spectra coaddition (PR `#805`_).
* memory constraints and load balancing (PR `#806`_ and `#809`_).
* preproc header keywords CCDSEC1-4 vs. A-D (PR `#807`_).
* Add `desi_pipe status` command (PR `#810`_).
* Convert any expid input into an int in QA (PR `#814`_).
* Support new FIBERASSIGN_X/Y instead of DESIGN_X/Y (PR `#821`_).
* Added hostname and jobid to task logging (PR `#822`_).

.. _desitransfer: https://github.com/desihub/desitransfer
.. _`#787`: https://github.com/desihub/desispec/pull/787
.. _`#789`: https://github.com/desihub/desispec/pull/789
.. _`#790`: https://github.com/desihub/desispec/pull/790
.. _`#791`: https://github.com/desihub/desispec/pull/791
.. _`#793`: https://github.com/desihub/desispec/pull/793
.. _`#794`: https://github.com/desihub/desispec/pull/794
.. _`#797`: https://github.com/desihub/desispec/pull/797
.. _`#798`: https://github.com/desihub/desispec/pull/798
.. _`#801`: https://github.com/desihub/desispec/pull/801
.. _`#802`: https://github.com/desihub/desispec/pull/802
.. _`#803`: https://github.com/desihub/desispec/pull/803
.. _`#804`: https://github.com/desihub/desispec/pull/804
.. _`#805`: https://github.com/desihub/desispec/pull/805
.. _`#806`: https://github.com/desihub/desispec/pull/806
.. _`#807`: https://github.com/desihub/desispec/pull/807
.. _`#809`: https://github.com/desihub/desispec/pull/809
.. _`#810`: https://github.com/desihub/desispec/pull/810
.. _`#814`: https://github.com/desihub/desispec/pull/814
.. _`#821`: https://github.com/desihub/desispec/pull/821
.. _`#822`: https://github.com/desihub/desispec/pull/822

0.29.0 (2019-05-30)
-------------------

* Add HPSS backup to the raw data transfer script (PR `#765`_).
* Update :mod:`desispec.database.redshift` for latest
  changes in fiberassign tile file data model (PR `#770`_).
* Constants, docs, and test cleanup (PR `#771`_, `#773`_, `#776`_).
* Tune cosmics masking parameters (PR `#775`_).
* Add desi_compute_pixmask (PR `#777`_).
* qproc updates for more flexibility and exposure flavors (PR `#778`_).
* Better io.findfile camera checks (PR `#780`_).
* Support SV1_DESI_TARGET (PR `#786`_).

.. _`#786`: https://github.com/desihub/desispec/pull/786
.. _`#780`: https://github.com/desihub/desispec/pull/780
.. _`#778`: https://github.com/desihub/desispec/pull/778
.. _`#777`: https://github.com/desihub/desispec/pull/777
.. _`#776`: https://github.com/desihub/desispec/pull/776
.. _`#775`: https://github.com/desihub/desispec/pull/775
.. _`#773`: https://github.com/desihub/desispec/pull/773
.. _`#771`: https://github.com/desihub/desispec/pull/771
.. _`#770`: https://github.com/desihub/desispec/pull/770
.. _`#765`: https://github.com/desihub/desispec/pull/765

0.28.0 (2019-02-28)
-------------------

* Update (non-essential) transfer script for spectrograph functional
  verification tests (PR `#758`_).
* New calibration data access (inc var. DESI_SPECTRO_CALIB
  replacing DESI_CCD_CALIBRATION_DATA) (PR `#753`_).
* Fix offline QA S/N vs. mag fits (PR `#763`_).

.. _`#753`: https://github.com/desihub/desispec/pull/753
.. _`#758`: https://github.com/desihub/desispec/pull/758
.. _`#763`: https://github.com/desihub/desispec/pull/763

0.27.1 (2019-01-28)
-------------------

* QL updates for January 2019 readiness review (PRs `#750`_, `#751`_, `#752`_,
  `#754`_, `#755`_, `#756`_, `#757`_).

.. _`#750`: https://github.com/desihub/desispec/pull/750
.. _`#751`: https://github.com/desihub/desispec/pull/751
.. _`#752`: https://github.com/desihub/desispec/pull/752
.. _`#754`: https://github.com/desihub/desispec/pull/754
.. _`#755`: https://github.com/desihub/desispec/pull/755
.. _`#756`: https://github.com/desihub/desispec/pull/756
.. _`#757`: https://github.com/desihub/desispec/pull/757

0.27.0 (2018-12-16)
-------------------

* DB loading targets columns `PRIORITY_INIT` and `NUMOBS_INIT`;
  requires desitarget/0.27.0 or later for DB loading (PR `#747`_).
* Fix S/N QA when inputs have NaNs (PR `#746`_).
* DB exposures table loading allows NaN entries for RA,DEC,SEEING,etc.
  for arc and flat calib exposures (PR `#743`_).
* Use new `desiutil.dust.ext_odonnell` function during flux-calibration
  (PR `#736`_).
* Add support for average flux calibration model in ccd_calibration_data
  repo (PR `#735`_).
* Support mockobs fibermap format with fewer columns (PR `#733`_).
* Upgrade data transfer script and add additional scripts (PR `#732`_).
* Fix desi_zcatalog RA_TARGET vs. TARGET_RA (PR `#723`_).
* Update redshift database data model and workaround a minor bad data problem (PR `#722`_).
* Refactor offline QA (S/N) to work with updated object typing
* Drop `contam_target` DB truth column; no longer in truth files
  (one-line commit to master, no PR).
* Bug fix in QA (S/N) + refactor exposure slurping (PR `#746`_)
* Refactor QA_Exposures, QA_Night, and QA_Prod; Generate new Prod QA (offline)

.. _`#722`: https://github.com/desihub/desispec/pull/722
.. _`#723`: https://github.com/desihub/desispec/pull/723
.. _`#732`: https://github.com/desihub/desispec/pull/732
.. _`#733`: https://github.com/desihub/desispec/pull/733
.. _`#735`: https://github.com/desihub/desispec/pull/735
.. _`#736`: https://github.com/desihub/desispec/pull/736
.. _`#737`: https://github.com/desihub/desispec/pull/737
.. _`#743`: https://github.com/desihub/desispec/pull/743
.. _`#746`: https://github.com/desihub/desispec/pull/746
.. _`#747`: https://github.com/desihub/desispec/pull/747

0.26.0 (2018-11-08)
-------------------

Major non-backwards compatible changes:

* Update to new fibermap format for consistency with targeting and
  fiber assignment (PR `#717`_).
* Include GAIN in preproc headers (PR `#715`_).
* Prototype data transfer status report webpage (PR `#714`_).
* Integrate qproc/qframe into quicklook (PR `#713`_).
* Quicklook flux calib and config edits (PR `#707`_).

.. _`#707`: https://github.com/desihub/desispec/pull/707
.. _`#713`: https://github.com/desihub/desispec/pull/713
.. _`#714`: https://github.com/desihub/desispec/pull/714
.. _`#715`: https://github.com/desihub/desispec/pull/715
.. _`#717`: https://github.com/desihub/desispec/pull/717

0.25.0 (2018-10-24)
-------------------

* QL algorithm, config, and format updates (PRs `#699`_, `#701`_, `#702`_).
  (Includes non-backwards compatible changes).

.. _`#699`: https://github.com/desihub/desispec/pull/699
.. _`#701`: https://github.com/desihub/desispec/pull/701
.. _`#702`: https://github.com/desihub/desispec/pull/702


0.24.0 (2018-01-05)
-------------------

* Quicklook updates (including non-backwards compatible changes)

  * New QL calibration QA metrics (PR `#677`_).
  * Update QL to use xytraceset instead of custom PSF (PR `#682`_).
  * Cleanup for robustness and maintainability (PR `#693`_).

* Offline QA updates

  * Integrates QL S/N QA into offline QA Frame object (PR `#675`_).
  * Additional offline QA plots on S/N (PR `#691`_).

* Spectroscopic pipeline updates

  * Option to generate bash scripts instead of slurm scripts (PR `#686`_).
  * new `desi_pipe go --resume` option (PR `#687`_).
  * `desi_pipe sync --force-spec-done` option (PR `#692`_)

* Miscellaneous

  * Work-around bug that forbids opening memory-mapped files in update mode
    on some NERSC filesystems (PR `#689`_).
  * Do not compress image masks (PR `#696`_).
  * Ensure that FITS files specify FITS-standard-compliant units (PR `#673`_).
  * Integration test fixes (PR `#695`_).

.. _`#673`: https://github.com/desihub/desispec/pull/673
.. _`#675`: https://github.com/desihub/desispec/pull/675
.. _`#677`: https://github.com/desihub/desispec/pull/677
.. _`#682`: https://github.com/desihub/desispec/pull/682
.. _`#686`: https://github.com/desihub/desispec/pull/686
.. _`#687`: https://github.com/desihub/desispec/pull/687
.. _`#689`: https://github.com/desihub/desispec/pull/689
.. _`#691`: https://github.com/desihub/desispec/pull/691
.. _`#692`: https://github.com/desihub/desispec/pull/692
.. _`#693`: https://github.com/desihub/desispec/pull/693
.. _`#695`: https://github.com/desihub/desispec/pull/695
.. _`#696`: https://github.com/desihub/desispec/pull/696

0.23.1 (2018-08-09)
-------------------

* Support STD/STD_FSTAR/STD_FAINT bit names (PR `#674`_).

.. _`#674`: https://github.com/desihub/desispec/pull/674

0.23.0 (2018-07-26)
-------------------

* Adds qproc algorithms and QFrame class (PR `#664`_).
* Adds `desi_pipe go` for production running (PR `#666`_).
* Increase job maxtime for edison realtime queue (PR `#667`_).
* Updates for running desispec on BOSS data (PR `#669`_).
* Fix QL for list vs. array change in specter/master (PR `#670`_).

.. _`#664`: https://github.com/desihub/desispec/pull/664
.. _`#666`: https://github.com/desihub/desispec/pull/666
.. _`#667`: https://github.com/desihub/desispec/pull/667
.. _`#669`: https://github.com/desihub/desispec/pull/669
.. _`#670`: https://github.com/desihub/desispec/pull/670

0.22.1 (2018-07-18)
-------------------

* Update processing of QL metrics (PR `#659`_).
* Refactor pipeline and integration test (PR `#660`_).
* Update redshift database to handle changes to fiberassign data model
  (PR `#662`_).
* Allow rows to be filtered when loading the redshift database (PR `#663`_).

.. _`#659`: https://github.com/desihub/desispec/pull/659
.. _`#660`: https://github.com/desihub/desispec/pull/660
.. _`#662`: https://github.com/desihub/desispec/pull/662
.. _`#663`: https://github.com/desihub/desispec/pull/663

0.22.0 (2018-06-30)
-------------------

This is the version used for mock observing in June 2018.  It includes an
update to the directory substructure where raw data are found, grouping each
exposure into a separate directory `$DESI_SPECTRO_DATA/{YEARMMDD}/{EXPID}/`.

* Faster traceshift code; requires numba (PR `#634`_).
* Fixed integration tests (PR `#635`_).
* Give empty HDUs am ``EXTNAME`` (PR `#636`_).
* Update redshift database loading in integration test (PR `#638`_).
* Integration test DB loading (PR `#640`_).
* Move ccd_calibration.yaml to SVN repo (PR `#641`_).
* Logging QA metric status for QLF (PR `#642`_).
* Supporting both new and old fibermap via io.read_fibermap (PP `#643`_).
* Faster lower memory preproc using numba (PR `#644`_)
* ivar bugfix in resample_flux interpolation (PR `#646`_).
* Many QL updates from mock observing (PR `#648`_).
* Raw data in NIGHT/EXPID/*.* instead of NIGHT/*.* (PR `#648`_).
* Fix cosmics masking near masked saturated pixels (PR `#649`_).
* Update edison realtime queue config to 25 nodes (PR `#650`_).
* trace_shift code supports PSF formats without "PSF" HDU (PR `#654`_).
* Change keyword ``clobber`` to ``overwrite`` in functions from ``astropy.io.fits`` (PR `#658`_).

.. _`#634`: https://github.com/desihub/desispec/pull/634
.. _`#635`: https://github.com/desihub/desispec/pull/635
.. _`#636`: https://github.com/desihub/desispec/pull/636
.. _`#638`: https://github.com/desihub/desispec/pull/638
.. _`#640`: https://github.com/desihub/desispec/pull/640
.. _`#641`: https://github.com/desihub/desispec/pull/641
.. _`#642`: https://github.com/desihub/desispec/pull/642
.. _`#643`: https://github.com/desihub/desispec/pull/643
.. _`#644`: https://github.com/desihub/desispec/pull/644
.. _`#646`: https://github.com/desihub/desispec/pull/646
.. _`#648`: https://github.com/desihub/desispec/pull/648
.. _`#649`: https://github.com/desihub/desispec/pull/649
.. _`#650`: https://github.com/desihub/desispec/pull/650
.. _`#654`: https://github.com/desihub/desispec/pull/654
.. _`#658`: https://github.com/desihub/desispec/pull/658

0.21.0 (2018-05-25)
-------------------

Major updates including non-backwards compatible changes to QL output format
and pipeline updates for semi-realtime nightly processing.

* Pipeline fix to allow redrock to use a full node per healpix (PR `#585`_).
* Update pipeline maxtime/maxnodes job calculation (PR `#588`_).
* Better sync of pixel tasks and DB sync bugfixes (PR `#590`_).
* Improved handling of errors in case of full job failure (PR `#592`_).
* QA speedups and improvements (PR `#593`_)

  * Add ability to load Frame without reading Resolution matrix
  * Refactor offline QA to use qaprod_dir more sensibly
  * Include hooks in QA to previous fiberflat file location (calib2d)
  * Inhibit scatter plot in skyredidual QA

* Pass MAG into output zbest file (PR `#595`_)
* Allow running multiple task types in a single job (PR `#601`_).
* Pipeline hooks for processing a single exposure (PR `#604`_).
* Override PSF file psferr to avoid masking bright lines.
  Requires specter > 0.8.1 (PR `#606`_).
* QL QA reorganization (PR `#577`_, `#600`_, `#607`_, `#613`_).
* Integration test and QA fixes (PR `#602`_ and `#605`_).
* New desi_night scripts for semi-realtime processing (PR `#609`_).
* Spectro teststand calibration/utility code updates (PR `#610`_)
* QL S/N vs. mag updates (PR `#611`_)
* QL resampling fixes (PR `#615`_)
* Merge database modules (PR `#616`_).
* Add flexure tests to QL (PR `#617`_).
* Added cori and edison realtime queue support (PR `#618`_, `#619`_, `#624`_).
* QL output format updates (PR `#623`_).

.. _`#577`: https://github.com/desihub/desispec/pull/577
.. _`#585`: https://github.com/desihub/desispec/pull/585
.. _`#588`: https://github.com/desihub/desispec/pull/588
.. _`#590`: https://github.com/desihub/desispec/pull/590
.. _`#592`: https://github.com/desihub/desispec/pull/592
.. _`#593`: https://github.com/desihub/desispec/pull/593
.. _`#595`: https://github.com/desihub/desispec/pull/595
.. _`#600`: https://github.com/desihub/desispec/pull/600
.. _`#601`: https://github.com/desihub/desispec/pull/601
.. _`#602`: https://github.com/desihub/desispec/pull/602
.. _`#604`: https://github.com/desihub/desispec/pull/604
.. _`#605`: https://github.com/desihub/desispec/pull/605
.. _`#606`: https://github.com/desihub/desispec/pull/606
.. _`#607`: https://github.com/desihub/desispec/pull/607
.. _`#609`: https://github.com/desihub/desispec/pull/609
.. _`#610`: https://github.com/desihub/desispec/pull/610
.. _`#611`: https://github.com/desihub/desispec/pull/611
.. _`#613`: https://github.com/desihub/desispec/pull/613
.. _`#615`: https://github.com/desihub/desispec/pull/615
.. _`#616`: https://github.com/desihub/desispec/pull/616
.. _`#617`: https://github.com/desihub/desispec/pull/617
.. _`#618`: https://github.com/desihub/desispec/pull/618
.. _`#619`: https://github.com/desihub/desispec/pull/619
.. _`#623`: https://github.com/desihub/desispec/pull/623
.. _`#624`: https://github.com/desihub/desispec/pull/624

0.20.0 (2018-03-29)
-------------------

Multiple non-backwards compatible changes:

* Astropy 2 compatibility (PR `#519`_).
* Update Travis tests to recent versions.
* Integration test fixes (PR `#552`_).
* Adds pipeline db count_task_states (PR `#552`_).
* Standardize spectro filenames/locations (PR `#545`_ and `#559`_).
* Complete rewrite of task pipelining (PR `#520`_, `#523`_, `#536`_, `#537`_,
  `#538`_, `#540`_, `#543`_, `#544`_, `#547`_, )
* QL format updates (`#517`_, `#554`_)
* module file set DESI_CCD_CALIBRATION_DATA (`#564`_).
* Optionally include RA,DEC in merged zcatalog (`#562`_).
* QL updates to S/N calculations (`#556`_).
* fix BUNIT, HPXNSIDE, HPXPIXEL keywords (PR `#566`_)

.. _`#517`: https://github.com/desihub/desispec/pull/517
.. _`#519`: https://github.com/desihub/desispec/pull/519
.. _`#520`: https://github.com/desihub/desispec/pull/520
.. _`#523`: https://github.com/desihub/desispec/pull/523
.. _`#536`: https://github.com/desihub/desispec/pull/536
.. _`#537`: https://github.com/desihub/desispec/pull/537
.. _`#538`: https://github.com/desihub/desispec/pull/538
.. _`#540`: https://github.com/desihub/desispec/pull/540
.. _`#543`: https://github.com/desihub/desispec/pull/543
.. _`#544`: https://github.com/desihub/desispec/pull/544
.. _`#545`: https://github.com/desihub/desispec/pull/545
.. _`#547`: https://github.com/desihub/desispec/pull/547
.. _`#552`: https://github.com/desihub/desispec/pull/552
.. _`#554`: https://github.com/desihub/desispec/pull/554
.. _`#556`: https://github.com/desihub/desispec/pull/556
.. _`#559`: https://github.com/desihub/desispec/pull/559
.. _`#562`: https://github.com/desihub/desispec/pull/562
.. _`#564`: https://github.com/desihub/desispec/pull/564
.. _`#566`: https://github.com/desihub/desispec/pull/566

0.19.0 (2018-03-01)
-------------------

* Update DB loading for desitarget 0.19.0 targets; make DB loading
  API less specific to datachallenge directory structure (PR `#516`_).

.. _`#516`: https://github.com/desihub/desispec/pull/516

0.18.0 (2018-02-23)
-------------------

* Replace deprecated scipy.stats.chisqprob with
  scipy.stats.distributions.chi2.sf for compatibility with
  scipy 1.0. (PR `#503`_)
* Faster desi_group_spectra that also propagates SCORES table
  (PR `#505`_ and `#507`_ )
* Add options for fitting spatially non-uniform sky (PR `#506`_)
* Fix logger redirection (PR `#508`_)
* Add hooks for MPI extraction timing benchmarks (PR `#509`_)
* QuickLook metric renaming (PR `#512`_)

.. _`#503`: https://github.com/desihub/desispec/pull/503
.. _`#505`: https://github.com/desihub/desispec/pull/505
.. _`#506`: https://github.com/desihub/desispec/pull/506
.. _`#507`: https://github.com/desihub/desispec/pull/507
.. _`#508`: https://github.com/desihub/desispec/pull/508
.. _`#509`: https://github.com/desihub/desispec/pull/509
.. _`#512`: https://github.com/desihub/desispec/pull/512

0.17.2 (2018-01-30)
-------------------

* Trace shift optimizations from analyzing teststand data (PR `#482`_).
* Minor QA edits to accommodate minitest (PR `#489`_)
* Additional QA edits including qaprod_root() method (PR `#490`_)
* Introduce QA_Night, QA_MultiExp and refactor QA_Prod accordingly (PR `#491`_)
* Add SCORES HDU to frame files (PR `#492`_)

.. _`#482`: https://github.com/desihub/desispec/pull/482
.. _`#489`: https://github.com/desihub/desispec/pull/489
.. _`#490`: https://github.com/desihub/desispec/pull/490
.. _`#491`: https://github.com/desihub/desispec/pull/491
.. _`#492`: https://github.com/desihub/desispec/pull/492

0.17.1 (2017-12-20)
-------------------

* Refactors spectral regouping to be faster and derive fibermap format
  from inputs (PR `#473`_).
* Removed deprecated Brick class, and unused coadds and redmonder zfind
  that were using Bricks (PR `#473`_).
* Adds skyline QA; fixes QA version usage (PR `#458`_).
* Fixes write_bintable bug if extname=None; fixes missing header comments
* spectro DB database loading updates (PR `#477`_).
* trace shift updates for fiber flats (PR `#479`_).
* Pipeline scaling updates (PR `#459`_ and `#466`_).

.. _`#458`: https://github.com/desihub/desispec/pull/458
.. _`#473`: https://github.com/desihub/desispec/pull/473
.. _`#477`: https://github.com/desihub/desispec/pull/477
.. _`#479`: https://github.com/desihub/desispec/pull/479
.. _`#459`: https://github.com/desihub/desispec/pull/459
.. _`#466`: https://github.com/desihub/desispec/pull/466

0.17.0 (2017-11-10)
-------------------

* Enabled specter.extract.ex2d nsubbundles option for faster extractions.
  Requires specter 0.8.1 (PR `#451`_).
* Fixed bug in :func:`desispec.parallel.dist_discrete` (PR `#446`_)
* Tuned pipeline for scaling tests (PR `#457`_)
* Improved wavelength fitting (via specex update) and sky model error
  propagation (PR `#459`_)
* Added QL fiberflat, py3 fixes, updated algorithms and config
* Many other QL updates (PR `#462`_)
* Enables MPI parallelism for desi_extract_spectra script (PR `#448`_)

.. _`#446`: https://github.com/desihub/desispec/pull/446
.. _`#448`: https://github.com/desihub/desispec/pull/448
.. _`#451`: https://github.com/desihub/desispec/pull/451
.. _`#457`: https://github.com/desihub/desispec/pull/457
.. _`#459`: https://github.com/desihub/desispec/pull/459
.. _`#462`: https://github.com/desihub/desispec/pull/462

0.16.0 (2017-09-29)
-------------------

* Small fixes to desi_qa_prod and qa_prod
* Removes a number of QL metrics from offline qa
* Fixes integration tests for desisim newexp refactor
* Removes spectra grouping by brick; nside=64 healpix grouping default
* Add get_nights method to io.meta (PR `#422`_)
* Add search_for_framefile method to io.frame (PR `#422`_)
* Add desi_qa_frame script to generate frame QA (PR `#424`_)
* Add frame_meta to parameters (for slurping the Frame headers) (PR `#425`_)
* Add get_reduced_frames() method to io.meta (PR `#425`_)
* Modifies QA_Prod meta file output to be JSON (PR `#425`_)
* Add load_meta() method to QA_Exposure (PR `#425`_)
* Add time_series ploting to desi_qa_prod (PR `#425`_)
* Add several new plots for skysub residuals (PR `#425`_)
* Adds method to generate QA Table for Prod (PR `#425`_)
* Refactor of skysubresid script (PR `#425`_)
* Refactor QA files to sit in their own folder tree (PR `#429`_)
* Generate HTML files with links to QA figures (PR `#429`_)
* Enable generation of Exposure level QA (PR `#429`_)
* Normalize fiberflat QA by fiber area (PR `#429`_)
* Fixed exptime in fluxcalib ZP calculation (PR `#429`_)
* Added find_exposure_night() method (PR `#429`_)
* Add MED_SKY metric to QA and bright/dark flag in desi_qa_prod
* Update pipeline code for specex and redrock (PR `#439`_ and `#440`_)
* Adds code for adjusting trace locations to match sky lines (PR `#433`_)
* Updates to DB loading (PR `#431`_)
* Adds pixelflat code (PR `#426`_)

.. _`#422`: https://github.com/desihub/desispec/pull/422
.. _`#424`: https://github.com/desihub/desispec/pull/424
.. _`#425`: https://github.com/desihub/desispec/pull/425
.. _`#426`: https://github.com/desihub/desispec/pull/426
.. _`#429`: https://github.com/desihub/desispec/pull/429
.. _`#431`: https://github.com/desihub/desispec/pull/431
.. _`#433`: https://github.com/desihub/desispec/pull/433
.. _`#439`: https://github.com/desihub/desispec/pull/439
.. _`#440`: https://github.com/desihub/desispec/pull/440

0.15.2 (2017-07-12)
-------------------

* Make the loading of libspecex through ctypes more robust and portable.
* QL configuration cleanup (PR `#389`_).
* Add extrapolate option to resample_flux (PR `#415`_).
* Sphinx and travis tests fixes.

.. _`#389`: https://github.com/desihub/desispec/pull/389
.. _`#415`: https://github.com/desihub/desispec/pull/415

0.15.1 (2017-06-19)
-------------------

* Fixed :func:`desispec.io.findfile` path for zbest and coadd (PR `#411`_).
* Add Notebook tutorial: introduction to reading and manipulating DESI spectra (PR `#408`_, `#410`_).
* Update quicklook configuration (PR `#395`_).
* Rename ``Spectra.fmap`` attribute to ``Spectra.fibermap`` (PR `#407`_).
* Enable ``desi_group_spectra`` to run without pipeline infrastructure (PR `#405`_).
* Update desispec.io.findfile spectra path to match dc17a (PR `#404`_).
* Load redshift catalog data from healpix-based zbest files (PR `#402`_).

.. _`#411`: https://github.com/desihub/desispec/pull/411
.. _`#410`: https://github.com/desihub/desispec/pull/410
.. _`#408`: https://github.com/desihub/desispec/pull/408
.. _`#395`: https://github.com/desihub/desispec/pull/395
.. _`#407`: https://github.com/desihub/desispec/pull/407
.. _`#405`: https://github.com/desihub/desispec/pull/405
.. _`#404`: https://github.com/desihub/desispec/pull/404
.. _`#402`: https://github.com/desihub/desispec/pull/402

0.15.0 (2017-06-15)
-------------------

* Refactor database subpackage and enable loading of both quicksurvey and
  pipeline outputs (PR `#400`_).
* Clean up pipeline script naming to be grouped by night.
* Modify pipeline to use Spectra objects grouped by HEALPix pixels instead
  of bricks.  Add entry point to regroup cframe data by pixel (PR `#394`_).
* Add a new class, Spectra, which encapsulates a grouping of 1D spectra
  in one or more bands.  Includes selection, updating, and I/O.
* Removed ``desispec.brick`` as it's now in :mod:`desiutil.brick` (PR `#392`_).
* Added function to calculate brick vertices at a given location (PR `#388`_).
* Added function to calculate brick areas at a given location (PR `#384`_).
* Add scripts for submitting nightly job chains.
* Production creation now correctly handles slicing by spectrograph.
* Pipeline job concurrency now computed based on task run time and
  efficient packing.
* Set default brick size to 0.25 sq. deg. in desispec.brick (PR `#378`_).
* Added function to calculate BRICKID at a given location (PR `#378`_).
* Additional LOCATION, DEVICE_LOC, and PETAL_LOC columns for fibermap (PR `#379`_).
* Create util.py in tests/ which is intended to contain methods to facilitate test runs
* Add vette() method for Frame class (PR `#386`_)
* Began a desispec parameter file:  data/params/desispec_param.yml
* Flux calibration improvements (PR `#390`_).

.. _`#386`: https://github.com/desihub/desispec/pull/386
.. _`#388`: https://github.com/desihub/desispec/pull/388
.. _`#384`: https://github.com/desihub/desispec/pull/384
.. _`#378`: https://github.com/desihub/desispec/pull/378
.. _`#379`: https://github.com/desihub/desispec/pull/379
.. _`#390`: https://github.com/desihub/desispec/pull/390
.. _`#392`: https://github.com/desihub/desispec/pull/392
.. _`#394`: https://github.com/desihub/desispec/pull/394
.. _`#400`: https://github.com/desihub/desispec/pull/400

0.14.0 (2017-04-13)
-------------------

* Replace all instances of :mod:`desispec.log` with ``desiutil.log``;
  :func:`~desispec.log.get_logger` now prints a warning that users need
  to switch.
* Working DTS delivery script and DTS simulator (PR `#367`_).
* Preproc updates for crosstalk and teststand data (PR `#370`_).
* Flux calibration algorithm updates (PR `#371`_).
* Adds quicklook integration test (PR `#361`_).
* Fixes brickname calculation (PR `#373`_).

.. _`#367`: https://github.com/desihub/desispec/pull/367
.. _`#370`: https://github.com/desihub/desispec/pull/370
.. _`#371`: https://github.com/desihub/desispec/pull/371
.. _`#361`: https://github.com/desihub/desispec/pull/361
.. _`#373`: https://github.com/desihub/desispec/pull/361

0.13.2 (2017-03-27)
-------------------

* Add framework for DTS delivery and nightly processing scripts (PR `#365`_).
* Force documentation errors to cause Travis errors (PR `#364`_).

.. _`#364`: https://github.com/desihub/desispec/pull/364
.. _`#365`: https://github.com/desihub/desispec/pull/365

0.13.1 (2017-03-03)
-------------------

* Fix installation of ``data/ccd/ccd_calibration.yaml``.

0.13.0 (2017-03-03)
-------------------

* Fix brick update corruption (PR `#314`_).
* Close PSF file after initializing PSF object.
* Refactor :mod:`desispec.io.database` to use SQLAlchemy_.
* Fix :func:`~desispec.pipeline.graph.graph_path` usage in workers.
* Update :func:`desispec.io.raw.write_raw` to enable writing simulated raw
  data with new headers.
* Allow ``test_bootcalib`` to run even if NERSC portal is returning 403 errors.
* Add ``bricksize`` property to desispec.brick.Bricks; allow
  `desispec.brick.Bricks.brickname` to specify bricksize.
* Do SVD inverses when cholesky decompositions fail in fiberflat, sky
  subtraction, and flux calibration.
* Algorithm updates for teststand and BOSS data
* pipeline updates for docker/shifter
* quicklook updates

.. _`#314`: https://github.com/desihub/desispec/pull/314
.. _SQLAlchemy: http://www.sqlalchemy.org

0.12.0 (2016-11-09)
-------------------

* Update integration test to use stdstar_templates_v1.1.fits.
* Support asymmetric resolution matrices (PR `#288`_).
* Quicklook updates (PR `#294`_, `#293`_, `#285`_).
* Fix BUNIT and wavelength f4 *versus* f8.
* Significant pipeline code refactor (PR `#300`_ and `#290`_).
* fix docstrings for sphinx build (PR `#308`_).

.. _`#288`: https://github.com/desihub/desispec/pull/288
.. _`#294`: https://github.com/desihub/desispec/pull/294
.. _`#293`: https://github.com/desihub/desispec/pull/293
.. _`#285`: https://github.com/desihub/desispec/pull/285
.. _`#300`: https://github.com/desihub/desispec/pull/300
.. _`#290`: https://github.com/desihub/desispec/pull/290
.. _`#308`: https://github.com/desihub/desispec/pull/308


0.11.0 (2016-10-14)
-------------------

* Update template Module file to reflect DESI+Anaconda infrastructure.
* Update redmonster wrapper for reproducibility.
* `desispec.io.brick.BrickBase.get_target_ids` returns target IDs in the order they appear in input file.
* Set BUNIT header keywords (PR `#284`_).
* Improved pipeline logging robustness.
* MPI updates for robustness and non-NERSC operation.
* More py3 fixes.

.. _`#284`: https://github.com/desihub/desispec/pull/284

0.10.0 (2016-09-10)
-------------------

PR `#266`_ update for Python 3.5:

* Many little updates to work for both python 2.7 and 3.5.
* Internally fibermap is now a :class:`~astropy.table.Table` instead of :class:`~astropy.io.fits.FITS_rec` table.
* Bug fix for flux calibration QA.
* Requires desiutil_ >= 1.8.0.

.. _`#266`: https://github.com/desihub/desispec/pull/266
.. _desiutil: https://github.com/desihub/desiutil

0.9.0 (2016-08-18)
------------------

PR `#258`_ (requires specter_ >= 0.6.0)

* Propagate pixel model goodness of fit to flag outliers from unmasked cosmics.
* desi_extract_spectra --model option to output 2D pixel model
* fix pipeline bug in call to desi_bootcalib (no --qafig option)
* adds extraction tests

Misc:

* desi_qa_skysub -- plots residuals (PR #259)
* More quicklook QA (PR #260 and #262)
* Added support for template groups in redmonster (PR #255)
* Lots more pipeline docs (PR #261)

.. _specter: https://github.com/desihub/specter
.. _`#258`: https://github.com/desihub/desispec/pull/258

0.8.1 (2016-07-18)
------------------

* added QA_Prod
* refactor of fluxcalib QA
* fixed pipeline QA figure output (pdf vs. yaml)

0.8.0 (2016-07-14)
------------------

* bootcalib robustness improvements
* improved fibermap propagation
* PRODNAME -> SPECPROD, TYPE -> SPECTYPE
* meaningful batch job names for each step
* better test coverage; more robust to test data download failures
* more quicklook metrics
* used for "oak1" production

0.7.0 and prior
----------------

* No changes.rst yet
