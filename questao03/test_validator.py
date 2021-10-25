import unittest
import validator

class TestValidator(unittest.TestCase):
  
    def test_cdvpy_valido(self):        
        self.assertTrue(validator.valida_cdvpy(123456))
    
    def test_cdvpy_invalido(self):        
        self.assertFalse(validator.valida_cdvpy(552523))
    
    def test_cdvpy_len(self):        
        self.assertFalse(validator.valida_cdvpy(1234567))
    
    def test_cdvpy_alternado(self):        
        self.assertFalse(validator.valida_cdvpy('1A2B3C'))
  
if __name__ == '__main__':
    unittest.main()