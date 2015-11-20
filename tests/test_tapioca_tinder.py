# coding: utf-8

import unittest

from tapioca_tinder import Tinder


class TestTapiocaTinder(unittest.TestCase):

    def setUp(self):
        self.wrapper = Tinder()


if __name__ == '__main__':
    unittest.main()
