import pickle
import numpy as np

ROOTDIR = '/Users/efrazer/leadingarm/sightlines/'
PICKLEFILE = '/Users/efrazer/leadingarm/fitdict.pickle'

with open(PICKLEFILE, 'rb') as handle:
    fitdict = pickle.load(handle)

sortedsightlines = sorted(fitdict, key=lambda x: (fitdict[x]['direction'], x))

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


biglist = [' ']

for sightline in sortedsightlines:

    for dubion in IONSTOUSE[sightline]:   #['CII', 'CIV', 'SiII', 'SiIII', 'SiIV']:  # taking out OI and SII

        ion = dubion.split('_')[0]

        try:
            iondict = fitdict[sightline][ion]['components']

        except KeyError:
            continue

        num = len(iondict['component number'])

        for n in np.arange(num):

            row = []

            # save the sightline name
            if np.any([sightline in mylist for mylist in biglist]):
                row.append(' ')
                row.append(' ')

            else:

                if 'SDSS' in sightline or 'UVQS' in sightline:
                    row.append('\\footnotesize{' + sightline + '}')
                else:
                    row.append(sightline)

                row.append(fitdict[sightline][ion]['direction'])

            # if (ion in biglist[-1]):
            # # if (ion in biglist[-1]) and (biglist[-1].split('&')[0].strip() != ''):
            #     row.append(' ')
            #     row.append(' ')

            # elif biglist[-1].split('&')[2].strip() == '':
            #
            #     if (ion in biglist[-2]) and (biglist[-2].split('&')[0].strip() != ''):
            #         row.append(' ')
            #         row.append(' ')
            #
            # elif biglist[-2].split('&')[2].strip() == '':
            #
            #     if (ion in biglist[-3]) and (biglist[-3].split('&')[0].strip() != ''):
            #         row.append(' ')
            #         row.append(' ')

            # else:
            row.append(ion)
            row.append('$' + str(np.int(fitdict[sightline][ion]['S/N'].round(0))) + '$')

            row.append('$' + '{:6.1f}'.format(iondict['redshift'][n] * 3.e5).strip() + '\pm' + '{:6.1f}'.format(iondict['redshift error'][n] * 3.e5).strip() + '$')
            # row.append('$' + '{:10.6f}'.format(iondict['redshift'][n]).strip() + '\pm' + '{:10.6f}'.format(iondict['redshift error'][n]).strip() + '$')

            row.append('$' + '{:6.1f}'.format(iondict['b value'][n]) + '\pm' + '{:6.1f}'.format(iondict['b value error'][n]) + '$')

            row.append('$' + '{:6.3f}'.format(iondict['column density'][n]) + '\pm' + '{:6.3f}'.format(iondict['column density error'][n]) + '$')

            biglist.append(' & '.join(row) + '\\\ ')

myfile = open('final-fit-table.tex', 'w+')
myfile.write("\n")
myfile.write("\\startlongtable\n")
myfile.write("\\begin{deluxetable*}{lllrrrr}\n")
myfile.write("\\tablewidth{0pt}\n")
myfile.write("\\tablecaption{}\n")
myfile.write("\\tablehead{Sightline & Sample & Ion & $S/N$ & $v_0$ & $b$ & log\\,$N$(ion)\\\ \n")
myfile.write("                     &        &     &  (per resel)  & (km s$^{-1}$) & (km s$^{-1}$) & ($N$ in cm$^{-2}$)}\n")
myfile.write("\\startdata\n")
for item in biglist:
    if '_' in item:
        item.replace('_', '\\_')
    myfile.write(item + "\n")
myfile.write("\\enddata\n")
myfile.write("\\label{tab:align-stats}\n")
myfile.write("\\end{deluxetable*}\n")
myfile.close()
