import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
import glob
import os
import numpy as np
from scipy import stats
import pickle

plt.rc('font',family='Arial')

ROOTDIR = '/Users/efrazer/leadingarm/sightlines/'
PICKLEFILE = '/Users/efrazer/leadingarm/fitdict.pickle'

ionstouse = {'SDSSJ234500.43-005936.0': ['SiII', 'SiIII', 'SiIV'],
             'RBS1897': ['SiII', 'SiIII', 'CIV'],
             'SDSSJ015530.02-085704.0': ['SiII', 'SiIII', 'SiIV'],
             'IO-AND': ['SiII', 'SiIII', 'SiIV'],
             'MRC2251-178': ['CII', 'SiIII', 'CIV'],
             'SDSSJ095915.60+050355.0': ['SiIII', 'CIV'],
             'RBS144': ['CII', 'SiIII'],
             'PG0026+129': ['CII', 'SiIII', 'SiIV'],
             'PKS1136-13': ['CII'],
             'HE0153-4520': ['SiII', 'SiIII'],
             'FAIRALL9': ['SiII', 'SiIII', 'SiIV'],
             'MRK304': ['CII', 'SiIII', 'CIV'],
             'LBQS0107-0233': ['SiIII', 'CIV'],
             'PKS1101-325': ['SiII'],
             'PG1049-005': ['CII', 'SiIII', 'CIV'],
             'SDSSJ094331.60+053131.0': ['SiII', 'SiIII'],
             'NGC3125': ['SiII'],
             'SDSSJ001224.01-102226.5': ['CII', 'SiIII', 'CIV'],
             'PG0003+158': ['SiII', 'SiIII', 'CIV'],
             'PHL1811': ['SiII', 'SiIII', 'CIV'],
             'UVQSJ101629.20-315023.6': ['SiII', 'SiIII'],
             'MRK1513': ['CII', 'SiIII', 'CIV'],
             'RX_J0209.5-0438': ['CII', 'CIV'],
             'ESO265-G23': ['SiII', 'SiIII', 'SiIV'],
             'PHL2525': ['CII', 'CIV'],
             'PG0044+030': ['CII', 'SiIII'],
             'ESO267-G13': ['SiII'],
             'NGC7714': [],
             'MRK1044': ['CII', 'SiIII', 'CIV'],
             'CD14-A05': [],
             'UGC12163': ['CII', 'SiIII', 'CIV'],
             'LBQS0107-0235': ['CII', 'SiIII', 'CIV'],
             'HE1159-1338': ['SiII', 'SiIII'],
             'MRK335': ['CII', 'SiIII', 'CIV'],
             'PG1011-040': ['SiII', 'SiIII'],
             'IRAS_F09539-0439': ['SiII', 'SiIV'],
             'PG2349-014': ['SiII', 'SiIII', 'SiIV'],
             'H1101-232': ['SiII', 'SiIII', 'SiIV'],
             'SDSSJ225738.20+134045.0': ['SiII', 'SiIII', 'SiIV']
             }

# unload the dictionary
with open(PICKLEFILE, 'rb') as handle:
    fitdict = pickle.load(handle)

# set up the lists for each case
blist_la_on_lo = []
blist_ms_on_lo = []
blist_la_off_lo = []
blist_ms_off_lo = []

blist_la_on_med = []
blist_ms_on_med = []
blist_la_off_med = []
blist_ms_off_med = []

blist_la_on_hi = []
blist_ms_on_hi = []
blist_la_off_hi = []
blist_ms_off_hi = []

nlist_la_on_lo = []
nlist_ms_on_lo = []
nlist_la_off_lo = []
nlist_ms_off_lo = []

nlist_la_on_med = []
nlist_ms_on_med = []
nlist_la_off_med = []
nlist_ms_off_med = []

nlist_la_on_hi = []
nlist_ms_on_hi = []
nlist_la_off_hi = []
nlist_ms_off_hi = []

