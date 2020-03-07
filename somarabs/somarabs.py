#! /usr/bin/env python
# -*- coding: utf-8 -*-
class RomansToArabs(object):
    """
    Classe per convertir nombres romans a nombres arabs
    """
    def romansToArabs(self, number):
        value = 0
        previous = ""
        for letter in number:
            if letter == "V":
                if previous == "I":
                    value = value - 2
                value = value + 5
            if letter == "I":
                value = value + 1
            if letter == "X":
                value = value + 10
            previous = letter

        return value

    def helloWorld(self):
        """Funció que retorna el típic hello world

        Arguments:
            cap

        Returns:
            [string] -- frase "Hola Món"
        """
        return "Hola Món!"
