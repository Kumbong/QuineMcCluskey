from unittest import TestCase, main
from core.qm.qm import QM

class TestQM(TestCase):
    def setup(self):
        self.fail()

    def test_to_binary(self):
        
        #test if the strings are the actual binary representations
        #for each of the strings
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        expected_conversion = ['0001','0010','0011','0100','0101','0110','1111']
        conversion = qm.to_binary(minterms)
        self.assertEqual(conversion,expected_conversion)
        
        #check if the number of bits in each binary string is the same for 
        #all
        for term in conversion:
            self.assertEqual(len(term),4)

        #check if the same applies to the don't cares

    def test_combine(self):
        self.fail()

    def test_combine_groups(self):
        self.fail()

    def test_combine_generation(self):
        self.fail()

    def test_group_minterms(self):
        self.fail()

    def test_pis(self):
        self.fail()

    def test_can_cover(self):
        self.fail()
    
    def test_epis(self):
        self.fail()

    def test_other_pis(self):
        self.fail()
