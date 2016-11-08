__author__ = 'Alex'
#-*- coding: cp866 -*-
import time
import os
from subprocess import call
import subprocess
import sys
import glob

target_dir = 'D:\PycharmProjects\srp_lab4'
rar_name = 'LC81810252015144LGN00.tar'
path = target_dir + rar_name
os.chdir(target_dir)
#call("f.bat")
# images = glob.glob('C:/workspace/lab/*.tif')
# for image in images:
# command.append(image)
images = 'c:/workspace/lab/LC81810252015144LGN00/LC81810252015144LGN00_B10.tif c:/workspace/lab/LC81810252015144LGN00/LC81810252015144LGN00_B11.tif c:/workspace/lab/LC81810252015144LGN00/LC81810252015144LGN00_B7.tif c:/workspace/lab/LC81810252015144LGN00/LC81810252015144LGN00_B5.tif c:/workspace/lab/LC81810252015144LGN00/LC81810252015144LGN00_B6.tif'
command = 'python gdal_merge.py -o C:\workspace\lab\mer5.tif -separate '
os.chdir('C:\Program Files (x86)\GDAL')
#os.system(command+images)

print ('###################################')
print ('gdalwarp')
command_1 = "gdalwarp -t_srs \"+proj=utm +zone=36\" c:\workspace\lab\mer5.tif c:\workspace\lab\gdalwarp.tif"
#os.system(command_1)

print ('###################################')
print ('gdalwarp_cut')
command_2 = 'gdalwarp -q -cutline c:/workspace/lab/LC81810252015144LGN00/newshape.shp -crop_to_cutline -of GTiff c:/workspace/lab/mer5.tif c:\workspace\lab\gdal_cut.tif'
os.system(command_2)

print ('###################################')
print ('gdalwarp_cut with x,y')
command_3 = 'gdalwarp -tr 30 -30 -te 5 255 122 348 c:/workspace/lab/LC81810252015144LGN00/LC81810252015144LGN00_B7.tif c:/workspace/lab/outputEND.tif '
#os.system(command_3)

print ('###################################')
print ('gdalwarp concatenate')
command_4 = 'gdalwarp ?of GTIFF ?ot Uint16 ?srcnodata ?dstnodata c:/workspace/lab/LC81810252015144LGN00/LC81810252015144LGN00_B11.tif c:/workspace/lab/LC81810252015144LGN00/LC81810252015144LGN00_B7.tif c:/workspace/lab/concatenate_data.tif'
#os.system(command_4)