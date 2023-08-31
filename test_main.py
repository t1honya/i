from main import check1
from main import check2
from main import check3 
import unittest2 as ut

class testcase1(ut.TestCase):
    def test1(self):
        self.assertEqual(check1(),'OK','Menu')
    def test2(self):
        self.assertEqual(check3(),'OK','PLay_button')
    def test3(self):
        self.assertEqual(check2(),"OK",'Customise')
ut.main()