#! /usr/bin/env python
# -*- coding: utf-8 -*-
class RomansToArabs(object):
    """
    Classe per convertir nombres romans a nombres arabs
    """
    def romansToArabs(self, number):
        value = 0
        for letter in number:
            if letter == "I":
                value = value + 1

        return value

    def helloWorld(self):
        """Funció que retorna el típic hello world

        Arguments:
            cap

        Returns:
            [string] -- frase "Hola Món"
        """
        return "Hola Món!"
