from unittest import TestCase, main
from core.qm.qm import QM

class TestQM(TestCase):
    def setup(self):
        pass

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
        #test for two terms that are not supposed to be combined
        #expected return value should be None
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)

        self.assertEqual(qm.combine('0000','1001'),None)
        #test for values(without _ ) that differ by exactly one position 
        #expected return value should have a new value with a _ in the positiion of difference

        self.assertEqual(qm.combine('0000','0001'),'000_')
        #test for values(without _ ) that differ by exactly one position 
        #expected return value should have a new value with a _ in the positiion of difference

        self.assertEqual(qm.combine('000_','100_'),'_00_')

        #test for values that differ in length 
        #valueerror exception should be thrown
        with self.assertRaises(ValueError):
            qm.combine('00000','0001'),ValueError

        #test for values that are the same 
        #None should be returned
        self.assertEqual(qm.combine('0000','0000'),None)


    def test_combine_groups(self):
        #test combination for some random groups
        
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        self.assertEqual(qm.combine_groups(['0001','1000'],['0011','1001','1100']),['00_1','_001','100_','1_00'])
        self.assertEqual(qm.combine_groups(['0000'],['0001','1000']),['000_','_000'])
        self.assertEqual(qm.combine_groups([],['0001','1000']),[])
        self.assertEqual(qm.combine_groups([],[]),[])
        
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
