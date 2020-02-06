import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
# import glob
import os
import numpy as np
from scipy import stats
import pickle

plt.rc('font', family='Arial')
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'

# ROOTDIR = '/Users/efrazer/leadingarm/sightlines/'
OUTDIR = '/Users/efrazer/leadingarm/figures/'
PICKLEFILE = '/Users/efrazer/leadingarm/fitdict.pickle'

IONSTOUSE = {'ESO265-G23': ['SiII_1193', 'SiIII_1206', 'SiIV_1393'],
             'FAIRALL9': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'H1101-232': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'HE0153-4520': ['SiII_1190', 'SiIII_1206'],
             'HE0226-4110': ['CII_1334', 'SiIII_1206', 'CIV_1550'],
             'HE1159-1338': ['SiII_1193', 'SiIII_1206'],
             'IO-AND': ['SiII_1193', 'SiIII_1206', 'SiIV_1393'],
             'IRAS_F09539-0439': ['SiII_1190', 'SiIV_1393'],
             'LBQS0107-0235': ['CII_1334', 'SiIII_1206'],
             'MRC2251-178': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'MRK304': ['CII_1334', 'SiIII_1206', 'CIV_1550'],
             'MRK335': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'MRK1044': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'MRK1513': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PG0003+158': ['SiII_1193', 'SiIII_1206', 'CIV_1548'],
             'PG0026+129': ['CII_1334', 'SiIII_1206', 'SiIV_1393'],
             'PG0044+030': ['CII_1334', 'SiIII_1206'],
             'PG1011-040': ['SiII_1193', 'SiIII_1206'],
             'PG1049-005': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PG2349-014': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'PHL1811': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PHL2525': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PKS1101-325': ['SiII_1193', 'SiIII_1206'],
             'PKS1136-13': ['CII_1334', 'SiIII_1206'],
             'RBS144': ['SiII_1193', 'SiIII_1206'],
             'RBS1897': ['SiII_1260', 'SiIII_1206'],
             'SDSSJ015530.02-085704.0': ['SiII_1260', 'SiIII_1206', 'SiIV_1393'],
             'SDSSJ095915.60+050355.0': ['SiIII_1206', 'CIV_1548'],
             'SDSSJ234500.43-005936.0': ['SiII_1260', 'SiIII_1206', 'SiIV_1393'],
             'UGC12163': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'UVQSJ101629.20-315023.6': ['SiII_1260', 'SiIII_1206'],
             # 'ESO267-G13': ['SiII_1193'],
             # 'LBQS0107-0233': ['SiIII_1206', 'CIV_1548'],
             # 'NGC3125': ['SiII_1190'],
             # 'RX_J0209.5-0438': ['CII_1334', 'CIV_1548'],
             # 'SDSSJ001224.01-102226.5': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             # 'SDSSJ094331.60+053131.0': ['SiII_1193', 'SiIII_1206'],
             # 'SDSSJ225738.20+134045.0': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             }

# unload the dictionary
with open(PICKLEFILE, 'rb') as handle:
    fitdict = pickle.load(handle)

# set up the lists for each case
blist_la_lo = []
blist_ms_lo = []

blist_la_med = []
blist_ms_med = []

blist_la_hi = []
blist_ms_hi = []

nlist_la_lo = []
nlist_ms_lo = []

nlist_la_med = []
nlist_ms_med = []

nlist_la_hi = []
nlist_ms_hi = []

blist_la_cii = []
blist_la_civ = []
blist_ms_cii = []
blist_ms_civ = []

# collect the data
for sightline in fitdict:

    ionlist = IONSTOUSE[sightline]  # only use the ions hand selected for this plot (1 lo 1 med 1 hi)
    # for ion in fitdict[sightline] # this would use all the ions avaiable

    for dubion in ionlist:

        ion = dubion.split('_')[0]

        if ion in ['SiII']:

            if fitdict[sightline][ion]['direction'] == 'MS':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_ms_lo.append(bval)
                    nlist_ms_lo.append(nval)

                else:
                    continue

            elif fitdict[sightline][ion]['direction'] == 'LA':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_la_lo.append(bval)
                    nlist_la_lo.append(nval)

                else:
                    continue

            else:
                continue

        elif ion in ['CII']:

            if fitdict[sightline][ion]['direction'] == 'MS':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_ms_cii.append(bval)

                else:
                    continue

            elif fitdict[sightline][ion]['direction'] == 'LA':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_la_cii.append(bval)

                else:
                    continue

            else:
                continue

        elif ion in ['SiIII']:

            if fitdict[sightline][ion]['direction'] == 'MS':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_ms_med.append(bval)
                    nlist_ms_med.append(nval)

                else:
                    continue

            elif fitdict[sightline][ion]['direction'] == 'LA':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_la_med.append(bval)
                    nlist_la_med.append(nval)

                else:
                    continue

            else:
                continue

        elif ion in ['SiIV']:

            if fitdict[sightline][ion]['direction'] == 'MS':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_ms_hi.append(bval)
                    nlist_ms_hi.append(nval)

                else:
                    continue

            elif fitdict[sightline][ion]['direction'] == 'LA':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_la_hi.append(bval)
                    nlist_la_hi.append(nval)

                else:
                    continue

            else:
                continue

        elif ion in ['CIV']:

            if fitdict[sightline][ion]['direction'] == 'MS':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_ms_civ.append(bval)

                else:
                    continue

            elif fitdict[sightline][ion]['direction'] == 'LA':

                for bvalerr, bval, nval in zip(fitdict[sightline][ion]['components']['b value error'], fitdict[sightline][ion]['components']['b value'], fitdict[sightline][ion]['components']['column density']):

                    blist_la_civ.append(bval)

                else:
                    continue

            else:
                continue

        else:
            continue


#######################################################
# b value LA low vs LA high
#######################################################

binwidth = 5.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_la, bins_la, patches_la = plt.hist((blist_la_lo, blist_la_med, blist_la_hi),
                                     bins=np.arange(0, 70, binwidth),
                                     color=['orange', 'deeppink', 'deepskyblue'],
                                     rwidth=0.8,
                                     align='mid',
                                     edgecolor='k',
                                     alpha=0.7,
                                     density=True,
                                     label=['Si II, N={}'.format(len(blist_la_lo)),
                                            'Si III N={}'.format(len(blist_la_med)),
                                            'Si IV, N={}'.format(len(blist_la_hi))])

plt.xlabel('b-value (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
plt.xticks(bins_la)
plt.axvline(10, color='black', linewidth=2, linestyle='dashed', alpha=0.7)
plt.ylabel('relative number', fontsize=16)
# plt.yticks(np.arange(np.max(n_la))+1)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig(os.path.join(OUTDIR, 'hist-b-LA.pdf'))
plt.close()

# compute KS stats and print to screen for latex
kstest_la_b_lohi = stats.ks_2samp(blist_la_hi, blist_la_lo)
kstest_la_b_medhi = stats.ks_2samp(blist_la_hi, blist_la_med)
kstest_la_b_lomed = stats.ks_2samp(blist_la_med, blist_la_lo)
print('LA b-value stats')
print('Si II-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_la_b_lohi[0], kstest_la_b_lohi[1]))
print('Si III-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_la_b_medhi[0], kstest_la_b_medhi[1]))
print('Si II-III K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_la_b_lomed[0], kstest_la_b_lomed[1]))
print('Si II mean +/- std = {} +/- {}'.format(np.mean(blist_la_lo), np.std(blist_la_lo)))
print('Si III mean +/- std = {} +/- {}'.format(np.mean(blist_la_med), np.std(blist_la_med)))
print('Si IV mean +/- std = {} +/- {}'.format(np.mean(blist_la_hi), np.std(blist_la_hi)))
print(' ---------------------- ')

#######################################################
# b value Stream low vs Stream high
#######################################################

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_ms, bins_ms, patches_ms = plt.hist((blist_ms_lo, blist_ms_med, blist_ms_hi),
                                     bins=np.arange(0, 70, binwidth),
                                     color=['orange', 'deeppink', 'deepskyblue'],
                                     alpha=0.7,
                                     rwidth=0.8,
                                     edgecolor='k',
                                     align='mid',
                                     density=True,
                                     label=['Si II, N={}'.format(len(blist_ms_lo)),
                                            'Si III N={}'.format(len(blist_ms_med)),
                                            'Si IV, N={}'.format(len(blist_ms_hi))])

plt.xlabel('b-value (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
plt.xticks(bins_ms)
plt.axvline(10, color='black', linewidth=2, linestyle='dashed', alpha=0.7)
plt.ylabel('relative number', fontsize=16)
# plt.yticks(np.arange(np.max(n_ms))+1)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig(os.path.join(OUTDIR, 'hist-b-MS.pdf'))
plt.close()

# compute KS stats and print to screen for latex
kstest_ms_b_lohi = stats.ks_2samp(blist_ms_hi, blist_ms_lo)
kstest_ms_b_medhi = stats.ks_2samp(blist_ms_hi, blist_ms_med)
kstest_ms_b_lomed = stats.ks_2samp(blist_ms_med, blist_ms_lo)
print('MS b-value stats')
print('Si II-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_ms_b_lohi[0], kstest_ms_b_lohi[1]))
print('Si III-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_ms_b_medhi[0], kstest_ms_b_medhi[1]))
print('Si II-III K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_ms_b_lomed[0], kstest_ms_b_lomed[1]))
print('Si II mean +/- std = {} +/- {}'.format(np.mean(blist_ms_lo), np.std(blist_ms_lo)))
print('Si III mean +/- std = {} +/- {}'.format(np.mean(blist_ms_med), np.std(blist_ms_med)))
print('Si IV mean +/- std = {} +/- {}'.format(np.mean(blist_ms_hi), np.std(blist_ms_hi)))
print(' ---------------------- ')

#######################################################
# b value Stream low vs LA low + carbon
#######################################################

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_lo, bins_lo, patches_lo = plt.hist((blist_ms_lo + blist_ms_cii, blist_la_lo + blist_la_cii),
                                     bins=np.arange(0, 70, binwidth),
                                     color=['lime', 'darkviolet'],
                                     alpha=0.6,
                                     rwidth=0.8,
                                     align='mid',
                                     edgecolor='k',
                                     density=True,
                                     label=['Si II + C II in MS, N={}'.format(len(blist_ms_lo + blist_ms_cii)),
                                            'Si II + C II in LA, N={}'.format(len(blist_la_lo + blist_la_cii))])


plt.xlabel('b-value (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
plt.xticks(bins_lo)
plt.axvline(10, color='black', linewidth=2, linestyle='dashed', alpha=0.7)
plt.ylabel('relative number', fontsize=16)
# plt.yticks(np.arange(np.max(n_lo))+1)
plt.title('Low Ion Components in the LA and MS', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig(os.path.join(OUTDIR, 'hist-b-LO-C.pdf'))
plt.close()

# compute KS stats and print to screen for latex
kstest_lo_b = stats.ks_2samp(blist_la_lo + blist_la_cii, blist_ms_lo + blist_ms_cii)
print('Stream low vs LA low b-value stats')
print('K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_lo_b[0], kstest_lo_b[1]))
print(' ---------------------- ')

#######################################################
# b value Stream high vs LA high
#######################################################

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_hi, bins_hi, patches_hi = plt.hist((blist_ms_hi + blist_ms_civ, blist_la_hi + blist_la_civ),
                                     bins=np.arange(0, 70, binwidth),
                                     color=['lime', 'darkviolet'],
                                     alpha=0.6,
                                     rwidth=0.8,
                                     align='mid',
                                     density=True,
                                     edgecolor='k',
                                     label=['Si IV + C IV in MS, N={}'.format(len(blist_ms_hi + blist_ms_civ)),
                                            'Si IV + C IV in LA, N={}'.format(len(blist_la_hi + blist_la_civ))])

plt.xlabel('b-value (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
plt.xticks(bins_hi)
plt.axvline(10, color='black', linewidth=2, linestyle='dashed', alpha=0.7)
plt.ylabel('relative number', fontsize=16)
# plt.yticks(np.arange(np.max(n_hi))+1)
plt.title('High Ion Components in the LA and MS', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig(os.path.join(OUTDIR, 'hist-b-HI-C.pdf'))
plt.close()

# compute KS stats and print to screen for latex
kstest_hi_b = stats.ks_2samp(blist_la_hi + blist_la_civ, blist_ms_hi + blist_ms_civ)
print('Stream high vs LA high b-value stats')
print('K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_hi_b[0], kstest_hi_b[1]))
print(' ---------------------- ')


#######################################################
# Column Density la low vs la high
#######################################################

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

plt.xlabel('Column Density ' + r'$[\log(N/cm^{-2})]$', fontsize=16)
plt.xticks(bins_la_ncol)
plt.ylabel('relative number', fontsize=16)
# plt.yticks(np.arange(np.max(n_la_ncol))+1)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=13)
plt.setp(ax.get_yticklabels(), fontsize=13)
plt.savefig(os.path.join(OUTDIR, 'hist-N-LA.pdf'))
plt.close()

# compute KS stats and print to screen for latex
kstest_la_lohi = stats.ks_2samp(nlist_la_lo, nlist_la_hi)
kstest_la_lomed = stats.ks_2samp(nlist_la_lo, nlist_la_med)
kstest_la_medhi = stats.ks_2samp(nlist_la_med, nlist_la_hi)
print('LA Column density stats')
print('Si II-IV K-S D={:6.5f}, p={:6.5f}'.format(kstest_la_lohi[0], kstest_la_lohi[1]))
print('Si II-III K-S D={:6.5f}, p={:6.5f}'.format(kstest_la_lomed[0], kstest_la_lomed[1]))
print('Si III-IV K-S D={:6.5f}, p={:6.5f}'.format(kstest_la_medhi[0], kstest_la_medhi[1]))
print('Si II mean +/- std = {} +/- {}'.format(np.mean(nlist_la_lo), np.std(nlist_la_lo)))
print('Si III mean +/- std = {} +/- {}'.format(np.mean(nlist_la_med), np.std(nlist_la_med)))
print('Si IV mean +/- std = {} +/- {}'.format(np.mean(nlist_la_hi), np.std(nlist_la_hi)))
print(' ---------------------- ')


#######################################################
# Column Density Stream low vs Stream high
#######################################################

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

plt.xlabel('Column Density ' + r'$[\log(N/cm^{-2})]$', fontsize=16)
plt.xticks(bins_ms_ncol)
plt.ylabel('relative number', fontsize=16)
# plt.yticks(np.arange(np.max(n_ms_ncol))+1)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=13)
plt.setp(ax.get_yticklabels(), fontsize=13)
plt.savefig(os.path.join(OUTDIR, 'hist-N-MS.pdf'))
plt.close()

# compute KS stats and print to screen for latex
kstest_ms_lohi = stats.ks_2samp(nlist_ms_lo, nlist_ms_hi)
kstest_ms_lomed = stats.ks_2samp(nlist_ms_lo, nlist_ms_med)
kstest_ms_medhi = stats.ks_2samp(nlist_ms_med, nlist_ms_hi)
print('Stream Column density stats')
print('Si II-IV K-S D={:6.5f}, p={:6.5f}'.format(kstest_ms_lohi[0], kstest_ms_lohi[1]))
print('Si II-III K-S D={:6.5f}, p={:6.5f}'.format(kstest_ms_lomed[0], kstest_ms_lomed[1]))
print('Si III-IV K-S D={:6.5f}, p={:6.5f}'.format(kstest_ms_medhi[0], kstest_ms_medhi[1]))
print('Si II mean +/- std = {} +/- {}'.format(np.mean(nlist_ms_lo), np.std(nlist_ms_lo)))
print('Si III mean +/- std = {} +/- {}'.format(np.mean(nlist_ms_med), np.std(nlist_ms_med)))
print('Si IV mean +/- std = {} +/- {}'.format(np.mean(nlist_ms_hi), np.std(nlist_ms_hi)))
print(' ---------------------- ')


#######################################################
# b value LA CII vs LA CIV
#######################################################

binwidth = 5.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_la_c, bins_la_c, patches_la_c = plt.hist((blist_la_cii, blist_la_civ),
                                           bins=np.arange(0, 70, binwidth),
                                           color=['orange', 'deepskyblue'],
                                           rwidth=0.8,
                                           align='mid',
                                           edgecolor='k',
                                           alpha=0.7,
                                           density=True,
                                           label=['C II, N={}'.format(len(blist_la_cii)),
                                                  'C IV, N={}'.format(len(blist_la_civ))])

plt.xlabel('b-value (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
plt.xticks(bins_la_c)
plt.axvline(10, color='black', linewidth=2, linestyle='dashed', alpha=0.7)
plt.ylabel('relative number', fontsize=16)
# plt.yticks(np.arange(np.max(n_la))+1)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig(os.path.join(OUTDIR, 'hist-b-LA-C.pdf'))
plt.close()

# compute KS stats and print to screen for latex
kstest_la_b_lohi_c = stats.ks_2samp(blist_la_cii, blist_la_civ)
print('LA b-value stats -- CII + CIV')
print('C II-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_la_b_lohi_c[0], kstest_la_b_lohi_c[1]))

print('C II mean +/- std = {} +/- {}'.format(np.mean(blist_la_cii), np.std(blist_la_cii)))
print('C IV mean +/- std = {} +/- {}'.format(np.mean(blist_la_civ), np.std(blist_la_civ)))
print(' ---------------------- ')

#######################################################
# b value MS CII vs LA CIV
#######################################################

binwidth = 5.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_axisbelow(True)
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.xaxis.grid(color='lightgray', linestyle='dashed')
n_ms_c, bins_ms_c, patches_ms_c = plt.hist((blist_ms_cii, blist_ms_civ),
                                           bins=np.arange(0, 70, binwidth),
                                           color=['orange', 'deepskyblue'],
                                           rwidth=0.8,
                                           align='mid',
                                           edgecolor='k',
                                           alpha=0.7,
                                           density=True,
                                           label=['C II, N={}'.format(len(blist_ms_cii)),
                                                  'C IV, N={}'.format(len(blist_ms_civ))])

plt.xlabel('b-value (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
plt.xticks(bins_ms_c)
plt.axvline(10, color='black', linewidth=2, linestyle='dashed', alpha=0.7)
plt.ylabel('relative number', fontsize=16)
# plt.yticks(np.arange(np.max(n_la))+1)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig(os.path.join(OUTDIR, 'hist-b-MS-C.pdf'))
plt.close()

# compute KS stats and print to screen for latex
kstest_ms_b_lohi_c = stats.ks_2samp(blist_ms_cii, blist_ms_civ)
print('MS b-value stats -- CII + CIV')
print('C II-IV K-S Statistic D={:6.5f}, p-value={:6.5f}'.format(kstest_ms_b_lohi_c[0], kstest_ms_b_lohi_c[1]))

print('C II mean +/- std = {} +/- {}'.format(np.mean(blist_ms_cii), np.std(blist_ms_cii)))
print('C IV mean +/- std = {} +/- {}'.format(np.mean(blist_ms_civ), np.std(blist_ms_civ)))
print(' ---------------------- ')