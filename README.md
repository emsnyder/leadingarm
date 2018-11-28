Repo to maintain scripts and results of science project

`sightlines/` Contains all the data and VoigtFit scripts for each sightline.

`make_vf_py.py` - Code to create the individual VoigtFit scripts for each sightline.

`makedatatable.py` - Code that takes the input `origdatafile.txt` from Fox et. al 2014 + 2018 and makes it into an astropy fits table. Outputs `datafile1417.fits`.

`organize.py` - Code to create all the subfolders for each sightline and copy the COS data to the correct spot.