# collect the data
for sightline in fitdict:

    ionlist = ionstouse[sightline]  # only use the ions hand selected for this plot (1 lo 1 med 1 hi)
    # for ion in fitdict[sightline] # this would use all the ions avaiable

    for ion in ionlist:

        # if ion in ['OI', 'CII', 'SII']:
        #
        #     if fitdict[sightline][ion]['direction'] == 'MS-Off':
        #
        #         blist_ms_off_lo.extend(fitdict[sightline][ion]['components']['b value'])
        #
        #     elif fitdict[sightline][ion]['direction'] == 'MS-On':
        #
        #         blist_ms_on_lo.extend(fitdict[sightline][ion]['components']['b value'])
        #
        #     elif fitdict[sightline][ion]['direction'] == 'LA-Off':
        #
        #         blist_la_off_lo.extend(fitdict[sightline][ion]['components']['b value'])
        #
        #     elif fitdict[sightline][ion]['direction'] == 'LA-On':
        #
        #         blist_la_on_lo.extend(fitdict[sightline][ion]['components']['b value'])
        #
        #     else:
        #         continue

        if ion in ['SiII']:

            if fitdict[sightline][ion]['direction'] == 'MS-Off':

                blist_ms_off_lo.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_ms_off_lo.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'MS-On':

                blist_ms_on_lo.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_ms_on_lo.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'LA-Off':

                blist_la_off_lo.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_la_off_lo.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'LA-On':

                blist_la_on_lo.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_la_on_lo.extend(fitdict[sightline][ion]['components']['column density'])

            else:
                continue

        elif ion in ['SiIII']:

            if fitdict[sightline][ion]['direction'] == 'MS-Off':

                blist_ms_off_med.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_ms_off_med.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'MS-On':

                blist_ms_on_med.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_ms_on_med.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'LA-Off':

                blist_la_off_med.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_la_off_med.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'LA-On':

                blist_la_on_med.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_la_on_med.extend(fitdict[sightline][ion]['components']['column density'])

            else:
                continue

        elif ion in ['SiIV']:

            if fitdict[sightline][ion]['direction'] == 'MS-Off':

                blist_ms_off_hi.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_ms_off_hi.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'MS-On':

                blist_ms_on_hi.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_ms_on_hi.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'LA-Off':

                blist_la_off_hi.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_la_off_hi.extend(fitdict[sightline][ion]['components']['column density'])

            elif fitdict[sightline][ion]['direction'] == 'LA-On':

                blist_la_on_hi.extend(fitdict[sightline][ion]['components']['b value'])
                nlist_la_on_hi.extend(fitdict[sightline][ion]['components']['column density'])

            else:
                continue

        # elif ion in ['CIV']:
        #
        #     if fitdict[sightline][ion]['direction'] == 'MS-Off':
        #
        #         blist_ms_off_hi.extend(fitdict[sightline][ion]['components']['b value'])
        #
        #     elif fitdict[sightline][ion]['direction'] == 'MS-On':
        #
        #         blist_ms_on_hi.extend(fitdict[sightline][ion]['components']['b value'])
        #
        #     elif fitdict[sightline][ion]['direction'] == 'LA-Off':
        #
        #         blist_la_off_hi.extend(fitdict[sightline][ion]['components']['b value'])
        #
        #     elif fitdict[sightline][ion]['direction'] == 'LA-On':
        #
        #         blist_la_on_hi.extend(fitdict[sightline][ion]['components']['b value'])

            # else:
            #     continue

        else:

            continue

# combine off and on numbers
blist_ms_lo = blist_ms_off_lo + blist_ms_on_lo
blist_ms_med = blist_ms_off_med + blist_ms_on_med
blist_ms_hi = blist_ms_off_hi + blist_ms_on_hi
blist_la_lo = blist_la_off_lo + blist_la_on_lo
blist_la_med = blist_la_off_med + blist_la_on_med
blist_la_hi = blist_la_off_hi + blist_la_on_hi


# B VALUE LA LO V HI
binwidth = 5.
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_la, bins_la, patches_la = plt.hist((blist_la_lo, blist_la_med, blist_la_hi),
                                     bins=np.arange(5, 85, binwidth),
                                     color=['orange', 'deeppink', 'deepskyblue'],
                                     rwidth=0.8,
                                     align='mid',
                                     edgecolor='k',
                                     alpha=0.7,
                                     density=True,
                                     label=['Si II, N={}'.format(len(blist_la_lo)),
                                            'Si III N={}'.format(len(blist_la_med)),
                                            'Si IV, N={}'.format(len(blist_la_hi))])

