from unittest import TestCase, main
from core.qm.qm import QM

class TestQM(TestCase):
    def setup(self):
        pass

    def test_convert_binary(self):
        
        #test if the strings are the actual binary representations
        #for each of the strings
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        conversion = qm.to_binary(minterms)
        expected_conversion = ['0001','0010','0011','0100','0101','0110','1111']
        self.assertEqual(conversion,expected_conversion)
        

    def test_length_convert_to_binary(self):
        #check if the number of bits in each binary string is the same for 
        #all
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        conversion = qm.to_binary(minterms)
        for term in conversion:
            self.assertEqual(len(term),4)

        #check if the same applies to the don't cares

    def test_combine_single_values(self):
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

    def test_combine_length(self):
        #test for values that differ in length 
        #valueerror exception should be thrown
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
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

        #edge test cases 
        self.assertEqual(qm.combine_groups([],['0001','1000']),[])
        self.assertEqual(qm.combine_groups([],[]),[])
        
    def test_combine_generation_no_dash(self):
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertEqual(qm.combine_generation([['0000'],['0001','1000'],['0011','1001','1100'],['0111','1011'],['1111']]),
        [['000_','_000'],['00_1','_001','100_','1_00'],['0_11','_011','10_1'],['_111','1_11']])

        #expected pass test case

    def test_combine_generation_dash(self):
        #test the combine generation with a generation that has dashes
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertEqual(qm.combine_generation([['000_','_000'],['00_1','_001','100_','1_00'],['0_11','_011','10_1'],['_111','1_11']]),
        [['_00_'],['_0_1'],['__11']])


    def test_combine_generation_no_new_generation(self):
        #test the combine generation with a generation that does not result in offspring
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertEqual(qm.combine_generation([['_00_'],['_0_1'],['__11']]),[])


    def test_combine_generation_empty_generation(self):
        #test the combine generation with an empty generation
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertEqual(qm.combine_generation([]),[])


    def test_combine_generation_wrong(self):
        #test the combine generation with an empty generation
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertNotEqual(qm.combine_generation([['_00_'],['_0_1'],['__11']]),[['____']])

    def test_group_minterms(self):
        #test the combine generation with an empty generation
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertEqual(qm.group_minterms(['0000','0001','0010','0100','0011','0101','1111']),[['0000'],['0001','0010','0100'],['0011','0101'],['1111']])

    def test_pis(self):
        #test the combine generation with an empty generation
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        #expected pass test case

        self.assertEqual(qm.pis(),['1111','00_1','0_01','001_','0_10','010_','01_0'])

    def test_can_cover(self):
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertTrue(qm.can_cover('_00_','0000'))
        self.assertTrue(qm.can_cover('_00_','1001'))
        self.assertFalse(qm.can_cover('_11_','0000'))
        self.assertFalse(qm.can_cover('_00_','0110'))

        
    
    def test_primary_epis(self):
        minterms = [1,2,3,4,5,6,9,11,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertEqual(qm.primary_epis(),[])
 

    def test_other_pis(self):
        minterms = [1,2,3,4,5,6,9,11,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertEqual(qm.secondary_epis(),[])


    def test_combine(self):
        minterms = [1,2,3,4,5,6,15]
        qm =  QM(minterms)
        x = qm.minimize()
        y = []
        for t in x:
            y+= t.split('+')
        
        y = [t.strip() for t in y]
        
        self.assertEqual(sorted(y),sorted(['1111', '0_10','00_1', '010_', '1111', '0_01',  '001_' , '01_0']))

    def test_to_char(self):
        minterms = [1,2,3,4,5,6,9,11,15]
        qm =  QM(minterms)
        #expected pass test case
        self.assertEqual(qm.to_char('_00_',['a','b','c','d']),"b'c'")
        self.assertEqual(qm.to_char('_11_',['a','b','c','d']),"bc")
        self.assertEqual(qm.to_char('____',['a','b','c','d']),"")
        self.assertEqual(qm.to_char('0000',['a','b','c','d']),"a'b'c'd'")
        self.assertEqual(qm.to_char('1111',['a','b','c','d']),"abcd")
        