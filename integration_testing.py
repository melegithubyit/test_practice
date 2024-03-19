import unittest

from shoppingCart import ShoppingCart

from product_class import product

class TestShoppingcart(unittest.TestCase):
    
    def test_shoppingcartTotal_empty_cart(self):
        cart = ShoppingCart()
        total = cart.calculateTotal()
        self.assertEqual(total, 0)
        
    
    def test_getCartTotal_with_products(self):
        cart = ShoppingCart()
        cart.addProduct(product("apple", 10, 5))
        cart.addProduct(product("banana", 20, 5))
        total = cart.calculateTotal()
        self.assertEqual(total, 150)



if __name__ == '__main__':
    unittest.main()

