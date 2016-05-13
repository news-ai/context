# -*- coding: utf-8 -*-
# Stdlib imports
import re


def split_uppercase(word):
    word = re.findall('[A-Z][^A-Z]*', word)
    return ' '.join(word)
