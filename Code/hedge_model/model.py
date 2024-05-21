import transformers
from transformers import AutoConfig,AutoModel,AutoTokenizer,logging
from torch.utils.data import RandomSampler,Dataset, DataLoader
from transformers import BertModel, BertTokenizer, BertConfig, AdamW, get_linear_schedule_with_warmup
from transformers import RobertaTokenizer, RobertaModel
# 导入torch
import torch
import torch.nn as nn
import torch.nn.functional as F

# 常用包
import re
import os
import numpy as np
import pandas as pd
from tqdm import tqdm
import pickle
import os
import torch
import torch.nn as nn
from torch.utils import data
from sklearn.utils import resample
from sentence_transformers import SentenceTransformer
from sklearn.metrics import accuracy_score
# 全局变量
os.environ["TOKENIZERS_PARALLELISM"] = "false"
RANDOM_SEED = 400
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
class SentenceClassifier(nn.Module):
    def __init__(self):
        n_classes = 2
        super(SentenceClassifier, self).__init__()
        # 如果是Bert_large，此处是
        # PRE_TRAINED_MODEL_NAME = "bert-large-uncased"
        # self.robert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME)
        # 如果是bert_base，此处是
        #PRE_TRAINED_MODEL_NAME = "bert-base-uncased"
        #self.robert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME)
        # 如果是roberta_large，此处是
        # PRE_TRAINED_MODEL_NAME = 'roberta-large'
        # self.robert = RobertaModel.from_pretrained(PRE_TRAINED_MODEL_NAME)
        self.model = SentenceTransformer('stsb-roberta-base')
        self.bilstm = nn.LSTM(input_size=768,
                              hidden_size=768, batch_first=True, bidirectional=True).to(device)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(768 * 2, n_classes).to(device)
        self.sigmoid = nn.Sigmoid()
    def forward(self, sentence):
        input_sentence = torch.from_numpy(self.model.encode(sentence)).to(device)
        #print()
        last_hidden_out = self.drop(input_sentence)
        output_hidden, _ = self.bilstm(last_hidden_out.unsqueeze(1))  # [10, 300, 768]
        output = self.drop(output_hidden) # dropout
        output = output.mean(dim=1)

        output = self.out(output)
        return output