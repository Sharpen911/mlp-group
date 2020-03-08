# MLP group project

data_aug.py: 生成数据增强以后的文本,并储存在augmentdata文件夹下面.用wordnet生成的文件已经有了

使用方法:
1  运行prepare_data.py,通过修改里面的dataset_name  datatype 来选择使用使用/未使用数据增强的各种数据集

2 python remove_word.py --dataset ='选的数据集' --datatype = 'wordnet'or'word2vec'  default = 使用原本的文本

3 python build_graph.py --dataset ='' --datatype =''

4 python train.py(还需要修改)