kstest_la_b_lohi = stats.ks_2samp(blist_la_hi, blist_la_lo)
kstest_la_b_medhi = stats.ks_2samp(blist_la_hi, blist_la_med)
kstest_la_b_lomed = stats.ks_2samp(blist_la_med, blist_la_lo)
plt.text(42, 0.075, 'Si II-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_la_b_lohi[0], kstest_la_b_lohi[1]))
plt.text(42, 0.07, 'Si III-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_la_b_medhi[0], kstest_la_b_medhi[1]))
plt.text(42, 0.065, 'Si II-III K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_la_b_lomed[0], kstest_la_b_lomed[1]))

plt.xlabel('b-value ' + r'$[km/s]$', fontsize=16)
plt.xticks(bins_la)
plt.ylabel('fraction of components', fontsize=16)
# plt.yticks(np.arange(np.max(n_la))+1)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('normedhists/hist-b-LA.pdf')
plt.close()

# B VALUE MS LO V HI
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_ms, bins_ms, patches_ms = plt.hist((blist_ms_lo, blist_ms_med, blist_ms_hi),
                                     bins=np.arange(5, 70, binwidth),
                                     color=['orange', 'deeppink', 'deepskyblue'],
                                     alpha=0.7,
                                     rwidth=0.8,
                                     edgecolor='k',
                                     align='mid',
                                     density=True,
                                     label=['Si II, N={}'.format(len(blist_ms_lo)),
                                            'Si III N={}'.format(len(blist_ms_med)),
                                            'Si IV, N={}'.format(len(blist_ms_hi))])

kstest_ms_b_lohi = stats.ks_2samp(blist_ms_hi, blist_ms_lo)
kstest_ms_b_medhi = stats.ks_2samp(blist_ms_hi, blist_ms_med)
kstest_ms_b_lomed = stats.ks_2samp(blist_ms_med, blist_ms_lo)
plt.text(32, 0.046, 'Si II-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_ms_b_lohi[0], kstest_ms_b_lohi[1]))
plt.text(32, 0.044, 'Si III-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_ms_b_medhi[0], kstest_ms_b_medhi[1]))
plt.text(32, 0.042, 'Si II-III K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_ms_b_lomed[0], kstest_ms_b_lomed[1]))

plt.xlabel('b-value ' + r'$[km/s]$', fontsize=16)
plt.xticks(bins_ms)
plt.ylabel('fraction of components', fontsize=16)
# plt.yticks(np.arange(np.max(n_ms))+1)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('normedhists/hist-b-MS.pdf')
plt.close()

# B VALUE MS LO V LA LO
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_lo, bins_lo, patches_lo = plt.hist((blist_ms_lo, blist_la_lo),
                                     bins=np.arange(5, 60, binwidth),
                                     color=['tomato', 'rebeccapurple'],
                                     alpha=0.7,
                                     rwidth=0.8,
                                     align='mid',
                                     edgecolor='k',
                                     density=True,
                                     label=['Si II in MS, N={}'.format(len(blist_ms_lo)),
                                            'Si II in LA, N={}'.format(len(blist_la_lo))])

kstest_lo_b = stats.ks_2samp(blist_la_lo, blist_ms_lo)
plt.text(32, 0.051, 'K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_lo_b[0], kstest_lo_b[1]))
plt.xlabel('b-value ' + r'$[km/s]$', fontsize=16)
plt.xticks(bins_lo)
plt.ylabel('fraction of components', fontsize=16)
# plt.yticks(np.arange(np.max(n_lo))+1)
plt.title('Low Ion Components in the LA and MS', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('normedhists/hist-b-LO.pdf')
plt.close()

# B VALUE MS HI V LA HI
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_hi, bins_hi, patches_hi = plt.hist((blist_ms_hi, blist_la_hi),
                                     bins=np.arange(5, 70, binwidth),
                                     color=['tomato', 'rebeccapurple'],
                                     alpha=0.7,
                                     rwidth=0.8,
                                     align='mid',
                                     density=True,
                                     edgecolor='k',
                                     label=['Si IV in MS, N={}'.format(len(blist_ms_hi)),
                                            'Si IV in LA, N={}'.format(len(blist_la_hi))])

kstest_hi_b = stats.ks_2samp(blist_la_hi, blist_ms_hi)
plt.text(40.2, 0.085, 'K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_hi_b[0], kstest_hi_b[1]))
plt.xlabel('b-value ' + r'$[km/s]$', fontsize=16)
plt.xticks(bins_hi)
plt.ylabel('fraction of components', fontsize=16)
# plt.yticks(np.arange(np.max(n_hi))+1)
plt.title('High Ion Components in the LA and MS', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('normedhists/hist-b-HI.pdf')
plt.close()


# combine off and on numbers
nlist_ms_lo = nlist_ms_off_lo + nlist_ms_on_lo
nlist_ms_med = nlist_ms_off_med + nlist_ms_on_med
nlist_ms_hi = nlist_ms_off_hi + nlist_ms_on_hi
nlist_la_lo = nlist_la_off_lo + nlist_la_on_lo
nlist_la_med = nlist_la_off_med + nlist_la_on_med
nlist_la_hi = nlist_la_off_hi + nlist_la_on_hi

# # Make the Column Density Plots now
#

# N VALUE LA LO V HI
binwidth = 0.25
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_la_ncol, bins_la_ncol, patches_la_ncol = plt.hist((nlist_la_lo, nlist_la_med, nlist_la_hi),
                                                    bins=np.arange(12, 14.5, binwidth),
                                                    color=['orange', 'deeppink', 'deepskyblue'],
                                                    align='mid',
                                                    histtype='bar',
                                                    rwidth=0.8,
                                                    alpha=0.7,
                                                    density=True,
                                                    edgecolor='k',
                                                    label=['Si II, N={}'.format(len(nlist_la_lo)),
                                                           'Si III, N={}'.format(len(nlist_la_med)),
                                                           'Si IV, N={}'.format(len(nlist_la_hi))])

kstest_la_lohi = stats.ks_2samp(nlist_la_lo, nlist_la_hi)
kstest_la_lomed = stats.ks_2samp(nlist_la_lo, nlist_la_med)
kstest_la_medhi = stats.ks_2samp(nlist_la_med, nlist_la_hi)
plt.text(13.4, 1.63, 'Si II-IV K-S D={:6.5f}, p={:6.5f}'.format(kstest_la_lohi[0], kstest_la_lohi[1]))
plt.text(13.4, 1.56, 'Si II-III K-S D={:6.5f}, p={:6.5f}'.format(kstest_la_lomed[0], kstest_la_lomed[1]))
plt.text(13.4, 1.49, 'Si III-IV K-S D={:6.5f}, p={:6.5f}'.format(kstest_la_medhi[0], kstest_la_medhi[1]))

plt.xlabel('Column Density ' + r'$[\log(N/cm^{-2})]$', fontsize=16)
plt.xticks(bins_la_ncol)
plt.ylabel('fraction of components', fontsize=16)
# plt.yticks(np.arange(np.max(n_la_ncol))+1)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=13)
plt.setp(ax.get_yticklabels(), fontsize=13)
plt.savefig('normedhists/hist-N-LA.pdf')
plt.close()

# N VALUE MS LO V HI
binwidth = 0.25
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_ms_ncol, bins_ms_ncol, patches_ms_ncol = plt.hist((nlist_ms_lo, nlist_ms_med, nlist_ms_hi),
                                                    bins=np.arange(11.75, 14.75, binwidth),
                                                    color=['orange', 'deeppink', 'deepskyblue'],
                                                    align='mid',
                                                    histtype='bar',
                                                    rwidth=0.8,
                                                    alpha=0.7,
                                                    density=True,
                                                    edgecolor='k',
                                                    label=['Si II, N={}'.format(len(nlist_ms_lo)),
                                                           'Si III, N={}'.format(len(nlist_ms_med)),
                                                           'Si IV, N={}'.format(len(nlist_ms_hi))])

kstest_ms_lohi = stats.ks_2samp(nlist_ms_lo, nlist_ms_hi)
kstest_ms_lomed = stats.ks_2samp(nlist_ms_lo, nlist_ms_med)
kstest_ms_medhi = stats.ks_2samp(nlist_ms_med, nlist_ms_hi)
plt.text(13.52, 1.4, 'Si II-IV K-S D={:6.5f}, p={:6.5f}'.format(kstest_ms_lohi[0], kstest_ms_lohi[1]))
plt.text(13.52, 1.32, 'Si II-III K-S D={:6.5f}, p={:6.5f}'.format(kstest_ms_lomed[0], kstest_ms_lomed[1]))
plt.text(13.52, 1.24, 'Si III-IV K-S D={:6.5f}, p={:6.5f}'.format(kstest_ms_medhi[0], kstest_ms_medhi[1]))

plt.xlabel('Column Density ' + r'$[\log(N/cm^{-2})]$', fontsize=16)
plt.xticks(bins_ms_ncol)
plt.ylabel('fraction of components', fontsize=16)
# plt.yticks(np.arange(np.max(n_ms_ncol))+1)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=13)
plt.setp(ax.get_yticklabels(), fontsize=13)
plt.savefig('normedhists/hist-N-MS.pdf')
plt.close()
