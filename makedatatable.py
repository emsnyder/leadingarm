from astropy.table import Table, Column
from astropy import units as u
import numpy as np
import os

datatable = Table()

datatable['target'] = Column([],
                             unit=u.dimensionless_unscaled,
                             description='target name',
                             dtype='S30')
datatable['region'] = Column([],
                             unit=u.dimensionless_unscaled,
                             description='Region probed by target [Stream (MS), Bridge, Leading Arm (LA), LMC '
                                         'Halo, or CHVC]. On/Off refer to directions with/without Magellanic Hi '
                                         '21cm emission',
                             dtype='S30')
datatable['l'] = Column([],
                        unit='degree',
                        description='Galatcic latitude',
                        dtype=np.float64)
datatable['b'] = Column([],
                        unit='degree',
                        description='Galactic longitude',
                        dtype=np.float64)
datatable['LMS'] = Column([],
                          unit='degree',
                          description='Magellanic latitude',
                          dtype=np.float64)
datatable['BMS'] = Column([],
                          unit='degree',
                          description='Magellanic longitude',
                          dtype=np.float64)
datatable['PID'] = Column([],
                          unit=u.dimensionless_unscaled,
                          description='HST program ID of dataset',
                          dtype=np.int)
datatable['vmin'] = Column([],
                           unit='km s^-1',
                           description='Minimum LSR velocity of Magellanic absorption',
                           dtype=np.int)
datatable['vmax'] = Column([],
                           unit='km s^-1',
                           description='Maximum LSR velocity of Magellanic absorption',
                           dtype=np.int)
datatable['vms'] = Column([],
                          unit='km s^-1',
                          description='central Magellanic LSR velocity',
                          dtype=np.int)
datatable['logN(HI)'] = Column([],
                               unit='cm^-2',
                               description='HI column density',
                               dtype=np.float64)
datatable['logN(HI)_lim'] = Column([],
                                   unit=u.dimensionless_unscaled,
                                   description='quantifies whether quantity is upper limit (1), lower limit '
                                               '(-1), or neither (0)',
                                   dtype=np.int)
datatable['logN(SiII)'] = Column([],
                                 unit='cm^-2',
                                 description='column density of SiII',
                                 dtype=np.float64)
datatable['logN(SiII)_lim'] = Column([],
                                     unit=u.dimensionless_unscaled,
                                     description='quantifies whether quantity is upper limit (1), lower limit '
                                                 '(-1), or neither (0)',
                                     dtype=np.int)
datatable['logN(SiII)_err'] = Column([],
                                     unit='cm^-2',
                                     description='error on measurement',
                                     dtype=np.float64)
datatable['logN(SiIII)'] = Column([],
                                  unit='cm^-2',
                                  description='column density of SiIII',
                                  dtype=np.float64)
datatable['logN(SiIII)_lim'] = Column([],
                                      unit=u.dimensionless_unscaled,
                                      description='quantifies whether quantity is upper limit (1), lower limit'
                                                  ' (-1), or neither (0)',
                                      dtype=np.int)
datatable['logN(SiIII)_err'] = Column([],
                                      unit='cm^-2',
                                      description='error on measurement',
                                      dtype=np.float64)
datatable['logN(SiIV)'] = Column([],
                                 unit='cm^-2',
                                 description='column density of SiIV',
                                 dtype=np.float64)
datatable['logN(SiIV)_lim'] = Column([],
                                     unit=u.dimensionless_unscaled,
                                     description='quantifies whether quantity is upper limit (1), lower limit '
                                                 '(-1), or neither (0)',
                                     dtype=np.int)
datatable['logN(SiIV)_err'] = Column([],
                                     unit='cm^-2',
                                     description='error on measurement',
                                     dtype=np.float64)
datatable['logN(CII)'] = Column([],
                                unit='cm^-2',
                                description='column density of CII',
                                dtype=np.float64)
datatable['logN(CII)_lim'] = Column([],
                                    unit=u.dimensionless_unscaled,
                                    description='quantifies whether quantity is upper limit (1), lower limit (-1),'
                                                ' or neither (0)',
                                    dtype=np.int)
datatable['logN(CII)_err'] = Column([],
                                    unit='cm^-2',
                                    description='error on measurement',
                                    dtype=np.float64)
datatable['logN(CIV)'] = Column([],
                                unit='cm^-2',
                                description='column density of CIV',
                                dtype=np.float64)
datatable['logN(CIV)_lim'] = Column([],
                                    unit=u.dimensionless_unscaled,
                                    description='quantifies whether quantity is upper limit (1), lower limit '
                                                '(-1), or neither (0)',
                                    dtype=np.int)
datatable['logN(CIV)_err'] = Column([],
                                    unit='cm^-2',
                                    description='error on measurement',
                                    dtype=np.float64)
datatable['log(SiIII/SiII)'] = Column([],
                                      unit=u.dimensionless_unscaled,
                                      description='ratio of SiIII to SiII column densities',
                                      dtype=np.float64)
