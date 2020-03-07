#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from .somarabs import RomansToArabs

class RomansToArabs_Tests(unittest.TestCase):
    def test__romanToArab__I(self):
        sa = RomansToArabs()

        result = sa.romansToArabs("I")

        self.assertEqual(result, 1)

    def test__romanToArab__II(self):
            sa = RomansToArabs()

            result = sa.romansToArabs("II")

            self.assertEqual(result, 2)

    def test__romanToArab__III(self):
            sa = RomansToArabs()

            result = sa.romansToArabs("III")

            self.assertEqual(result, 3)

    def test__helloWorld__OK(self):
        sa = RomansToArabs()

        result = sa.helloWorld()

        self.assertEqual(result, "Hola Món!")
