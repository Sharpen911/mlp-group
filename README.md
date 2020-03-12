# MLP group project



使用方法:
1  运行prepare_data.py,通过修改里面的dataset_name  datatype 生成用来训练的文本.通过修改这个文件的第66行,来决定从训练集中抽样百分之多少来增强

2 python remove_words.py --dataset Click --datatype  wordnet_data(or word2vec_data)  default :使用原本的文本

3 python build_graph.py --dataset Click --datatype =wordnet_data

4 python train.py --dataset =Click --datatype =wordnet_data --seed 42
