from astropy.table import Table
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord
import numpy as np
import cartopy.crs as ccrs


# read in data table
data = Table.read('/Users/efrazer/leadingarm/datafile1418.fits')

sldict = {'UVQSJ101629.20-315023.6':
              {'ion_label': ['Si II 1193', 'Si III 1206'],
               'ions': ['SiII', 'SiIII'],
               'dir': 'LA'},
          'CD14-A05':
              {'ion_label': ['Si II 1193', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'SDSSJ095915.60+050355.0':
              {'ion_label': ['Si III 1206', 'C IV 1548'],
               'ions': ['SiIII', 'CIV'],
               'dir': 'LA'},
          'PKS1101-325':
              {'ion_label': ['Si II 1190', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'NGC3125':
              {'ion_label': ['Si II 1190', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'IRAS_F09539-0439':
              {'ion_label': ['Si II 1190', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'SDSSJ234500.43-005936.0':
              {'ion_label': ['Si II 1260', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'MS'},
          'SDSSJ001224.01-102226.5':
              {'ion_label': ['C II 1334', 'C IV 1548'],
               'ions': ['CII', 'CIV'],
               'dir': 'MS'},
          'RBS144':
              {'ion_label': ['Si II 1193', 'Si III 1206'],
               'ions': ['SiII', 'SiIII'],
               'dir': 'MS'},
          'PHL2525':
              {'ion_label': ['C II 1334', 'C IV 1548'],
               'ions': ['CII', 'CIV'],
               'dir': 'MS'},
          'NGC7714':
              {'ion_label': ['C II 1334', 'C IV 1548'],
               'ions': ['CII', 'CIV'],
               'dir': 'MS'},
          'FAIRALL9':
              {'ion_label': ['Si II 1193', 'Si IV 1402'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'MS'}
          }

slname = []
lmsvals = []
bmsvals = []

for key in sldict:
    slname.append(key)
    lmsvals.append(data[np.where(data['target']==key)]['LMS'])
    bmsvals.append(data[np.where(data['target']==key)]['BMS'])


# use SkyCoord to create galactic coordinates out of the filtered dataset
c = SkyCoord(l=lmsvals, b=bmsvals, frame='galactic')

langle = coord.Angle(c.l)
langle = langle.wrap_at(180 * u.degree)
bangle = coord.Angle(c.b)

# make a color array from the filtered data
colorarray =

# make the plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='mollweide')
sc = ax.scatter(langle.radian, bangle.radian, c=colorarray, cmap=plt.cm.rainbow, marker='o', s=100)
bl = ax.scatter(langle.radian, bangle.radian, facecolors='none', edgecolors='black', marker='o', s=100)
plt.grid(True)
cbar = plt.colorbar(sc)
cbar.set_label(figtitle, labelpad=+1)
ax.set_xlabel('Magellanic Stream Longitude (Degrees)')
ax.set_ylabel('Magellanic Stream Latitude (Degrees)')
plt.savefig(outputname)