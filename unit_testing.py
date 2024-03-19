from product_class import product

import unittest

class TestProduct(unittest.TestCase):
    def test_product(self):
        p = product("apple", 10, 5)
        total = p.calcuateTotal()
        self.assertEqual(total, 50)
        
    def test_calculateTotal_zero_quantity(self):
        p = product("apple", 10, 0)
        total = p.calcuateTotal()
        self.assertEqual(total, 0)
    
    def test_calculateTotal_negative_quantity(self):
        p = product("apple", 10, -1)
        with self.assertRaises(ValueError):
            total = p.calcuateTotal()
            

if __name__ == '__main__':
    unittest.main()