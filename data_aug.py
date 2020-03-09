from textaugment import Wordnet
from textaugment import Word2vec
import gensim

dataset_name = 'Click'
source_path = 'originaldata'
save_path = 'word2vec_data'

if save_path=='word2vec_data':
    word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('./googlemodel.bin',binary=True)
    augment_model = Word2vec(model=word2vec_model, runs=1, v=False, p=0.2)
if save_path=='wordnet_data':
    augment_model = Wordnet(v=False,n=True, p=0.2)


if dataset_name=='Click':
    with open(source_path+'/'+dataset_name+'bait.txt', 'r',encoding='utf-8') as f:  # load the clickbait title

        pos_sentences =[i for i in f.read().splitlines() if i!='']


    with open(source_path+'/'+'non_'+dataset_name+'bait.txt', 'r',encoding='utf-8') as f:  # load the non_clickbait title
        neg_sentences = [j for j in f.read().splitlines() if j!='']


    for i in range(len(pos_sentences)):
        augmented = augment_model.augment(pos_sentences[i])
        if pos_sentences[i].lower() != augmented:
            #pos_sentences[i]+=' '+augmented
            pos_sentences.append(augmented)

    for j in range(len(neg_sentences)):
        augmented = augment_model.augment(neg_sentences[j])
        if neg_sentences[j].lower() != augmented:
            #neg_sentences[j]+=' '+augmented
            neg_sentences.append(augmented)

    augment_corpus_str = '\n'.join(pos_sentences)

    f = open(save_path+'/Clickbait.txt', 'w',encoding='utf-8')
    f.write(augment_corpus_str)
    f.close()

    augment_corpus_str = '\n'.join(neg_sentences)
    f = open(save_path + '/non_Clickbait.txt', 'w', encoding='utf-8')
    f.write(augment_corpus_str)
    f.close()





else:
    with open(source_path+'/'+dataset_name+'.txt', 'r',encoding='utf-8') as f:
        sentences = f.read().splitlines()
    with open(source_path+'/'+dataset_name+'_gnd'+'.txt', 'r',encoding='utf-8') as f:
        labels = f.read().splitlines()

    aug_sentences=[]
    aug_labels = []
    for i in range(len(sentences)):
        augmented = augment_model.augment(sentences[i])
        if sentences[i].lower() != augmented:
            aug_sentences.append(augmented)
            aug_labels.append(labels[i])

    sentences+=aug_sentences
    labels+=aug_labels

    augment_sentences = '\n'.join(sentences)
    f = open(save_path + '/'+dataset_name+'.txt', 'w', encoding='utf-8')
    f.write(augment_sentences)
    f.close()

    augment_labels = '\n'.join(labels)
    f = open(save_path + '/' + dataset_name + '_gnd.txt', 'w', encoding='utf-8')
    f.write(augment_labels)
    f.close()
