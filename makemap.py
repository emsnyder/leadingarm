from astropy.table import Table
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord
import numpy as np
import os

# read in data table
data = Table.read('/Users/efrazer/leadingarm/datafile1418.fits')
rootdir = '/Users/efrazer/leadingarm/sightlines/'

sldict = {'UVQSJ101629.20-315023.6':
              {'ion_label': ['Si II 1193', 'Si III 1206'],
               'ions': ['none'],
               'dir': 'LA'},
          'CD14-A05':
              {'ion_label': ['Si II 1193', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'SDSSJ095915.60+050355.0':
              {'ion_label': ['Si III 1206', 'C IV 1548'],
               'ions': ['none'],
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
               'ions': ['none'],
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


def extract_fits(input_path):
    compnum = []
    n = []
    n_err = []
    fitfile = open(input_path+'.fit', 'r')
    for line in fitfile:
        line = line.strip()
        if ('#' not in line) and (line != ''):
            compnum.append(int(line.split()[0]))
            n.append(float(line.split()[6]))
            n_err.append(float(line.split()[7]))

    return compnum, n, n_err


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
lown = []
highn = []
ndname = []
ndl = []
ndb = []

for key in sldict:

    if (sldict[key]['dir'] == 'MS') or (sldict[key]['dir'] == 'LA'):

        for i, ion in enumerate(sldict[key]['ions']):

            if ion == 'none':
                ndname.append(key)
                ndl.append(data[np.where(data['target'] == key)]['l'])
                ndb.append(data[np.where(data['target'] == key)]['b'])
                continue

            if i == 0:
                slname.append(key)
                lvals.append(data[np.where(data['target'] == key)]['l'])
                bvals.append(data[np.where(data['target'] == key)]['b'])

            if (ion == 'CII') or (ion == 'SiII'):

                slpath = os.path.join(rootdir, key, key + '-' + ion)
                comp, nval, nval_err = extract_fits(slpath)
                logsum = np.log10(np.sum([10 ** x for x in nval[1::]]))
                lown.append(logsum)

            elif (ion == 'SiIV') or (ion == 'CIV'):

                slpath = os.path.join(rootdir, key, key + '-' + ion)
                comp, nval, nval_err = extract_fits(slpath)
                logsum = np.log10(np.sum([10 ** x for x in nval[1::]]))
                highn.append(logsum)

            else:
                raise ValueError('huh')


ratio = np.array(highn)/np.array(lown)

# use SkyCoord to create galactic coordinates out of the filtered dataset
c = SkyCoord(l=lvals, b=bvals, frame='galactic')
ndc = SkyCoord(l=ndl, b=ndb, frame='galactic')

langle = coord.Angle(c.l)
langle = langle.wrap_at(180 * u.degree)
bangle = coord.Angle(c.b)

ndlangle = coord.Angle(ndc.l)
ndlangle = ndlangle.wrap_at(180 * u.degree)
ndbangle = coord.Angle(ndc.b)

colorarray = ratio

degree_sign = u'\N{DEGREE SIGN}'
newticks = [str(np.int(x))+degree_sign for x in np.arange(150., -151, -30)]

# make the plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='mollweide')
sc = ax.scatter(langle.radian.flatten()*-1., bangle.radian.flatten(), c=colorarray, cmap=plt.cm.rainbow, marker='o', s=150)
bl = ax.scatter(langle.radian.flatten()*-1., bangle.radian.flatten(), facecolors='none', edgecolors='black', marker='o', s=150)
scnd = ax.scatter(ndlangle.radian.flatten()*-1., ndbangle.radian.flatten(), c='white', marker='o', s=150)
blnd = ax.scatter(ndlangle.radian.flatten()*-1., ndbangle.radian.flatten(), facecolors='none', edgecolors='black', marker='o', s=150)

plt.grid(True)
cbar = plt.colorbar(sc, orientation='vertical')
cbar.set_label('log(high/low ion column density)', labelpad=+6, fontsize=16)
ax.set_xlabel('Galactic Longitude', fontsize=16)
ax.set_ylabel('Galactic Latitude', fontsize=16)
ax.set_xticklabels(newticks)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('fullmap_ratio_vert.pdf')
