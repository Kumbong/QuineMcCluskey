from unittest import TestCase, main
from core.qm.petrick import *

class TestPetrick(TestCase):
    def setup(self):
        pass

#def test_multiply(self):
    #     self.fail()

    # def test_remove_dups(self):
    #     self.fail()

    # def test_multiply_all(self):
    #     self.fail()

    # def test_reduce_expr(self):
    #     self.fail()

    def test_min_len_terms(self):
        x = ['abcd','abc','abcde','a','b']
        self.assertEqual(min_len_terms(x),['a','b'])

        
        self.assertEqual(min_len_terms(['a']),['a'])

    def test_count_literals(self):
        self.assertEqual(count_literals('____'),0)
        self.assertEqual(count_literals('abcd'),4)
        self.assertEqual(count_literals('ab__'),2)   

    def test_fewest_literals(self):
        self.assertEqual(fewest_literals(['abcd','ab__','__cd']),['ab__','__cd'])
        self.assertEqual(fewest_literals(['a_b_','ab__','__cd']),['a_b_','ab__','__cd'])