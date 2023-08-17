import os
import json
import numpy as np
import re
from util import preprocess_text
from nltk.tokenize import sent_tokenize, word_tokenize
list_d = os.listdir('dataset')
arr_final_review = []
coling_final_review = []
acl_final_review = []
conll_final_review = []
iclr_2017_final_review = []
iclr_2018_final_review = []
iclr_2019_final_review = []
iclr_2021_final_review = []
iclr_2022_final_review = []
arr_s = []
arr_w = []
coling_s = []
coling_w = []
acl_s = []
acl_w = []
conll_s = []
conll_w = []
iclr_2017_s = []
iclr_2017_w = []
iclr_2018_s = []
iclr_2018_w = []
iclr_2019_s = []
iclr_2019_w = []
iclr_2021_s = []
iclr_2021_w = []
iclr_2022_s = []
iclr_2022_w = []
accept = 0
reject = 0
s = 0
confidence_count = np.zeros(11)
score_count = np.zeros([11,11])
for li in list_d:
    if li == 'ARR-22':
        arr_file_dir = './dataset/' + li + '/data'
        arr_second_list = os.listdir(arr_file_dir)
        arr_second_list.remove('LICENSE.txt')
        arr_second_list.remove('meta.json')
        #print(len(arr_second_list))
        for arr_revlist in arr_second_list:
            accept = accept + 1

            arr_review_file = arr_file_dir + '/' + arr_revlist + '/v1/' + 'reviews.json'
            with open(arr_review_file) as f:
                arr_rev = json.load(f)
                for arr_text in arr_rev:
                    arr_result = {}
                    arr_review_text = ''
                    for t in arr_text['report']:
                        arr_review_text = arr_review_text + arr_text['report'][t]
                        #print(review_text)
                    ff = preprocess_text(arr_review_text)
                    arr_w.append(len(word_tokenize(ff)))
                    arr_s.append(len(sent_tokenize(ff)))
                    arr_scores = arr_text['scores']['overall']
                    arr_confidence_score = arr_text['meta']['confidence']
                    arr_result['decision'] = 'Accept'
                    arr_result['review_text'] = arr_review_text
                    arr_result['rating_score'] = arr_scores
                    arr_result['confidence_score'] = arr_confidence_score
                    s += int(arr_confidence_score[0])
                    confidence_count[int(arr_confidence_score[0])] += 1
                    arr_score = re.findall('\d+', arr_scores)
                    score_count[int(arr_score[0])][int(arr_confidence_score[0])] += 1
                    arr_final_review.append(arr_result)
            f.close()
        print(accept)
        print(reject)
        print('arr:',s/len(arr_final_review))
        s = 0
    if li == 'COLING2020':
        coling_file_dir = './dataset/' + li + '/data'
        coling_second_list = os.listdir(coling_file_dir)
        coling_second_list.remove('LICENSE.txt')
        coling_second_list.remove('meta.json')
        #print(len(coling_second_list))
        for coling_revlist in coling_second_list:

            coling_meta_file = coling_file_dir + '/' + coling_revlist + '/v1/' + 'meta.json'
            coling_review_file = coling_file_dir + '/' + coling_revlist + '/v1/' + 'reviews.json'
            with open(coling_meta_file) as fp:
                coling_meta = json.load(fp)
                try:
                    coling_decision = coling_meta['status']
                    if 'Accept' in coling_decision:
                        accept = accept + 1
                    else:
                        reject = reject + 1
                except:
                    coling_decision = 'Accept'
                    accept = accept + 1
            fp.close()
            with open(coling_review_file) as f:
                coling_rev = json.load(f)
                for coling_text in coling_rev:
                    coling_result = {}
                    coling_review_text = coling_text['report']['main']
                    coling_scores = coling_text['scores']['overall']
                    coling_confidence_score = coling_text['meta']['REVIEWER_CONFIDENCE']
                    ff = preprocess_text(coling_review_text)
                    coling_w.append(len(word_tokenize(ff)))
                    coling_s.append(len(sent_tokenize(ff)))
                    coling_result['decision'] = coling_decision
                    coling_result['review_text'] = coling_review_text
                    coling_result['rating_score'] = coling_scores
                    coling_result['confidence_score'] = coling_confidence_score
                    s += int(coling_confidence_score[0])
                    confidence_count[int(coling_confidence_score[0])] += 1
                    coling_score = re.findall('\d+', coling_scores)
                    score_count[int(coling_score[0])][int(coling_confidence_score[0])] += 1
                    coling_final_review.append(coling_result)
            f.close()
        print(accept)
        print(reject)
        print('coling:', s / len(coling_final_review))
        s = 0
    if li == 'PeerRead-ACL2017':
        acl_file_dir = './dataset/' + li + '/data'
        acl_second_list = os.listdir(acl_file_dir)
        acl_second_list.remove('LICENSE.txt')
        acl_second_list.remove('meta.json')
        #(len(acl_second_list))
        for acl_revlist in acl_second_list:

            acl_review_file = acl_file_dir + '/' + acl_revlist + '/v1/' + 'reviews.json'
            acl_de = os.listdir(acl_file_dir + '/' + acl_revlist)
            if 'v2' in acl_de:
                acl_decision = 'Accept'
                accept = accept + 1
            else:
                acl_decision = 'Reject'
                reject = reject + 1
            with open(acl_review_file) as f:
                acl_rev = json.load(f)
                for acl_text in acl_rev:
                    acl_result = {}
                    acl_review_text = acl_text['report']['main']
                    acl_scores = acl_text['scores']['overall']
                    acl_confidence_score = acl_text['meta']['REVIEWER_CONFIDENCE']
                    acl_result['decision'] = acl_decision
                    fff = preprocess_text(acl_review_text)
                    acl_s.append(len(sent_tokenize(fff)))
                    acl_w.append(len(word_tokenize(fff)))

                    acl_result['review_text'] = acl_review_text
                    acl_result['rating_score'] = acl_scores
                    acl_result['confidence_score'] = acl_confidence_score
                    s += int(acl_confidence_score[0])
                    confidence_count[int(acl_confidence_score[0])] += 1
                    acl_score = re.findall('\d+', acl_scores)
                    score_count[int(acl_score[0])][int(acl_confidence_score[0])] += 1
                    acl_final_review.append(acl_result)
            f.close()
        print(accept)
        print(reject)
        print('acl:', s / len(acl_final_review))
        s = 0
    if li == 'PeerRead-CONLL2016':
        conll_file_dir = './dataset/' + li + '/data'
        conll_second_list = os.listdir(conll_file_dir)
        conll_second_list.remove('LICENSE.txt')
        conll_second_list.remove('meta.json')
        #print(len(conll_second_list))
        for conll_revlist in conll_second_list:
            conll_result = {}
            conll_review_file = conll_file_dir + '/' + conll_revlist + '/v1/' + 'reviews.json'
            conll_de = os.listdir(conll_file_dir + '/' + conll_revlist)
            if 'v2' in conll_de:
                conll_decision = 'Accept'
                accept = accept + 1
            else:
                conll_decision = 'Reject'
                reject = reject + 1
            with open(conll_review_file) as f:
                conll_rev = json.load(f)
                for conll_text in conll_rev:
                    conll_result = {}
                    conll_review_text = conll_text['report']['main']
                    conll_scores = conll_text['scores']['overall']
                    conll_confidence_score = conll_text['meta']['REVIEWER_CONFIDENCE']
                    conll_result['decision'] = conll_decision
                    fff = preprocess_text(conll_review_text)
                    conll_s.append(len(sent_tokenize(fff)))
                    conll_w.append(len(word_tokenize(fff)))

                    conll_result['review_text'] = conll_review_text
                    conll_result['rating_score'] = conll_scores
                    conll_result['confidence_score'] = conll_confidence_score
                    s += int(conll_confidence_score[0])
                    confidence_count[int(conll_confidence_score[0])] += 1
                    conll_score = re.findall('\d+', conll_scores)
                    score_count[int(conll_score[0])][int(conll_confidence_score[0])] += 1
                    conll_final_review.append(conll_result)
            f.close()
        print(accept)
        print(reject)
        print('conll:', s / len(conll_final_review))
        s = 0
    if li == 'ICLR_2017':
        iclr_2017_file_dir = './dataset/' + li + '/ICLR_2017_review'
        iclr_2017_dec_dir = './dataset/' + li + '/ICLR_2017_paper'
        iclr_2017_second_list = os.listdir(iclr_2017_file_dir)
        #print(len(iclr_2017_second_list))
        for iclr_2017_file in iclr_2017_second_list:
            iclr_2017_review_file = iclr_2017_file_dir + '/' + iclr_2017_file
            iclr_2017_dec = iclr_2017_file.replace('review', 'paper')
            iclr_2017_paper_file = iclr_2017_dec_dir + '/' + iclr_2017_dec
            try:
                with open(iclr_2017_paper_file) as fp:
                    iclr_2017_paper = json.load(fp)
                    iclr_2017_decision = iclr_2017_paper['decision']
                    if 'Accept' in iclr_2017_decision:
                        accept = accept + 1
                    else:
                        reject = reject + 1
            except:
                iclr_2017_decision = 'Accept'
                accept = accept + 1
                print(iclr_2017_paper_file)
            with open(iclr_2017_review_file) as f:
                iclr_2017_rev = json.load(f)
                iclr_2017_rev_dir = iclr_2017_rev['reviews']
                for iclr_2017_text in iclr_2017_rev_dir:
                    iclr_2017_text['decision'] = iclr_2017_decision
                    ff = preprocess_text(iclr_2017_text['review'])
                    iclr_2017_w.append(len(word_tokenize(ff)))
                    iclr_2017_s.append(len(sent_tokenize(ff)))
                    s += int(iclr_2017_text['confidence'][0])
                    confidence_count[int(iclr_2017_text['confidence'][0])] += 1
                    iclr_2017_score = re.findall('\d+', iclr_2017_text['rating'])
                    score_count[int(iclr_2017_score[0])][int(iclr_2017_text['confidence'][0])] += 1
                    iclr_2017_final_review.append(iclr_2017_text)
        print(accept)
        print(reject)
        print('iclr_2017:', s / len(iclr_2017_final_review))
        s = 0
    if li == 'ICLR_2018':
        iclr_2018_file_dir = './dataset/' + li + '/ICLR_2018_review'
        iclr_2018_dec_dir = './dataset/' + li + '/ICLR_2018_paper'
        iclr_2018_second_list = os.listdir(iclr_2018_file_dir)
        #print(len(iclr_2018_second_list))
        for iclr_2018_file in iclr_2018_second_list:
            iclr_2018_review_file = iclr_2018_file_dir + '/' + iclr_2018_file
            iclr_2018_dec = iclr_2018_file.replace('review', 'paper')
            iclr_2018_paper_file = iclr_2018_dec_dir + '/' + iclr_2018_dec
            with open(iclr_2018_paper_file) as fp:
                iclr_2018_paper = json.load(fp)
                iclr_2018_decision = iclr_2018_paper['decision']
                if 'Accept' in iclr_2018_decision:
                    accept = accept + 1
                else:
                    reject = reject + 1
            with open(iclr_2018_review_file) as f:
                iclr_2018_rev = json.load(f)
                iclr_2018_rev_dir = iclr_2018_rev['reviews']
                for iclr_2018_text in iclr_2018_rev_dir:
                    iclr_2018_text['decision'] = iclr_2018_decision
                    ff = preprocess_text(iclr_2018_text['review'])
                    iclr_2018_w.append(len(word_tokenize(ff)))
                    iclr_2018_s.append(len(sent_tokenize(ff)))
                    s += int(iclr_2018_text['confidence'][0])
                    confidence_count[int(iclr_2018_text['confidence'][0])] += 1
                    iclr_2018_score = re.findall('\d+', iclr_2018_text['rating'])
                    score_count[int(iclr_2018_score[0])][int(iclr_2018_text['confidence'][0])] += 1
                    iclr_2018_final_review.append(iclr_2018_text)

        print(accept)
        print(reject)
        print('iclr_2018:', s / len(iclr_2018_final_review))
        s = 0
    if li == 'ICLR_2019':
        iclr_2019_file_dir = './dataset/' + li + '/ICLR_2019_review'
        iclr_2019_dec_dir = './dataset/' + li + '/ICLR_2019_paper'
        iclr_2019_second_list = os.listdir(iclr_2019_file_dir)
        #print(len(iclr_2019_second_list))
        for iclr_2019_file in iclr_2019_second_list:
            iclr_2019_review_file = iclr_2019_file_dir + '/' + iclr_2019_file
            iclr_2019_dec = iclr_2019_file.replace('review', 'paper')
            iclr_2019_paper_file = iclr_2019_dec_dir + '/' + iclr_2019_dec
            with open(iclr_2019_paper_file) as fp:
                iclr_2019_paper = json.load(fp)
                iclr_2019_decision = iclr_2019_paper['decision']
                if 'Accept' in iclr_2019_decision:
                    accept = accept + 1
                else:
                    reject = reject + 1
            with open(iclr_2019_review_file) as f:
                iclr_2019_rev = json.load(f)
                iclr_2019_rev_dir = iclr_2019_rev['reviews']
                for iclr_2019_text in iclr_2019_rev_dir:
                    iclr_2019_text['decision'] = iclr_2019_decision
                    ff = preprocess_text(iclr_2019_text['review'])
                    iclr_2019_w.append(len(word_tokenize(ff)))
                    iclr_2019_s.append(len(sent_tokenize(ff)))
                    s+=int(iclr_2019_text['confidence'][0])
                    confidence_count[int(iclr_2019_text['confidence'][0])] += 1
                    iclr_2019_score = re.findall('\d+', iclr_2019_text['rating'])

                    score_count[int(iclr_2019_score[0])][int(iclr_2019_text['confidence'][0])] += 1
                    iclr_2019_final_review.append(iclr_2019_text)
        print(accept)
        print(reject)
        print('iclr_2019:', s / len(iclr_2019_final_review))
        s = 0
