# Global-Encoding
This code is based on the paper *Global Encoding for Abstractive Summarization*, https://arxiv.org/abs/1805.03989 and it's github,https://github.com/lancopku/Global-Encoding

***********************************************************

## Requirements
* Ubuntu 16.0.4
* Python 3.5
* Pytorch 0.4.1
* pyrouge(did not use)

*************************************************************
## .yaml文件参数设置
data:处理后数据所在的位置
logF：log日志及模型保存所在的文件夹
batch_size:如果出现out of memorzy，将batch_size调小
eval_interval:每训练x轮输出一次验证集结果。
save_interval:每训练x轮保存一次当前的模型。

## 数据预处理
中文数据分字，每个字之间加一个空格，例子：
市 民 反 映 ， 自 家 住 在 东 城 区 崇 文 门 外 街 道 西 花 市 南 里 西 区 新 景 家 园 1 2 号 楼 ， 1 0 号 楼 和 1 2 号 楼 两 栋 楼 的 暖 气 都 不 热 ， 在 1 6 度 左 右 , 属 于 集 中 供 暖 ， 供 暖 单 位 ： 北 京 热 能 集 团 ， 来 电 反 映 温 度 不 达 标 的 问 题 。 

数据共6个文件，将这6个文件放在一个文件夹内
train.src 训练集 原文
train.tgt  参考的摘要
test.src  测试集
test.tgt
valid.src 验证集
valid.tgt
```
python3 preprocess.py -load_data path_to_data -save_data path_to_store_data
```
>-load_data 上面这6个原始数据文件所在的文件夹
-save_data 处理后的数据集所放的文件夹

## 模型的训练
```
python3 train.py -log log_name -config test.yaml -gpus id
```
>-log log文件夹的名称，log会存放在上面test.yaml文件中logF的目录下，即logF/log_name
>-config 即配置文件，上述的test.yaml
>-gpus id 调用某个id的gpu进行训练

**每eval_interval轮训练后，可以在logF/log_name文件夹下查看验证集的输出结果，
checkpoint.pt是保存的模型文件，
candidate.txt是模型对验证集的生成结果
reference.txt是作为参考的摘要
best_bleu_checkpoint.pt是最优的一个模型
best_bleu_prediction.pt是最优模型预测的验证集的数据**

## 模型的评价
```
python3 train.py -log log_name -config config_yaml -gpus id -restore checkpoint -mode eval
```
>-restore checkpoint 直接调用训练好的模型，即.pt文件的路径
>-mode eval 评价模式（不用修改）

## extra
server.py为封装好的测试用的socket服务端，client.py为客户端
使用时保证数据文件中valid.src和valid.tgt中只有一条数据，然后重新预处理数据
服务端使用方法同模型的评价：
```
python3 server.py -log log_name -config config_yaml -gpus id -restore checkpoint -mode eval
```
客户端使用方法
```
python3 client.py
```

# Source
```
@inproceedings{globalencoding,
  title     = {Global Encoding for Abstractive Summarization},
  author    = {Junyang Lin and Xu Sun and Shuming Ma and Qi Su},
  booktitle = {{ACL} 2018},
  year      = {2018}
}
```
