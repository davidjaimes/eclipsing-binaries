---
layout: ../layouts/post-layout.astro
date: "Apr 01, 2023"
title: "KOI-3570: An Eclipsing Binary Star System"
path: /eclipsing-binaries
badges:
    - Python
    - Astropy
image: koi-3570-pflc.png
alt: koi-3570
excerpt: An eclipsing binary consists of two close stars moving in an orbit so placed in space in relation to Earth that the light of one can at times be hidden behind the other.
---

<br>

An eclipsing binary consists of two close stars moving in an orbit so placed in space in relation to Earth that the light of one can at times be hidden behind the other. Time series analysis in search for eclipsing binary stars can be daunting. Sometimes, it takes hours--even days or months--to find a single eclipsing binary in a dataset. However, when you find one, it is exciting. The following is an example light curve for target Kepler Object of Interest (KOI) 3570.

## KOI-3570
**KOI-3570** (aliases: **2MASS J19405783+4009273**, **KIC 5023948**, and **WISE J194057.82+400927.3**) is an eclipsing binary star system. It is a member of the old open cluster NGC 6819. By analyzing the eclipse properties of this system, we can measure the mass and radius of each star. These measurements can be used to precisely determine the age of the stars.

## Getting the data: FITS file
If you're familiar getting FITS files, then download the data from [Nasa Exoplanet Archive][1]. I downloaded the following batch file `download_exoarch_27821.bat` from the archive.

```bash
#!/bin/sh

# If wget is not installed on your system,
# please refer to http://irsa.ipac.caltech.edu/docs/batch_download_help.html.
#
# Windows users: the name of wget may have version number (ie: wget-1.10.2.exe)
# Please rename it to wget in order to successfully run this script
# Also the location of wget executable may need to be added to the PATH environment.
#
wget -O 'kplr005023948-2010355172524_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/281/81/kplr005023948-2010355172524_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2011073133259_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/415/00/kplr005023948-2011073133259_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2011177032512_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/314/41/kplr005023948-2011177032512_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2012004120508_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/482/00/kplr005023948-2012004120508_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2012088054726_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/514/78/kplr005023948-2012088054726_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2012179063303_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/548/10/kplr005023948-2012179063303_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2013011073258_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/614/95/kplr005023948-2013011073258_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2013098041711_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/647/84/kplr005023948-2013098041711_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2013131215648_llc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/681/29/kplr005023948-2013131215648_llc.fits' -a search_345998328.log
wget -O 'kplr005023948-2012060035710_slc.fits' 'http://exoplanetarchive.ipac.caltech.edu:80/data/ETSS//Kepler/005/753/70/kplr005023948-2012060035710_slc.fits' -a search_345998328.log

```

Change the script file's permissions to make it executable (for example, chmod 755 irsspect.bat):

```bash
chmod 755 download_exoarch_27821.bat
```

## Lightcurve
Use [AstroPy][3] to plot a lightcurve (flux vs time) for KOI-3570. I am using `kplr005023948-2012060035710_slc.fits` because it has the greatest amount of data points in any file on the batch list--over 40,000 points.

```python
from astropy.io import fits
import matplotlib.pyplot as plt

hdu = fits.open('kplr005023948-2012060035710_slc.fits')
time = hdu[1].data['TIME']
flux = hdu[1].data['SAP_FLUX']
plt.plot(time, flux, '.', markersize=1)
```
![koi-3570-lightcurve](/koi-3570-lc.png)

## Phase Fold Lightcurve
Arguably, one of the most important parameters to find for an eclipsing binary star system is the orbital period. There are many ways to find the period around the center of mass and the method I like to use is a multi-term Lomb-Scargle approach. For this system, I used the period published in Brewer et al. 2016. They found an orbital period of 3.649301 days. Phase folding the light curve with this orbital period yields the following plot. The secondary and primary eclipses are at about phase equal to 0.2 and 0.7, respectively.

```python
period = 3.649301
phase = (time - time[0]) / period % 1
plt.plot(phase, flux, '.', markersize=1)
```

![koi-3570-phasefold](/koi-3570-pflc.png)

## References
1. [Nasa Exoplanet Archive][1]
2. [Homebrew][2]
3. [AstroPy][3]

[1]: https://exoplanetarchive.ipac.caltech.edu
[2]: https://brew.sh/
[3]: https://www.astropy.org/
