from textaugment import Wordnet
import random


dataset_name = 'Click'
source_path = 'originaldata'
save_path = 'augmentdata'

wordnet_aug = Wordnet(v=False,n=True, p=0.5)


if dataset_name=='Click':
    with open(source_path+'/'+dataset_name+'bait.txt', 'r',encoding='utf-8') as f:  # load the clickbait title

        pos_sentences =[i for i in f.read().splitlines() if i!='']


    with open(source_path+'/'+'non_'+dataset_name+'bait.txt', 'r',encoding='utf-8') as f:  # load the non_clickbait title
        neg_sentences = [j for j in f.read().splitlines() if j!='']


    for i in range(len(pos_sentences)):
        augmented = wordnet_aug.augment(pos_sentences[i])
        if pos_sentences[i].lower() == augmented:
            #pos_sentences[i]+=' '+augmented
            pos_sentences.append(augmented)

    for j in range(len(neg_sentences)):
        augmented = wordnet_aug.augment(neg_sentences[j])
        if neg_sentences[j].lower() == augmented:
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




#TODO:another 3 dataset
else:
    with open(source_path+'/'+dataset_name+'.txt', 'r',encoding='utf-8') as f:
        sentences = f.read().splitlines()
    with open(source_path+'/'+dataset_name+'_gnd'+'.txt', 'r',encoding='utf-8') as f:
        labels = f.read().splitlines()

