# test_shieldchain.py
"""
Tests for ShieldChain module.
"""

import unittest
from shieldchain import ShieldChain

class TestShieldChain(unittest.TestCase):
    """Test cases for ShieldChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShieldChain()
        self.assertIsInstance(instance, ShieldChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShieldChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
