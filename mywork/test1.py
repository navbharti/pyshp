'''
Created on Sep 18, 2014

@author: rajni
'''
import shapefile
import os

cd=os.path.abspath(os.curdir)
print cd
sf = shapefile.Reader("C:\\py\\pyshp\\shapefiles\\blockgroups.shp")
shapes = sf.shapes()
#print shapes
print len(shapes)
print len(list(sf.iterShapes()))

for name in dir(shapes[3]):
    if not name.startswith('__'):
        name
print shapes[3].shapeType