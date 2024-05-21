import json
import os
from hedge_model.model import SentenceClassifier
from nltk.tokenize import sent_tokenize, word_tokenize
import torch
import re
from tqdm import tqdm
from tagger.annotator import Annotator
from util import preprocess_text
import pandas as pd

file_dir = os.listdir('./final_dataset')
model = SentenceClassifier()

model.load_state_dict(torch.load('F:\code\confidence score-master\hedge_model\lstm_64.pt'))
annotator = Annotator('./tagger/labels.txt', 'F:\code\confidence score-master\\tagger\seqlab_final', 'gpu')
conf_sen_1 = []
conf_word_1 = []
conf_sen_2 = []
conf_word_2 = []
conf_sen_3 = []
conf_word_3 = []
conf_sen_4 = []
conf_word_4 = []
conf_sen_5 = []
conf_word_5 = []
def sentence_token_nltk(str):
    sent_tokenize_list = sent_tokenize(str)
    return sent_tokenize_list

def text_annotate(text):
    asp_list = []
    for sentence in text:
        aspect_sentence = annotator.annotate(sentence)
        asp_dir = {}
        asp = []
        for pair in aspect_sentence:
            if pair[1] == 'O':
                pass
            else:
                asp.append(pair[1])
        if len(asp) == 0:
            asp.append('no_asp')
        asp_t = set(asp)
        asp_dir[sentence] = list(asp_t)
        asp_list.append(asp_dir)
    return asp_list

def hedge_classfication(pre_text):
    pred_hedge = model(pre_text)
    _, out_val = torch.max(torch.softmax(pred_hedge, dim=1), dim=1)
    out = out_val.squeeze().tolist()
    return out

def count_sentenceandword(confidence_score, review_text, review_word):
    if confidence_score[0] == '1':
        conf_sen_1.append(len(review_text))
        conf_word_1.append(len(review_word))
        for sentence in process_text:
            for hedgeword in hws:
                if " " + hedgeword + " " in (" " + sentence.strip('.') + " "):
                    hedge_dic[hedgeword] += 1
    if confidence_score[0] == '2':
        conf_sen_2.append(len(review_text))
        conf_word_2.append(len(review_word))
        for sentence in process_text:
            for hedgeword in hws:
                if " " + hedgeword + " " in (" " + sentence.strip('.') + " "):
                    hedge_dic[hedgeword] += 1
    if confidence_score[0] == '3':
        conf_sen_3.append(len(review_text))
        conf_word_3.append(len(review_word))
        for sentence in process_text:
            for hedgeword in hws:
                if " " + hedgeword + " " in (" " + sentence.strip('.') + " "):
                    hedge_dic[hedgeword] += 1
    if confidence_score[0] == '4':
        conf_sen_4.append(len(review_text))
        conf_word_4.append(len(review_word))
        for sentence in process_text:
            for hedgeword in hws:
                if " " + hedgeword + " " in (" " + sentence.strip('.') + " "):
                    hedge_dic[hedgeword] += 1
    if confidence_score[0] == '5':
        conf_sen_5.append(len(review_text))
        conf_word_5.append(len(review_word))
        for sentence in process_text:
            for hedgeword in hws:
                if " " + hedgeword + " " in (" " + sentence.strip('.') + " "):
                    hedge_dic[hedgeword] += 1

def hedge_word():
    hedge_dic = {}
    with open('F:\code\confidence score-master\hedge_model\hw.txt') as f:
        for h in f:
            h = h.replace(', ', ',')
            word_list = h.split(',')
    with open('F:\code\confidence score-master\hedge_model\hedge_word.txt') as f:
        for w in f:
            hedge_dic[w.strip('\n').lower()] = 0
            #print()
    for word in word_list:
        if word in hedge_dic.keys():
            pass
        else:
            hedge_dic[word] = 0
    return hedge_dic
hedge_dic = hedge_word()
score = ['1', '2', '3', '4', '5']
sen_list = []
text_list = []
for s in score:
    asp_dic = {"clarity_negative": 0, "clarity_positive": 0, "meaningful_comparison_negative": 0,
               "meaningful_comparison_positive": 0, "motivation_negative": 0, "motivation_positive": 0,
               "originality_negative": 0, "originality_positive": 0, "replicability_negative": 0, "replicability_positive": 0,
               "soundness_negative": 0, "soundness_positive": 0, "substance_negative": 0, "substance_positive": 0, "summary": 0}

    count_list =[]
