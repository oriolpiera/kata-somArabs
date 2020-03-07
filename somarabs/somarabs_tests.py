#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from .somarabs import RomansToArabs

class RomansToArabs_Tests(unittest.TestCase):
    def test__romanToArab__I(self):
        sa = RomansToArabs()

        result = sa.romansToArabs("I")

        self.assertEqual(result, 1)

    def test__helloWorld__OK(self):
        sa = RomansToArabs()

        result = sa.helloWorld()

        self.assertEqual(result, "Hola Món!")
