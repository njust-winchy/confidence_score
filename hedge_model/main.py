import pickle
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from model import SentenceClassifier
from transformers import AdamW, get_linear_schedule_with_warmup
from tqdm.autonotebook import tqdm
#import logging
from util import BCEFocalLoss
import os
import torch
import matplotlib.pyplot as plt
from load_data import getLoaders
from tqdm.autonotebook import tqdm
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, classification_report
from sentence_transformers import SentenceTransformer
from transformers import *
import os
#from util import sigmoid_focal_loss

torch.cuda.set_device(0)
os.environ['TOKENIZERS_PARALLELISM']='False'

# tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
# model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased')
batch_size = 64
#model = SentenceTransformer('stsb-roberta-base')
#model = AutoModel.from_pretrained('bert-base-cased')
torch.manual_seed(400)
np.random.seed(400)

train_loader, val_loader = getLoaders(batch_size)

if torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
  print('No GPU available, using the CPU instead.')
  device = torch.device("cpu")

text_model = SentenceClassifier()
text_model.to(device)
#criterion = nn.CrossEntropyLoss()
criterion = BCEFocalLoss()

no_decay = ['bias', 'LayerNorm.weight']
optimizer_grouped_parameters = [
    {'params': [p for n, p in text_model.named_parameters() if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
    {'params': [p for n, p in text_model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.01}
]
optimizer = torch.optim.AdamW(optimizer_grouped_parameters, lr=0.001, weight_decay=1e-4)
#scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=6, gamma=0.01)  # 设定优优化器更新的时刻表

text_model.train()
result = []
EPOCH = 12
print("number of epoch = ", EPOCH)

loss_log1 = []
loss_log2 = []

train_f1_log = []

val_f1_log = []

train_acc_log = []
val_acc_log = []

final_output_train = []
final_output_val = []

best_val_out = []
max_acc = 0
#logger = getLogger()
for epoch in range(EPOCH):
    train_out = []
    train_true = []

    val_out = []
    val_true = []

    final_train_loss = 0.0
    final_val_loss = 0.0

    l1 = []
    l2 = []

    text_model.train()

    for data in tqdm(train_loader, desc="Train epoch {}/{}".format(epoch + 1, EPOCH)):
        sentence = data['sentence']


        targets = data['label'].to(device)


        optimizer.zero_grad()
        pred = text_model(sentence)
        #_, out = torch.max(torch.softmax(pred, dim=1), dim=1)
        loss = criterion(pred, targets.long())

        train_out += pred.squeeze().tolist()
        train_true += targets.squeeze().tolist()
        #loss.requires_grad_(True)
        l1.append(loss.item())
        final_train_loss += loss.item()
        loss.backward()
        optimizer.step()

    loss_log1.append(np.average(l1))
    #scheduler.step()
    with torch.no_grad():
        text_model.eval()

        for data in tqdm(val_loader, desc="Valid epoch {}/{}".format(epoch + 1, EPOCH)):
            sentence = data['sentence']

            #input_sentence = torch.from_numpy(model.encode(sentence)).to(device)
            targets = data['label'].to(device)

            pred_val = text_model(sentence)
            #_, out_val = torch.max(torch.softmax(pred_val, dim=1), dim=1)


            loss = criterion(pred_val, targets.long())
            #loss.requires_grad_(True)
            val_out += pred_val.squeeze().tolist()
            val_true += targets.squeeze().tolist()
            l2.append(loss.item())
            l2.append(loss.item())

            final_val_loss += loss.item()

        # scheduler.step(final_val_loss)
        loss_log2.append(np.average(l2))
        curr_lr = optimizer.param_groups[0]['lr']

    train_out = np.array([s > 0.5 for s in train_out])
    train_true = np.array(train_true)

    val_out = np.array([s > 0.5 for s in val_out])
    val_true = np.array(val_true)

    print("Epoch {}, loss: {}, val_loss: {}".format(epoch + 1, final_train_loss / len(train_loader),
                                                    final_val_loss / len(val_loader)))
    print(
        f"TRAINING F1 SCORE: {f1_score(train_true, train_out, average='weighted')} \nValidation F1 SCORE: {f1_score(val_true, val_out, average='weighted')}")
    print(
        f"TRAINING ACCURACY: {accuracy_score(train_true, train_out)} \nValidation ACCURACY: {accuracy_score(val_true, val_out)}")
    #w_m = w_m.detach().cpu()
    # s_i=s_i.detach().cpu()

    # if (epoch == EPOCH - 1):
    #     print(classification_report(val_true, val_out))
    #     with open("weight_matrix_JCDL.pickle", 'wb') as out:
    #         pickle.dump(w_m, out)

    train_f1_log.append(f1_score(train_true, train_out))
    val_f1_log.append(f1_score(val_true, val_out))

    train_acc_log.append(accuracy_score(train_true, train_out))
    val_acc_log.append(accuracy_score(val_true, val_out))

    if (accuracy_score(val_true, val_out) > max_acc):
        torch.save(text_model.state_dict(), "final_model.pt")
        max_acc = accuracy_score(val_true, val_out)
        best_val_out = val_out
    #logger.info('train|epoch:{epoch}\\train_acc:{acc}\\tloss:{loss:.4f}\\t valid_acc:{val_acc}'.format(epoch=epoch, acc=accuracy_score(train_true, train_out),
     #                                                                                   loss=loss.item(),val_acc= accuracy_score(val_true, val_out)))  # 打印训练日志

plt.plot(range(len(loss_log1)), loss_log1)
plt.plot(range(len(loss_log2)), loss_log2)
plt.savefig('loss_curve.png')
print("MAXIMUM ACCURACY:", max_acc)
