import unittest
import math_operations  # Import the module with your code

class TestMathOperations(unittest.TestCase):
    def test_square_positive(self):
        """Test square function with a positive number"""
        result = math_operations.square(4)
        self.assertEqual(result, 16)  # Check if 4 * 4 = 16

    def test_square_negative(self):
        """Test square function with a negative number"""
        result = math_operations.square(-3)
        self.assertEqual(result, 9)  # Check if -3 * -3 = 9

    def test_square_zero(self):
        """Test square function with zero"""
        result = math_operations.square(0)
        self.assertEqual(result, 0)  # Check if 0 * 0 = 0

if __name__ == '__main__':
    unittest.main()