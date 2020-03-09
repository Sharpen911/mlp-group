#!/usr/bin/python
#-*-coding:utf-8-*-
import random




dataset_name = 'StackOverFlow'
datatype = 'originaldata' #Choose word2vec_data,wordnet_data or originaldata

if dataset_name=='Click':
    with open(datatype + '/' + dataset_name + 'bait.txt', 'r', encoding='utf-8') as f:  # load the clickbait title

        pos_sentences = [i for i in f.read().splitlines() if i != '']

    with open(datatype + '/' + 'non_' + dataset_name + 'bait.txt', 'r',
              encoding='utf-8') as f:  # load the non_clickbait title
        neg_sentences = [j for j in f.read().splitlines() if j != '']




    sentences = pos_sentences+neg_sentences

    pos_label = ['1']*(len(pos_sentences))
    neg_label = ['0']*len(neg_sentences)
    labels = pos_label+neg_label



else:
    with open(datatype+'/'+dataset_name+'.txt', 'r',encoding='utf-8') as f:
        sentences = f.read().splitlines()
    with open(datatype+'/'+dataset_name+'_gnd'+'.txt', 'r',encoding='utf-8') as f:
        labels = f.read().splitlines()

random.seed(233333)
random.shuffle(sentences)
random.seed(233333)
random.shuffle(labels)


train_list = ['train']*(int(0.7*len(labels)))

test_list = ['test']*(int(0.3*len(labels))+1)

train_or_test_list = train_list+test_list


meta_data_list = []

for i in range(len(sentences)):
    meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
    meta_data_list.append(meta)

meta_data_str = '\n'.join(meta_data_list)


f = open(datatype+'/data/' + dataset_name + '.txt', 'w',encoding='utf-8')
f.write(meta_data_str)
f.close()

corpus_str = '\n'.join(sentences)

f = open(datatype+'/data/corpus/' + dataset_name + '.txt', 'w',encoding='utf-8')
f.write(corpus_str)
f.close()
