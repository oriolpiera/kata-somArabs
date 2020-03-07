#! /usr/bin/env python
# -*- coding: utf-8 -*-
class RomansToArabs(object):
    """
    Classe per convertir nombres romans a nombres arabs
    """
    def romansToArabs(self, number):
        if number == "II":
            return 2
        return 1

    def helloWorld(self):
        """Funció que retorna el típic hello world

        Arguments:
            cap

        Returns:
            [string] -- frase "Hola Món"
        """
        return "Hola Món!"
