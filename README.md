### Repo to maintain scripts and results of science project

#### Directories
`sightlines/` Contains all the data and VoigtFit scripts for each sightline.


#### Scripts
`make_vf_py.py` - Code to create the individual VoigtFit scripts for each sightline.

`makedatatable.py` - Code that takes the input `origdatafile.txt` from Fox et. al 2014 + 2018 and makes it into an astropy fits table. Outputs `datafile1418.fits`.

`organize.py` - Code to create all the subfolders for each sightline and copy the COS data to the correct spot.


### Plotting routines
`plotions.py` - makes plots showing the original spectra, the best fit line, and the centers of each component for each sightline. Set up to make a 2x3 plot grid (optimized for AAS poster).

`makemap.py` - makes a galactic coordinate map with colored points for the high-to-low ion ratios of each sightline.

`makehistograms.py` - makes histograms of b value and column densities for the LA and Stream