for file in file_dir:
    with open('./final_dataset/' + file) as f:
        data = json.load(f)
        for rev in tqdm(data):
            rev_dir = {}
            if 'review_text' in rev.keys():
                k = 'review_text'
            else:
                k = 'review'
            if 'confidence_score' in rev.keys():
                m = 'confidence_score'
            else:
                m = 'confidence'
            review_text = sentence_token_nltk(rev[k])
            review_word = word_tokenize(preprocess_text(rev[k]))
            confidence_score = re.findall('\d+', rev[m])
            hws = hedge_dic.keys()
            count_sentenceandword(confidence_score, review_text, review_word)
            process_text = list(map(preprocess_text, review_text))
            # if rev['confidence_score'] == '5':
            #     pred_hedge = hedge_classfication(process_text)
            #     for lab in range(len(pred_hedge)):
            #         if pred_hedge[lab] == 1:
            #             print(review_text[lab])
            #
            # print()
            for p_t in process_text:
                if len(p_t) < 2:
                    process_text.remove(p_t)
            uncen_count = 0
            if confidence_score[0] == s:
                pred_hedge = hedge_classfication(process_text)
                if isinstance(pred_hedge, int):
                    anatk = []
                    anatk.append(pred_hedge)
                    pred_hedge = anatk
                #asp_list = text_annotate(process_text)
                for pre in range(len(pred_hedge)):
                    asp = []
                    if pred_hedge[pre] == 1:
                        uncen_count += 1
                            #asp_val = asp_list[pre].values()
                        keyofhed = hedge_dic.keys()
                        for k in keyofhed:
                            if " " + k + " " in (" " + process_text[pre].strip('.') + " "):
                                aspect_sentence = annotator.annotate(process_text[pre])

                                for pair in aspect_sentence:
                                    if pair[1] == 'O':
                                        pass
                                    else:
                                        asp.append(pair[1])
                                if len(asp) == 0:
                                    asp.append('no_asp')
                                asp_t = list(set(asp))
                                # if len(asp_t)>1:
                                #     print(asp_t)
                                for asp_p in asp_t:
                                    if asp_p in asp_dic:
                                        asp_dic[asp_p] += 1
                                break
                            else:
                                pass

                count_list.append(uncen_count)
    result_dic = sorted(asp_dic.items(), key=lambda x: x[1], reverse=True)
    with open(s + 'conf_asp.json', 'w') as f:
        json.dump(result_dic, f)
    print(s + ":", result_dic)
    aver = sum(count_list) / len(count_list)
    print(s + ':', aver)


    asp_dic = {'confidence_score': 0, 'soundness': 0, 'clarity': 0, 'substance': 0, 'originality': 0,
                       'meaningful': 0, 'motivation': 0, 'replicability': 0, 'num_sentence': 0, 'decision': 0}
    asp_dic_2 = {'confidence_score': 0, 'soundness': 0, 'clarity': 0, 'substance': 0, 'originality': 0,
                       'meaningful': 0, 'motivation': 0, 'replicability': 0, 'num_sentence': 0, 'decision': 0}
    asp_list = text_annotate(review_text)
    rev_list = []
    if isinstance(pred_hedge, int):
        anatk = []
        anatk.append(pred_hedge)
        pred_hedge = anatk
    for i in range(len(asp_list)):
        sen_dir = {}
        for k, v in asp_list[i].items():
            sen_dir['sentence'] = k
            sen_dir['aspect'] = v
        sen_dir['label'] = pred_hedge[i]
        rev_list.append(sen_dir)
        for send in rev_list:
            if send['label'] == 1:
                asp_dic_2['num_sentence'] += 1
                if 'no_asp' in send['aspect']:
                    pass
                elif 'summary' in send['aspect']:
                    pass
                else:
                    for asp in send['aspect']:
                        asp_res = asp.split('_')
                        asp_dic_2[asp_res[0]] += 1

    asp_dic_2['confidence_score'] = confidence_score[0]
    for res in rev_list:
        ss = res['aspect']

        if 'no_asp' in ss:
            pass
        elif 'summary' in ss:
            pass
        else:
            for asp in res['aspect']:
                asp_res = asp.split('_')
                asp_dic[asp_res[0]] += 1
    asp_dic['confidence_score'] = confidence_score[0]
    asp_dic['num_sentence'] = len(review_text)
    if 'Accept' in rev['decision']:
        asp_dic_2['decision'] = 1
        asp_dic['decision'] = 1
    else:
        asp_dic_2['decision'] = 0
        asp_dic['decision'] = 0
    text_list.append(asp_dic)
    sen_list.append(asp_dic_2)
#


df_1 = pd.DataFrame(sen_list)
df_1.to_excel('sent_asp.xlsx', index=False)
df_2 = pd.DataFrame(text_list)
df_2.to_excel('text_asp.xlsx', index=False)
result_dic = sorted(asp_dic.items(), key=lambda x : x[1], reverse=True)
with open('conf5_asp.json', 'w') as f:
    json.dump(result_dic, f)
print(result_dic)
aver_1 = sum(conf_word_1) / len(conf_word_1)
aver_2 = sum(conf_word_2) / len(conf_word_2)
aver_3 = sum(conf_word_3) / len(conf_word_3)
aver_4 = sum(conf_word_4) / len(conf_word_4)
aver_5 = sum(conf_word_5) / len(conf_word_5)
aver = sum(count_list) / len(count_list)
print(aver)
aver_1 = sum(conf_sen_1) / len(conf_sen_1)
aver_2 = sum(conf_sen_2) / len(conf_sen_2)
aver_3 = sum(conf_sen_3) / len(conf_sen_3)
aver_4 = sum(conf_sen_4) / len(conf_sen_4)
aver_5 = sum(conf_sen_5) / len(conf_sen_5)
print('aver1:', aver_1)
print('aver2:', aver_2)
print('aver3:', aver_3)
print('aver4:', aver_4)
print('aver5:', aver_5)