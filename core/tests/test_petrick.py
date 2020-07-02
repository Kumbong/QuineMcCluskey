from unittest import TestCase, main
from core.qm.petrick import multiply,min_len_terms, count_literals, fewest_literals

class TestPetrick(TestCase):
    def setup(self):
        pass

def test_multiply(self):
    #test case with two empty expressions
    self.assertEqual(multiply('',''),'')
   

    # def test_remove_dups(self):
    #     self.fail()

    # def test_multiply_all(self):
    #     self.fail()

    # def test_reduce_expr(self):
    #     self.fail()

def test_min_len_terms(self):
    #check if the shortest minterm is actually the one being selected
    x = ['abcd','abc','abcde','a','b']
    self.assertEqual(min_len_terms(x),['a','b'])

    #edge case for situation where there is only a single minterm
    self.assertEqual(min_len_terms(['a']),['a'])

def test_count_literals(self):
    #check if the number of literals in an expression is counted correctly
    
    #the case where there is no literal
    self.assertEqual(count_literals('____'),0)

    #the case where the expression has all literals and no dashes
    self.assertEqual(count_literals('abcd'),4)

    #the case where there are some literals and some dashes
    self.assertEqual(count_literals('ab__'),2)   

def test_fewest_literals(self):
    #find the expressions with the lowest number of literals

    #case where there are some expressions that have the lowest number of literals
    self.assertEqual(fewest_literals(['abcd','ab__','__cd']),['ab__','__cd'])

    #the case where there is no particular expression with the lowest number of literals
    self.assertEqual(fewest_literals(['a_b_','ab__','__cd']),['a_b_','ab__','__cd'])