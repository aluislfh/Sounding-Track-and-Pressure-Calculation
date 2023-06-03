#!/usr/bin/env python
#-*- coding: utf-8 -*-
# encoding: utf-8
from __future__ import unicode_literals

import matplotlib
# matplotlib.use('agg')

import numpy as np
import glob
import os, sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PolyCollection
import shapefile as shp
import matplotlib as mpl

def main():


    for ff in sorted(glob.glob('*.fil')):
 
        stnlon = -77.847143
        stnlat = 21.423636
        
        data = np.loadtxt(ff, delimiter=',', skiprows=1)

        # lnmin,lnmax,lamin,lamax = (-78.86029518082424,-76.31110854746204,20.038998349472248,22.137192713553127)
        lnmin,lnmax,lamin,lamax = (np.min(np.degrees(data[:,3])),np.max(np.degrees(data[:,3])),np.min(np.degrees(data[:,2])),np.max(np.degrees(data[:,2])))
        
        map = Basemap(resolution='h',llcrnrlon=lnmin,llcrnrlat=lamin,urcrnrlon=lnmax,urcrnrlat=lamax)

        # plot3d(data, map, stnlon, stnlat, ff)
        plot3d_bmap(data, map, stnlon, stnlat, ff, lnmin, lnmax, lamin, lamax)


# def plot3d(data,map,stnlon,stnlat,f):

#     xlons = np.degrees(data[:,3])# + stnlon
#     xlats = np.degrees(data[:,2])# + stnlat

#     fig = plt.figure()
#     ax = fig.gca(projection='3d')

#     ax.plot(xlons, xlats, data[:,1], marker=None,color='r',linewidth=0.8)

#     plt.show()


def plot3d_bmap(data,map,stnlon,stnlat,f,lnmin,lnmax,lamin,lamax):

    xlons = np.degrees(data[:,3])# + stnlon
    xlats = np.degrees(data[:,2])# + stnlat

    xmin,xmax,ymin,ymax = (np.min(xlons),np.max(xlons),np.min(xlats),np.max(xlats))

    mpl.rcParams['legend.fontsize'] = 6
    fig = plt.figure(1,figsize=(12.0, 9.0),dpi=300)

    ax = fig.gca(projection='3d')

    ax.set_xlim3d(lnmin,lnmax)
    ax.set_ylim3d(lamin,lamax)
    ax.set_zlim3d(0, 26000)

#    ax.set_xticklabels(fontsize=6)
#    ax.set_yticklabels(fontsize=6)
#    ax.set_xticklabels()

    sf = shp.Reader('shp/gis_osm_roads_free_1')
    
    for shape in sf.shapeRecords():
        for i in range(len(shape.shape.parts)):
            i_start = shape.shape.parts[i]
            if i==len(shape.shape.parts)-1:
                i_end = len(shape.shape.points)
            else:
                i_end = shape.shape.parts[i+1]

            lons = []
            for i in shape.shape.points[i_start:i_end]:
                
#                if float(i[0]) >= xmin and float(i[0]) <= xmax and float(i[1]) >= ymin and float(i[1]) <= ymax:
                if float(i[0]) >= lnmin and float(i[0]) <= lnmax and float(i[1]) >= lamin and float(i[1]) <= lamax:
                    lons.append(i[0])

            lats = []
            for i in shape.shape.points[i_start:i_end]:
#                if float(i[0]) >= xmin and float(i[0]) <= xmax and float(i[1]) >= ymin and float(i[1]) <= ymax:
                if float(i[0]) >= lnmin and float(i[0]) <= lnmax and float(i[1]) >= lamin and float(i[1]) <= lamax:
                    lats.append(i[1])

            ax.plot(lons, lats, np.zeros(shape=(len(lons))), marker=None,color='grey',linewidth=0.1)



    sf = shp.Reader('shp/gis_osm_waterways_free_1')
    
    for shape in sf.shapeRecords():
        for i in range(len(shape.shape.parts)):
            i_start = shape.shape.parts[i]
            if i==len(shape.shape.parts)-1:
                i_end = len(shape.shape.points)
            else:
                i_end = shape.shape.parts[i+1]

            lons = []
            for i in shape.shape.points[i_start:i_end]:
                
