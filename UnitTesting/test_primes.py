import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5), msg="5 is prime")

    def test_is_four_not_prime(self):
        """Is four successfully determined to be not prime?"""
        self.assertFalse(is_prime(4), msg="4 is not prime")

    def test_is_zero_not_prime(self):
        """Is zero successfully determined to be not prime?"""
        self.assertFalse(is_prime(0), msg="0 is not prime")

    def test_is_one_not_prime(self):
        """Is one successfully determined to be not prime?"""
        self.assertFalse(is_prime(1), msg="1 is not prime")

    def test_is_prime(self):
        """Is one successfully determined to be not prime?"""
        self.assertFalse(is_prime(-1), msg="-10 is not prime")

if __name__ == '__main__':
    unittest.main()