iclr_2021_list = os.listdir('ICLR_2021')
for iclr_2021_li in iclr_2021_list:
    iclr_2021_rev_list = os.listdir('ICLR_2021/' + iclr_2021_li)
    #print(len(iclr_2021_rev_list))
    for iclr_2021_rev_file in iclr_2021_rev_list:
        iclr_2021_rev_dir = 'ICLR_2021/' + iclr_2021_li + '/' + iclr_2021_rev_file
        with open(iclr_2021_rev_dir) as f:
            iclr_2021_rev = json.load(f)
            iclr_2021_review = iclr_2021_rev['reviews']
            iclr_2021_decision = iclr_2021_rev['Decision:']
            if 'Accept' in iclr_2021_decision:
                accept = accept + 1
            else:
                reject = reject + 1
            for iclr_2021_rev_text in iclr_2021_review:
                iclr_2021_rev_text['decision'] = iclr_2021_rev['Decision:']
                confidence_count[int(iclr_2021_rev_text['confidence_score'][0])] += 1
                iclr_2021_score = re.findall('\d+', iclr_2021_rev_text['rating_score'])
                ff = preprocess_text(iclr_2021_rev_text['review_text'])
                iclr_2021_w.append(len(word_tokenize(ff)))
                iclr_2021_s.append(len(sent_tokenize(ff)))
                s+=int(iclr_2021_rev_text['confidence_score'][0])
                score_count[int(iclr_2021_score[0])][int(iclr_2021_rev_text['confidence_score'][0])] += 1
                iclr_2021_final_review.append(iclr_2021_rev_text)
