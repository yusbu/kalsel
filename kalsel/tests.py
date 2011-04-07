import unittest
import os
from geonode.maps.utils import upload

DATA_DIR = os.path.join(os.getcwd(), 'data') 

class KalSelTestCase(unittest.TestCase):
    def testUpload(self):
        msg = ('%s is not a directory' % DATA_DIR)
        assert os.path.isdir(DATA_DIR), msg

        ricefields = os.path.join(DATA_DIR, 'arahan_edited.shp')
        
        msg = ('%s is not a file' % ricefields)
        assert os.path.isfile(ricefields), msg

        boundary = os.path.join(DATA_DIR, 'adm_kab.shp')
        
        msg = ('%s is not a file' % ricefields)
        assert os.path.isfile(ricefields), msg

        rice  = upload(ricefields)
        adm = upload(boundary)

        print rice
        print adm

        assert rice is not None
        assert adm is not None
