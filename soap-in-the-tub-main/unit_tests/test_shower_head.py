"""
Unit tests for the shower_head module
"""

import numpy as np
import shower_head
import unittest


class TestShowerHead(unittest.TestCase):

    def test_generate_droplet(self):
        """
        Test the ShowerHead class.
        :return:
        """
        shower = shower_head.ShowerHead()
        image = np.zeros((100, 100))
        shower.generate_droplet(image, 10)
        assert len(shower.droplets) == 10

    def test_update_droplets(self):
        shower = shower_head.ShowerHead()
        image = np.zeros((100, 100))
        shower.generate_droplet(image, 10)
        old_shower = shower.droplets
        shower.update_droplets(image)
        assert old_shower != shower.droplets

    def test_remove_droplets(self):
        shower = shower_head.ShowerHead()
        image = np.zeros((100, 100))
        shower.generate_droplet(image, 10)
        shower.remove_droplets(shower.droplets)
        assert len(shower.droplets) == 0
