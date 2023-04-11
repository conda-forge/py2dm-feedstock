#!/usr/bin/env python3

import unittest

class Py2DMTestCase(unittest.TestCase):
    def test_cimport(self):
        """Test import and CPython implementation available"""
        import py2dm
        self.assertEqual('c', py2dm.implementation)

if __name__ == '__main__':
    unittest.main()
