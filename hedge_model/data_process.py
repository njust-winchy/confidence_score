import os
import jsonlines
import torch.utils.data
from tqdm.autonotebook import tqdm
import pickle
import json
from torch import nn
from torch.utils.data import DataLoader
from util import preprocess_text
import numpy as np
import matplotlib.pyplot as plt

hedge_dataset = []
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

with open('hedge_sentence.json') as f:
    data = json.load(f)
for t in tqdm(data):
    preprocess_dir = {}
    s = t['sentences']
    process_s = preprocess_text(s)
    preprocess_dir['sentence'] = process_s
    preprocess_dir['label'] = t['label']
    hedge_dataset.append(preprocess_dir)

train_size = int(0.8 * len(hedge_dataset))
test_size = len(hedge_dataset) - train_size

train_dataset, test_dataset = torch.utils.data.random_split(hedge_dataset, [train_size, test_size])

hedge_train = []
hedge_test = []
for x in tqdm(train_dataset):
    m = {}
    bert_token = tokenizer(x['sentence'], padding="max_length", truncation=True)
    m['sentence'] = x['sentence']
    m['input_ids'] = bert_token['input_ids']
    m['attention_mask'] = bert_token['attention_mask']
    m['label'] = x['label']
    hedge_train.append(m)
for n in tqdm(test_dataset):
    i = {}
    bert_token1 = tokenizer(n['sentence'], padding="max_length", truncation=True)
    i['sentence'] = n['sentence']
    i['input_ids'] = bert_token1['input_ids']
    i['attention_mask'] = bert_token1['attention_mask']
    i['label'] = n['label']
    hedge_test.append(i)
with open('train_data.json', 'w') as f:
    json.dump(hedge_train, f)
with open('test_data.json', 'w') as fp:
    json.dump(hedge_test, fp)
print()


