from nltk.corpus import stopwords
import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from utils import clean_str, loadWord2Vec
import sys
import argparse
import random
from collections import Counter





parser = argparse.ArgumentParser(description='Build Document Graph')
parser.add_argument('--dataset', type=str, default='20ng',
                    choices=['Click','Biomedical','SearchSnippets','StackOverflow'],
                    help='dataset name')

parser.add_argument('--datatype', type=str, default='originaldata',
                    choices=['wordnet_data','word2vec_data'],
                    help='use augmentation data or not')

args = parser.parse_args()

dataset = args.dataset

datatype = args.datatype

train_val_ids = []
test_ids = []

with open(datatype+'/data/' + dataset + '.txt', 'r') as f:
    lines = f.readlines()
    for id, line in enumerate(lines):
        _, data_name, data_label = line.strip().split("\t")
        if data_name.find('test') != -1:
            test_ids.append(id)
        elif data_name.find('train') != -1:
            train_val_ids.append(id)

idx = list(range(len(train_val_ids)))
random.shuffle(idx)
train_val_ids = [train_val_ids[i] for i in idx]

idx = list(range(len(test_ids)))
random.shuffle(idx)
test_ids = [test_ids[i] for i in idx]

train_val_size = len(train_val_ids)
val_size = int(0.1 * train_val_size)
train_size = train_val_size - val_size
train_ids, val_ids = train_val_ids[:train_size], train_val_ids[train_size:]

doc_content_list = []

f = open(datatype+'/data/corpus/' + dataset + '.txt', 'rb')
for line in f.readlines():
    doc_content_list.append(line.strip().decode('latin1'))
f.close()

with open(datatype+'/data/ind.train.ids', "w") as f:
    f.write('\n'.join([str(i) for i in train_ids]))
with open(datatype+'/data/ind.val.ids', "w") as f:
    f.write('\n'.join([str(i) for i in val_ids]))
with open(datatype+'/data/ind.test.ids', "w") as f:
    f.write('\n'.join([str(i) for i in test_ids]))

def get_clean_words(docs):
    clean_words = []
    for doc in docs:

        temp = clean_str(doc).split()
        clean_words.append(temp)
    return clean_words
clean_words = get_clean_words(doc_content_list)

word_freq = Counter()
# total = 0
for i in train_ids+test_ids+val_ids:
    doc_words = clean_words[i]
    word_freq.update(doc_words)

vocab, count = zip(*word_freq.most_common())
if dataset == "Click":
    cutoff = -1
else:
    cutoff = count.index(5)

vocab = set(vocab[:cutoff])

clean_docs = []
for words in clean_words:
    closed_words = [w for w in words if w in vocab ]
    doc_str = ' '.join(closed_words)
    clean_docs.append(doc_str)

clean_corpus_str = '\n'.join(clean_docs)

f = open(datatype+'/data/corpus/' + dataset + '.clean.txt', 'w')
f.write(clean_corpus_str)
f.close()

# dataset = args.dataset
# min_len = 10000
# aver_len = 0
# max_len = 0

# f = open('data/corpus/' + dataset + '.clean.txt', 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     temp = line.split()
#     aver_len = aver_len + len(temp)
#     if len(temp) < min_len:
#         min_len = len(temp)
#     if len(temp) > max_len:
#         max_len = len(temp)
# f.close()
# aver_len = 1.0 * aver_len / len(lines)
# print('min_len : ' + str(min_len))
# print('max_len : ' + str(max_len))
# print('average_len : ' + str(aver_len))
