# -*- coding: utf-8 -*-
import unittest
import os
import ogr
from shapely.wkb import loads
from kalsel.models import calculate

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data') 

class KalSelTestCase(unittest.TestCase):
    def testUpload(self):
        msg = ('%s is not a directory' % DATA_DIR)
        assert os.path.isdir(DATA_DIR), msg
        ricefields = os.path.join(DATA_DIR, 'arahan_edited.shp')
        boundaries = os.path.join(DATA_DIR, 'adm_kab.shp')

        rice = ogr.Open(ricefields)
        adm = ogr.Open(boundaries)

        output = calculate(rice, adm)

        msg = ('The calculation returned %s'  % output)
        assert output is not None, msg

if __name__ == '__main__':
    suite = unittest.makeSuite(KalSelTestCase, 'test')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
