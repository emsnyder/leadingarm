from astropy.table import Table
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord
import numpy as np


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

# slname = []
# lvals = []
# bvals = []
# hivals = []
#
# for key in sldict:
#     slname.append(key)
#     lvals.append(data[np.where(data['target'] == key)]['l'])
#     bvals.append(data[np.where(data['target'] == key)]['b'])
#     hivals.append(data[np.where(data['target'] == key)]['log(SiIV/SiII)'])
#
# # use SkyCoord to create galactic coordinates out of the filtered dataset
# c = SkyCoord(l=lvals, b=bvals, frame='galactic')
#
# langle = coord.Angle(c.l)
# langle = langle.wrap_at(180 * u.degree)
# bangle = coord.Angle(c.b)
#
# # make a color array from the filtered data
# colorarray = hivals
#
# degree_sign = u'\N{DEGREE SIGN}'
# newticks = [str(np.int(x))+degree_sign for x in np.arange(150., -151, -30)]
#
# # make the plot
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection='mollweide')
# sc = ax.scatter(langle.radian*-1., bangle.radian, c=colorarray, cmap=plt.cm.rainbow, marker='o', s=150)
# bl = ax.scatter(langle.radian*-1., bangle.radian, facecolors='none', edgecolors='black', marker='o', s=150)
# for n, xy in enumerate(zip(langle.radian*-1., bangle.radian, slname)):
#     ax.annotate('{}'.format(n+1), xy=(xy[0],xy[1]), textcoords='data')
#     print('{} = {}'.format(n+1, xy[2]))
# plt.grid(True)
# cbar = plt.colorbar(sc, orientation='vertical')
# cbar.set_label('H I Column Density ' + r'$[log(N/cm^{-2})]$', labelpad=+6, fontsize=16)
# ax.set_xlabel('Galactic Longitude', fontsize=16)
# ax.set_ylabel('Galactic Latitude', fontsize=16)
# ax.set_xticklabels(newticks)
# plt.setp(ax.get_xticklabels(), fontsize=14)
# plt.setp(ax.get_yticklabels(), fontsize=14)
# plt.savefig('fullmap_labels.pdf')


slname = []
lvals = []
bvals = []
hivals = []

for key in sldict:
    slname.append(key)
    lvals.append(data[np.where(data['target'] == key)]['l'])
    bvals.append(data[np.where(data['target'] == key)]['b'])
    hivals.append(data[np.where(data['target'] == key)]['log(SiIV/SiII)'])

# use SkyCoord to create galactic coordinates out of the filtered dataset
c = SkyCoord(l=lvals, b=bvals, frame='galactic')

langle = coord.Angle(c.l)
langle = langle.wrap_at(180 * u.degree)
bangle = coord.Angle(c.b)

# make a color array from the filtered data
colorarray = hivals

degree_sign = u'\N{DEGREE SIGN}'
newticks = [str(np.int(x))+degree_sign for x in np.arange(150., -151, -30)]

# make the plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='mollweide')
sc = ax.scatter(langle.radian*-1., bangle.radian, c=colorarray, cmap=plt.cm.rainbow, marker='o', s=150)
bl = ax.scatter(langle.radian*-1., bangle.radian, facecolors='none', edgecolors='black', marker='o', s=150)
for n, xy in enumerate(zip(langle.radian*-1., bangle.radian, slname)):
    ax.annotate('{}'.format(n+1), xy=(xy[0],xy[1]), textcoords='data')
    print('{} = {}'.format(n+1, xy[2]))
plt.grid(True)
cbar = plt.colorbar(sc, orientation='vertical')
cbar.set_label('H I Column Density ' + r'$[log(N/cm^{-2})]$', labelpad=+6, fontsize=16)
ax.set_xlabel('Galactic Longitude', fontsize=16)
ax.set_ylabel('Galactic Latitude', fontsize=16)
ax.set_xticklabels(newticks)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('fullmap_labels.pdf')
