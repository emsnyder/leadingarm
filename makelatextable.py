import pickle
import numpy as np

ROOTDIR = '/Users/efrazer/leadingarm/sightlines/'
PICKLEFILE = '/Users/efrazer/leadingarm/fitdict.pickle'

with open(PICKLEFILE, 'rb') as handle:
    fitdict = pickle.load(handle)

biglist = [' ']


for sightline in fitdict:

    for ion in ['CII', 'CIV', 'SiII', 'SiIII', 'SiIV', 'OI', 'SII']:

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

                row.append(fitdict[sightline][ion]['direction'][0])

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

            row.append('$' + '{:10.6f}'.format(iondict['redshift'][n]).strip() + '\pm' + '{:10.6f}'.format(iondict['redshift error'][n]).strip() + '$')

            row.append('$' + str(iondict['b value'][n]) + '\pm' + str(iondict['b value error'][n]) + '$')

            row.append('$' + str(iondict['column density'][n]) + '\pm' + str(iondict['column density error'][n]) + '$')

            biglist.append(' & '.join(row) + '\\\ ')

for item in biglist:
    if '_' in item:
        item.replace('_', '\_')
    print(item)
