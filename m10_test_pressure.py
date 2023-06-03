#!/usr/bin/env python
#-*- coding: utf-8 -*-
# encoding: utf-8
from __future__ import unicode_literals

import matplotlib
matplotlib.use('agg')
import glob, os, sys
import numpy as np
import matplotlib.pyplot as plt


def main():

#    Example:
#      0     1         2          3        4         5       6    7      8      9       10      11     12    13    14      16       17         18        19
#    TempF,AltitudF,LatitudeF ,LongitudeF,VEstF  ,VNordF ,VVertF,VHorF ,VDirF,TaNCalF,TaCalF ,TaRadF ,UNCaF,UCalF,PressF,GPSAltF,AD_OzoneF ,T_OzoneF ,AD_AuxF 
#    43119,00122.00,+0.3739125,-1.3586929,-05.40,-01.52,+1.50,005.60,074.3,+25.17,+25.17,+25.17,086.8,086.8,1005.1,00122.24,0004,-82.33,0000
#    43120,00123.64,+0.3739122,-1.3586940,-06.33,-01.32,+1.98,006.46,078.2,+25.12,+25.12,+25.12,086.7,086.7,1004.9,00123.89,0004,-81.85,1431655765
#    43121,00125.06,+0.3739121,-1.3586950,-05.23,-00.54,+2.28,005.26,084.1,+25.09,+25.09,+25.09,086.7,086.7,1004.7,00125.31,0004,-82.14,-1717986918
#    43122,00126.63,+0.3739121,-1.3586958,-05.10,-00.52,+2.54,005.13,084.2,+25.04,+25.04,+25.04,086.7,086.7,1004.6,00126.88,0004,-82.13,613566757

#    https://www.tutiempo.net/meteorologia/ecuaciones.html

    for ff in sorted(glob.glob('*.fil')):

        stnlon = -77.847143
        stnlat = 21.423636


        data = np.loadtxt(ff, delimiter=',', skiprows=1)

        xlons = np.degrees(data[:,3])
        xlats = np.degrees(data[:,2])

        relhum = data[:,13]
        temps = data[:,10]
        altitud = data[:,1]
        press = data[:,14]
        altgps = data[:,16]

        # variante 1 (z - sfc)

        Po = 1015.0
        g = 9.80617
        R = 287.04
        Z = altitud
        tsfc = 22.0
        Tm = (temps[:] - tsfc)/2 + 273.15
        P1 = Po / np.exp(Z * g /( R * Tm))   


        # variante 2 (z1 - z0)

        Po = 1015.0
        g = 9.80617
        R = 287.04
        Z = altitud
        tsfc = 22.0

        P2 = []
        for zh in range(len(altitud)):

            if zh == 0:
                Tm = (temps[zh] - tsfc)/2 + 273.15
                Ptmp = Po / np.exp(Z[zh] * g /( R * Tm))
                P2.append(Ptmp)    
            else:
                Tm = (temps[zh] - temps[zh-1])/2 + 273.15
                Ptmp = Po / np.exp(Z[zh] * g /( R * Tm))
                P2.append(Ptmp)




        plt.figure(1, dpi=300)

        plt.plot(press, altitud,color='k',label='Presión Atmosférica del Sondeo Real')
        plt.plot(P1, altitud,color='r',label='Variante 1 / MAE = '+str(np.average(np.abs(P1-press))))
        plt.plot(P2, altitud,color='b',label='Variante 2 / MAE = '+str(np.average(np.abs(P2-press))))

        plt.title("Curva de altura vs presión")
        plt.ylabel("Altura (m)")
        plt.xlabel("Presión (hPa)")

        plt.grid(True)
        plt.legend()

        plt.savefig('variantes_'+ff+'.png', dpi=300, bbox_inches='tight', pad_inches=0)
        plt.close('all')


        plt.figure(2, dpi=300)

        plt.plot(press[:450], altitud[:450],color='k',label='Presión Atmosférica del Sondeo Real')
        plt.plot(P1[:450], altitud[:450],color='r',label='Variante 1 / MAE = '+str(np.average(np.abs(P1[:450]-press[:450]))))
        plt.plot(P2[:450], altitud[:450],color='b',label='Variante 2 / MAE = '+str(np.average(np.abs(P2[:450]-press[:450]))))

        plt.title("Curva de altura vs presión entre 0 - 1 km")
        plt.ylabel("Altura (m)")
        plt.xlabel("Presión (hPa)")

        plt.grid(True)
        plt.legend()

        plt.savefig('variantes_1km_'+ff+'.png', dpi=300, bbox_inches='tight', pad_inches=0)
        plt.close('all')



main()
























