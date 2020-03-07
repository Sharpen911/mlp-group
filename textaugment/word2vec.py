# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:10:32 2020

@author: Lynn
"""

import gensim
from textaugment import Wordnet
import numpy as np
import nltk
from textaugment import Word2vec

vec2model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

vec_aug =  Word2vec(model=vec2model)

with open("textaugment\clickbait.txt", 'r', encoding='utf-8' ) as vec_org:
    with open("word2vec_clickbait.txt","w",encoding='utf-8') as vec:
        lines = vec_org.readlines()
        vec.write('startinput')
        for line in lines:
            print(line)
            new = vec_aug.augment(line)
            print(new)
            vec.write(new+'\n')
