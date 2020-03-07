import gensim
from textaugment import Wordnet
import numpy as np
import nltk
from textaugment import Wordnet
from textaugment import Word2vec

#Word2vec
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
word2vec_aug = Word2vec(model=model)
word2vec_aug.augment('The stories are good')#example

string = 'The stories are good'
print(type(string))
with open('originaldata\clickbait.txt', 'r') as vec_org:
    with open('augmentdata\word2vec_clickbait.txt','w') as vec:
        lines = vec_org.readlines()
        vec.write('startinput')
        for line in lines:
            print(type(line))
            new = word2vec_aug.augment(line)
            vec.write(new+'\n')

#Wordnet
with open('originaldata\clickbait.txt', 'r') as wordnet_f:  # 打开文件
    with open('augmentdata\wordnet_clickbait.txt','w') as wordnet_w:
        lines = wordnet_f.readlines()
        for line in lines:
            new = wordnet_aug.augment(line) 
            wordnet_w.write(new+'\n')
with open('non_clickbait.txt', 'r',encoding='utf-8') as f:  # 打开文件
    with open('augmentdata\wordnet_non_clickbait.txt','w',encoding='utf-8') as w:
        lines = f.readlines()
        for line in lines:
            new = wordnet_aug.augment(line) 
            w.write(new)
            w.write('\n')
