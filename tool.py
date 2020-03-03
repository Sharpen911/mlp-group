#!/usr/bin/python
#-*-coding:utf-8-*-

with open('originaldata/clickbait.txt', 'r',encoding='utf-8') as f:#load the clickbait title
    lines = f.readlines()
clickbait=[]
for line in lines:
    if line != "\n":
        clickbait.append(line.strip())

with open('originaldata/non_clickbait.txt', 'r',encoding='utf-8') as f:#load the non_clickbait title
    lines = f.readlines()
non_clickbait=[]
for line in lines:
    if line != "\n":
        non_clickbait.append(line.strip())

labels=[]
clickbait_train_sentences=clickbait[:int(0.7*len(clickbait))]
labels+=['1' for i in range(len(clickbait_train_sentences))]#add labels for clickbait type

non_clickbait_train_sentences=non_clickbait[:int(0.7*len(non_clickbait))]
labels+=['0' for i in range(len(non_clickbait_train_sentences))]#add labels for non_clickbait type

clickbait_test_sentences = clickbait[int(0.7*len(clickbait)):]
labels+=['1' for i in range(len(clickbait_test_sentences))]

non_clickbait_test_sentences = non_clickbait[int(0.7*len(non_clickbait)):]
labels+=['0' for i in range(len(non_clickbait_test_sentences))]

train_or_test_list = []

train_sentences = clickbait_train_sentences+non_clickbait_train_sentences
train_or_test_list+=['train' for i in range(len(train_sentences))]

test_sentences = clickbait_test_sentences+non_clickbait_test_sentences
train_or_test_list+=['test' for i in range(len(test_sentences))]

sentences = train_sentences+test_sentences




'''
build my own dataset
'''
dataset_name = 'clickbait'
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