datatable['log(SiIII/SiII)_lim'] = Column([],
                                          unit=u.dimensionless_unscaled,
                                          description='quantifies whether quantity is upper limit (1), lower '
                                                      'limit (-1), or neither (0)',
                                          dtype=np.int)
datatable['log(SiIII/SiII)_err'] = Column([],
                                          unit=u.dimensionless_unscaled,
                                          description='error on measurement',
                                          dtype=np.float64)
datatable['log(SiIV/SiII)'] = Column([],
                                     unit=u.dimensionless_unscaled,
                                     description='ratio of SiIV to SiII column densities',
                                     dtype=np.float64)
datatable['log(SiIV/SiII)_lim'] = Column([],
                                         unit=u.dimensionless_unscaled,
                                         description='quantifies whether quantity is upper limit (1), lower limit'
                                                     ' (-1), or neither (0)',
                                         dtype=np.int)
datatable['log(SiIV/SiII)_err'] = Column([],
                                         unit=u.dimensionless_unscaled,
                                         description='error on measurement',
                                         dtype=np.float64)
datatable['log(CIV/CII)'] = Column([],
                                   unit=u.dimensionless_unscaled,
                                   description='ratio of CIV to CII column densities',
                                   dtype=np.float64)
datatable['log(CIV/CII)_lim'] = Column([],
                                       unit=u.dimensionless_unscaled,
                                       description='quantifies whether quantity is upper limit (1), '
                                                   'lower limit (-1), or neither (0)',
                                       dtype=np.int)
datatable['log(CIV/CII)_err'] = Column([],
                                       unit=u.dimensionless_unscaled,
                                       description='error on measurement',
                                       dtype=np.float64)
datatable['logN(OI)'] = Column([],
                                unit='cm^-2',
                                description='column density of OI',
                                dtype=np.float64)
datatable['logN(OI)_lim'] = Column([],
                                    unit=u.dimensionless_unscaled,
                                    description='quantifies whether quantity is upper limit (1), lower limit '
                                                '(-1), or neither (0)',
                                    dtype=np.int)
datatable['logN(OI)_err'] = Column([],
                                    unit='cm^-2',
                                    description='error on measurement',
                                    dtype=np.float64)


def checklims(input_str):
    if input_str[0] == '<':
        lim = 1
        val = input_str[1:]
    elif input_str[0] == '>':
        lim = -1
        val = input_str[1:]
    else:
        lim = 0
        val = input_str
    return val, lim


rootdir = '/Users/efrazer/leadingarm/'
f = open(os.path.join(rootdir, 'origdatafile.txt'), 'r')
f.readline()
for line in f.readlines():
    myline = line.strip()
    sline = myline.split()
    target = sline[0]
    region = sline[1]
    SiII = sline[2]
    SiII_err = sline[3]
    SiIII = sline[4]
    SiIII_err = sline[5]
    SiIV = sline[6]
    SiIV_err = sline[7]
    CII = sline[8]
    CII_err = sline[9]
    CIV = sline[10]
    CIV_err = sline[11]
    SiIIISiII = sline[12]
    SiIIISiII_err = sline[13]
    SiIVSiII = sline[14]
    SiIVSiII_err = sline[15]
    CIVCII = sline[16]
    CIVCII_err = sline[17]
    l = sline[18]
    b = sline[19]
    LMS = sline[20]
    BMS = sline[21]
    PID = sline[22]
    vmin = sline[23]
    vmax = sline[24]
    vms = sline[25]
    HI = sline[26]
    OI = sline[27]
    OI_err = sline[28]
    newHI, HI_lim = checklims(HI)
    newSiII, SiII_lim = checklims(SiII)
    newSiIII, SiIII_lim = checklims(SiIII)
    newSiIV, SiIV_lim = checklims(SiIV)
    newCII, CII_lim = checklims(CII)
    newCIV, CIV_lim = checklims(CIV)
    newSiIIISiII, SiIIISiII_lim = checklims(SiIIISiII)
    newSiIVSiII, SiIVSiII_lim = checklims(SiIVSiII)
    newCIVCII, CIVCII_lim = checklims(CIVCII)
    newOI, OI_lim = checklims(OI)
    mylist = (target, region, float(l), float(b), float(LMS), float(BMS),
              int(PID), int(vmin), int(vmax), int(vms),
              float(newHI), HI_lim,
              float(newSiII), SiII_lim, float(SiII_err),
              float(newSiIII), SiIII_lim, float(SiIII_err),
              float(newSiIV), SiIV_lim, float(SiIV_err),
              float(newCII), CII_lim, float(CII_err),
              float(newCIV), CIV_lim, float(CIV_err),
              float(newSiIIISiII), SiIIISiII_lim, float(SiIIISiII_err),
              float(newSiIVSiII), SiIVSiII_lim, float(SiIVSiII_err),
              float(newCIVCII), CIVCII_lim, float(CIVCII_err),
              float(newOI), OI_lim, float(OI_err))
    datatable.add_row(mylist)

# datatable.write('newdatafile.hdf5', path='data', serialize_meta=True, overwrite=True)
datatable.write(os.path.join(rootdir, 'datafile1418.fits'), format='fits', overwrite=True)
