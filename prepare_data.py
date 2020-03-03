#!/usr/bin/python
#-*-coding:utf-8-*-
import random




dataset_name = 'StackOverflow'
with open('origialdatas/StackOverflow.txt', 'r',encoding='utf-8') as f:
    sentences = f.read().splitlines()
with open('origialdatas/StackOverflow_gnd.txt', 'r',encoding='utf-8') as f:
    labels = f.read().splitlines()
random.seed(233333)
random.shuffle(sentences)
random.seed(233333)
random.shuffle(labels)


train_list = ['train' for i in range(int(0.7*len(sentences)))]
test_list = ['test' for j in range(int(0.3*len(sentences)))]
train_or_test_list = train_list+test_list



meta_data_list = []

for i in range(len(sentences)):
    meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
    meta_data_list.append(meta)

meta_data_str = '\n'.join(meta_data_list)

f = open('data/' + dataset_name + '.txt', 'w',encoding='utf-8')
f.write(meta_data_str)
f.close()

corpus_str = '\n'.join(sentences)

f = open('data/corpus/' + dataset_name + '.txt', 'w',encoding='utf-8')
f.write(corpus_str)
f.close()
