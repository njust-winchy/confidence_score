import pandas as pd
import json
data_path = '../dataset/HedgePeer.jsonl'

Hedge_data = pd.read_json(path_or_buf=data_path, lines=True)
data_list = []
for index, row in Hedge_data.iterrows():
    rev_id = row['Review_id']
    sents = row['Sentences']
    for s in sents:
        hedges = s['Hedges']
        if(len(hedges)==0):
            d = {}
            d['Review_id'] = rev_id
            d['Sentence_id'] = s['Sentence_id']
            d['Raw Sentence'] = s['Sentence']
            d['Hedged Sentence'] = s['Sentence']
            d['Hedge'] = 'NO HEDGE'
            d['Span'] = None
            data_list.append(d)
        else:
            for h in hedges:
                d = {}
                d['Review_id'] = rev_id
                d['Sentence_id'] = s['Sentence_id']
                d['Raw Sentence'] = s['Sentence']
                d['Hedged Sentence'] = h['Hedged Sentence']
                d['Hedge'] = h['Hedge']
                d['Span'] = h['Span']
                data_list.append(d)
hedges_list = []
t = 0
f = 0
hedge_sentence_dataset = []
for hedge_dir in data_list:
    hedge_sentence = {}
    hedge = hedge_dir['Hedge']
    if hedge == 'NO HEDGE':
        hedge_sentence['sentences'] = hedge_dir['Raw Sentence']
        hedge_sentence['label'] = 0
        t = t + 1
        hedge_sentence_dataset.append(hedge_sentence)
    else:
        hedge_sentence['sentences'] = hedge_dir['Raw Sentence']
        hedge_sentence['label'] = 1
        f = f + 1
        hedge_sentence_dataset.append(hedge_sentence)
        if hedge not in hedges_list:
            hedges_list.append(hedge)
print(t,f)
# with open('hedge_sentence.json', 'w') as f:
#     json.dump(hedge_sentence_dataset, f)
with open('hedge_word.txt', 'w') as fp:
    for words in hedges_list:
        fp.writelines(words)
        fp.writelines('\n')
