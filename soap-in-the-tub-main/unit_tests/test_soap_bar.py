"""
Unit tests for the soap_bar module
"""

import numpy as np
import soap_bar
import unittest
import shower_head


class TestSoapBar(unittest.TestCase):
    def test_load_soap(self):
        """
        Test the load soap method.
        """
        soap = soap_bar.SoapBar()
        assert isinstance(soap.soap, np.ndarray)


    def test_size(self):
        """
        Test the size method.
        """
        soap = soap_bar.SoapBar()
        assert soap.size() > 0

    def test_percentage_remaining(self):
        """
        Test the percentage remaining method.
        """
        soap = soap_bar.SoapBar()
        assert soap.percentage_remaining() == 100

    def test_erode(self):
        """
        Test the erode method.
        """
        droplet = shower_head.Droplets(50, 50, 10)
        soap = soap_bar.SoapBar()
        soap.erode([droplet])
        assert soap.soap[50, 50] == 255

