import json

import torch
from model import SentenceClassifier
from load_data import gettestLoaders
from tqdm.autonotebook import tqdm
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, classification_report

import numpy as np
device = torch.device("cuda:0")

batch_size = 16
model = SentenceClassifier()
model.load_state_dict(torch.load('F:\code\confidence score-master\hedge_model\lstm_64.pt'))


test_loader = gettestLoaders(batch_size)
test_out = []
test_true = []
result = []
m = 0
for data in tqdm(test_loader, desc="test "):
    sentence = data['sentence']

    targets = data['label'].to(device)

    pred = model(sentence)
    _, out = torch.max(torch.softmax(pred, dim=1), dim=1)

    test_out += out.squeeze().tolist()
    test_true += targets.long().squeeze().tolist()
    for i in range(len(sentence)):
        resultt = {}
        resultt['raw sentence:'] = sentence[i]
        resultt['correct label:'] = test_true[i+m]
        resultt['predict:'] = test_out[i+m]
        result.append(resultt)

    m = i + m + 1


with open('result.json', 'w') as f:
    for words in result:
        json.dump(words, f, indent=4)