print(accept)
print(reject)
print('iclr_2021:', s / len(iclr_2021_final_review))
s = 0
iclr_2022_list = os.listdir('ICLR_2022')
error_list = []
for iclr_2022_li in iclr_2022_list:
    iclr_2022_rev_list = os.listdir('ICLR_2022/' + iclr_2022_li)
    #print(len(iclr_2022_rev_list))
    for iclr_2022_rev_file in iclr_2022_rev_list:
        iclr_2022_rev_dir = 'ICLR_2022/' + iclr_2022_li + '/' + iclr_2022_rev_file

        with open(iclr_2022_rev_dir) as f:
            iclr_2022_rev = json.load(f)
            iclr_2022_review = iclr_2022_rev['reviews']
            iclr_2022_decision = iclr_2022_rev['Decision:']
            if 'Accept' in iclr_2022_decision:
                accept = accept + 1
            else:
                reject = reject + 1
            for iclr_2022_rev_text in iclr_2022_review:
                iclr_2022_result = {}
                iclr_2022_result['decision'] = iclr_2022_rev['Decision:']
                iclr_2022_result['review_text'] = iclr_2022_rev_text['review_text']
                ff = preprocess_text(iclr_2022_rev_text['review_text'])
                iclr_2022_w.append(len(word_tokenize(ff)))
                iclr_2022_s.append(len(sent_tokenize(ff)))
                iclr_2022_result['rating_score'] = iclr_2022_rev_text['rating_score']
                iclr_2022_result['confidence_score'] = iclr_2022_rev_text['confidence_score']
                s += int(iclr_2022_rev_text['confidence_score'][0])
                confidence_count[int(iclr_2022_rev_text['confidence_score'][0])] += 1
                try:
                    iclr_2022_score = re.findall('\d+', iclr_2022_rev_text['rating_score'])
                    score_count[int(iclr_2022_score[0])][int(iclr_2022_rev_text['confidence_score'][0])] += 1
                except:
                    error_list.append(iclr_2022_li + '#' +iclr_2022_rev_file)
                iclr_2022_final_review.append(iclr_2022_result)
