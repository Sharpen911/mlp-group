#!/usr/bin/python
#-*-coding:utf-8-*-
import random
from textaugment import Wordnet
from textaugment import Word2vec
import gensim



dataset_name = 'SearchSnippets'
datatype = 'word2vec_data' #Choose word2vec_data,wordnet_data or originaldata


if datatype=='word2vec_data':
    word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('./googlemodel.bin',binary=True)
    augment_model = Word2vec(model=word2vec_model, runs=1, v=False, p=0.5)
if datatype=='wordnet_data':
    augment_model = Wordnet(v=False,n=True, p=0.9)






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


train_sentences = sentences[:int(0.7*len(sentences))]
train_labels = labels[:int(0.7*len(labels))]
test_sentences = sentences[int(0.7 * len(sentences)):]
test_labels = labels[int(0.7 * len(labels)):]

if datatype!='originaldata':
    index = range(len(train_sentences))
    selected_index = random.sample(index,int(0.3*len(train_sentences)))
    selected_index.sort()
    for i in selected_index:
        augmented = augment_model.augment(train_sentences[i])
        train_sentences.append(augmented)
        train_labels.append(train_labels[i])

sentences = train_sentences+test_sentences
labels = train_labels+test_labels







train_list = ['train']*(len(train_labels))
test_list = ['test']*(len(test_labels))

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
