import pickle
import torch
import numpy as np
import os
from util import preprocess_text
from torch.utils.data import Dataset, DataLoader, SubsetRandomSampler
from transformers import *
import torch.nn as nn
#conf_name = ""
torch.manual_seed(400)
np.random.seed(400)
import json
import tqdm
from sentence_transformers import SentenceTransformer


torch.manual_seed(400)
np.random.seed(400)

torch.cuda.set_device(0)
model = SentenceTransformer('stsb-roberta-base')
os.environ['TOKENIZERS_PARALLELISM'] = 'False'

#batch_size = 16
class Data(Dataset):
    def __init__(self, hedge_sentence, labels):
        self.hedge_sentence = hedge_sentence
        self.label = labels
        self.max_len = 50


    @classmethod

    def getReader(self):
        with open('hedge_sentence.json') as f:
            datasets = json.load(f)
        hedge_dataset = []
        for t in datasets:
            preprocess_dir = {}
            s = t['sentences']
            #preprocess_dir['raw_sentence'] = s
            process_s = preprocess_text(s)
            preprocess_dir['sentence'] = process_s
            desc = torch.zeros(1)
            desc[0] = t['label']
            preprocess_dir['label'] = desc[0]
            hedge_dataset.append(preprocess_dir)



        train_size = int(0.8 * len(hedge_dataset))
        test_size = len(hedge_dataset) - train_size

        train_dataset, test_dataset = torch.utils.data.random_split(hedge_dataset, [train_size, test_size])

        return train_dataset, test_dataset

    def test_data(batch_size):
        with open('hedge_sentence.json') as f:
            datasets = json.load(f)
            hedge_dataset = []
            for t in datasets:
                pre_dir = {}
                s = t['sentences']
                pre_dir['raw_sentence'] = s
                process_s = preprocess_text(s)
                pre_dir['sentence'] = process_s
                #print(t['label'])
                desc = torch.zeros(1)
                desc[0] = t['label']
                pre_dir['label'] = desc[0]
                #print(pre_dir['label'])
                hedge_dataset.append(pre_dir)
        test_sampler = SubsetRandomSampler(range(100))
        test_loader = DataLoader(hedge_dataset, batch_size=batch_size, sampler=test_sampler)
        return test_loader
def getLoaders(batch_size):
    print('Reading the training Dataset...')

    train_dataset, test_dataset = Data.getReader()

    print('Reading the validation Dataset...')
    #print()

    trainloader = DataLoader(dataset=train_dataset, batch_size=batch_size, num_workers=0, shuffle=True)
    validloader = DataLoader(dataset=test_dataset, batch_size=batch_size, num_workers=0, shuffle=True)
    return trainloader, validloader
def gettestLoaders(batch_size):
    print('Reading the training Dataset...')

    test_d = Data.test_data(batch_size=batch_size)

    print('Reading the validation Dataset...')
    #print()
    return test_d
#a = getLoaders(16)
#b = gettestLoaders(16)