# with open('error.txt', 'w') as f:
#     for r in error_list:
#         f.writelines(r + '\n')
# print('total review number:' + str(len(iclr_2021_final_review) + len(iclr_2022_final_review) + len(iclr_2018_final_review) + len(iclr_2017_final_review) + len(iclr_2019_final_review) + len(acl_final_review) + len(arr_final_review) + len(coling_final_review) + len(conll_final_review)))
# for x in range(10):
#     for y in range(5):
#         if score_count[x][y] == 0:
#             continue
#         l = 'score:' + str(x) + '-' + 'confidence:' + str(y)
#         print('\n' + l + 'total:' + str(score_count[x][y]))
print(accept)
print(reject)
print('iclr_2022:', s / len(iclr_2022_final_review))
s = 0
print(np.sum(confidence_count))
print('paper number:' + str(accept + reject))
print('accept paper number:' + str(accept))
print('reject paper number:' + str(reject))
print(sum(arr_w)/len(arr_w),sum(arr_s)/len(arr_s))
print(sum(acl_w)/len(acl_w),sum(acl_s)/len(acl_s))
print(sum(conll_w)/len(conll_w),sum(conll_s)/len(conll_s))
print(sum(coling_w)/len(coling_w),sum(coling_s)/len(coling_s))
print(sum(iclr_2017_w)/len(iclr_2017_w),sum(iclr_2017_s)/len(iclr_2017_s))
print(sum(iclr_2018_w)/len(iclr_2018_w),sum(iclr_2018_s)/len(iclr_2018_s))
print(sum(iclr_2019_w)/len(iclr_2019_w),sum(iclr_2019_s)/len(iclr_2019_s))
print(sum(iclr_2021_w)/len(iclr_2021_w),sum(iclr_2021_s)/len(iclr_2021_s))
print(sum(iclr_2022_w)/len(iclr_2022_w),sum(iclr_2022_s)/len(iclr_2022_s))
# np.savetxt('score_count.txt', score_count, fmt='%d', delimiter=',')
# if os.path.exists('./final_dataset'):
#     pass
# else:
#     os.makedirs('./final_dataset')
#
# with open('final_dataset/arr_data.json', 'w') as f:
#     json.dump(arr_final_review, f)
#     f.close()
# with open('final_dataset/coling_data.json', 'w') as f:
#     json.dump(coling_final_review, f)
#     f.close()
# with open('final_dataset/conll_data.json', 'w') as f:
#     json.dump(conll_final_review, f)
#     f.close()
# with open('final_dataset/acl_data.json', 'w') as f:
#     json.dump(acl_final_review, f)
#     f.close()
# with open('final_dataset/iclr_2017_data.json', 'w') as f:
#     json.dump(iclr_2017_final_review, f)
#     f.close()
# with open('final_dataset/iclr_2018_data.json', 'w') as f:
#     json.dump(iclr_2018_final_review, f)
#     f.close()
# with open('final_dataset/iclr_2019_data.json', 'w') as f:
#     json.dump(iclr_2019_final_review, f)
#     f.close()
# with open('final_dataset/iclr_2021_data.json', 'w') as f:
#     json.dump(iclr_2021_final_review, f)
#     f.close()
# with open('final_dataset/iclr_2022_data.json', 'w') as f:
#     json.dump(iclr_2022_final_review, f)
#     f.close()