#                if float(i[0]) >= xmin and float(i[0]) <= xmax and float(i[1]) >= ymin and float(i[1]) <= ymax:
                if float(i[0]) >= lnmin and float(i[0]) <= lnmax and float(i[1]) >= lamin and float(i[1]) <= lamax:
                    lons.append(i[0])

            lats = []
            for i in shape.shape.points[i_start:i_end]:
#                if float(i[0]) >= xmin and float(i[0]) <= xmax and float(i[1]) >= ymin and float(i[1]) <= ymax:
                if float(i[0]) >= lnmin and float(i[0]) <= lnmax and float(i[1]) >= lamin and float(i[1]) <= lamax:
                    lats.append(i[1])

            ax.plot(lons, lats, np.zeros(shape=(len(lons))), marker=None,color='b',linewidth=0.1)



    sf = shp.Reader('shp/reproj_muni')
    
    for shape in sf.shapeRecords():
        for i in range(len(shape.shape.parts)):
            i_start = shape.shape.parts[i]
            if i==len(shape.shape.parts)-1:
                i_end = len(shape.shape.points)
            else:
                i_end = shape.shape.parts[i+1]

            lons = []
            for i in shape.shape.points[i_start:i_end]:
                
#                if float(i[0]) >= xmin and float(i[0]) <= xmax and float(i[1]) >= ymin and float(i[1]) <= ymax:
                if float(i[0]) >= lnmin and float(i[0]) <= lnmax and float(i[1]) >= lamin and float(i[1]) <= lamax:
                    lons.append(i[0])

            lats = []
            for i in shape.shape.points[i_start:i_end]:
#                if float(i[0]) >= xmin and float(i[0]) <= xmax and float(i[1]) >= ymin and float(i[1]) <= ymax:
                if float(i[0]) >= lnmin and float(i[0]) <= lnmax and float(i[1]) >= lamin and float(i[1]) <= lamax:
                    lats.append(i[1])

            ax.plot(lons, lats, np.zeros(shape=(len(lons))), marker=None,color='k',linewidth=0.3)



    sf = shp.Reader('shp/reproj_prov')
    
    for shape in sf.shapeRecords():
        for i in range(len(shape.shape.parts)):
            i_start = shape.shape.parts[i]
            if i==len(shape.shape.parts)-1:
                i_end = len(shape.shape.points)
            else:
                i_end = shape.shape.parts[i+1]

            lons = []
            for i in shape.shape.points[i_start:i_end]:
                
#                if float(i[0]) >= xmin and float(i[0]) <= xmax and float(i[1]) >= ymin and float(i[1]) <= ymax:
                if float(i[0]) >= lnmin and float(i[0]) <= lnmax and float(i[1]) >= lamin and float(i[1]) <= lamax:
                    lons.append(i[0])

            lats = []
            for i in shape.shape.points[i_start:i_end]:
#                if float(i[0]) >= xmin and float(i[0]) <= xmax and float(i[1]) >= ymin and float(i[1]) <= ymax:
                if float(i[0]) >= lnmin and float(i[0]) <= lnmax and float(i[1]) >= lamin and float(i[1]) <= lamax:
                    lats.append(i[1])

            ax.plot(lons, lats, np.zeros(shape=(len(lons))), marker=None,color='k',linewidth=0.5)

#    plt.xlim(xmin,xmax)
#    plt.ylim(ymin,ymax)

    ax.plot(xlons, xlats, data[:,1], marker=None,color='r',linewidth=0.8,label='Sounding trajectory')
    ax.legend()


    plt.savefig('plot3d_track_'+f[:-4]+'.png', dpi=300, pad_inches=0,bbox_inches='tight')
    plt.clf()
    plt.cla()
    plt.close('all')

    return


main()















