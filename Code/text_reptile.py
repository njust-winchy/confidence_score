from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import json
from itertools import groupby
def reptile_2021(url, file_name, count):
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    time.sleep(4)
    k = browser.find_elements(By.CLASS_NAME, "note_content_field")
    title = []
    decision_num = 0
    for n in range(len(k)):
        #print(x.text)
        if 'Review:' in k[n].text:
            title.append(n)
        elif 'Decision:' in k[n].text:
            decision_num = n
        #title.append(x.text)
    v = browser.find_elements(By.CLASS_NAME, "note_content_value")
    reviews = []
    if len(title) == 0:
        print(file_name[0:-4] + 'no review')
        return
    for m in title:
        review = {}
        review_text = v[m].text
        rating_score = v[m+1].text
        confidence_score = v[m+2].text
        review['review_text'] = review_text
        review['rating_score'] = rating_score
        review['confidence_score'] = confidence_score
        reviews.append(review)
    #print(title, text)
    result_dic = {}
    ids = str(count) + '_review'
    result_dic['ids'] = ids
    result_dic['Decision:'] = v[decision_num].text
    result_dic['reviews'] = reviews
    if os.path.exists('./ICLR_2021/' + file_name[0:-4]):
        pass
    else:
        os.makedirs('./ICLR_2021/' + file_name[0:-4])
    write_file_name = './ICLR_2021/' + file_name[0:-4] + '/' + str(count) + '.json'
    with open(write_file_name, 'w') as fp:
        json.dump(result_dic, fp)
    print(ids + ' wrote down')


def reptile_2022(url, file_name, count):
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    time.sleep(4)
    k = browser.find_elements(By.CLASS_NAME, "note_content_field")
    title = []
    decision_num = 0
    decision = 'None'
    for y in range(len(k)):
        if 'Summary Of The Paper:' in k[y].text:
            title.append(y)
        elif 'Main Review:' in k[y].text:
            title.append(y)
        elif 'Summary Of The Review:' in k[y].text:
            title.append(y)
        elif 'Recommendation:' in k[y].text:
            title.append(y)
        elif 'Confidence:' in k[y].text:
            title.append(y)
        if 'Decision:' in k[y].text:
            decision_num = y
        else:
            decision = 'Reject'
        #title.append(x.text)
    v = browser.find_elements(By.CLASS_NAME, "note_content_value")
    reviews = []
    if len(title) == 0:
        print(file_name[0:-4] + 'no review')
        return
    for m in range(len(title)//4 - 1):
        review = {}
        m = m * 5
        review_text = v[title[m]].text + v[title[m+1]].text + v[title[m+2]].text
        rating_score = v[title[m+3]].text
        confidence_score = v[title[m+4]].text
        review['review_text'] = review_text
        review['rating_score'] = rating_score
        review['confidence_score'] = confidence_score
        reviews.append(review)
        #print(title, text)
    result_dic = {}
    ids = str(count) + '_review'
    result_dic['ids'] = ids
    if decision == 'None':
        result_dic['Decision:'] = v[decision_num].text
    else:
        result_dic['Decision:'] = decision
    result_dic['reviews'] = reviews
    if os.path.exists('./ICLR_2022/' + file_name[0:-4]):
        pass
    else:
        os.makedirs('./ICLR_2022/' + file_name[0:-4])
    write_file_name = './ICLR_2022/' + file_name[0:-4] + '/' + str(count) + '.json'
    with open(write_file_name, 'w') as fp:
        json.dump(result_dic, fp)
    print(ids + ' wrote down')

open_list_2021 = ['2021_oral-presentations.txt', '2021_poster-presentations.txt', '2021_spotlight-presentations.txt', '2021_withdrawn-rejected-submissions.txt']
#open_list_2022 = ['2022_oral-submissions.txt', '2022_spotlight-submissions.txt', '2022_poster-submissions.txt', '2022_submitted-submissions.txt', '2022_desk-rejected-withdrawn-submissions.txt']
open_list_2022 = ['2022_oral-submissions.txt', '2022_spotlight-submissions.txt', '2022_poster-submissions.txt', '2022_submitted-submissions.txt']
# for file_name in open_list_2021:
#     url_list_2021 = []
#     with open(file_name, encoding='utf-8') as f:
#         for x in f:
#             url_list_2021.append(x.strip('\n'))
#     for num in range(len(url_list_2021)):
#         url = url_list_2021[num]
#         #print(file_name[0:-4])
#         reptile_2021(url, file_name, num)
#     print(file_name + 'finished')
#
# for file_name in open_list_2022:
#     url_list_2022 = []
#     with open(file_name, encoding='utf-8') as f:
#         for x in f:
#             url_list_2022.append(x.strip('\n'))
#     for num in range(len(url_list_2022)):
#         url = url_list_2022[num]
#         #print(file_name[0:-4])
#         reptile_2022(url, file_name, num)
#     print(file_name + 'finished')
oral_l = []
spotlight_l = []
poster_l = []
submitted_l = []
for file_name in open_list_2022:
    url_list_2022 = []
    if 'oral-submissions' in file_name:
        with open(file_name, encoding='utf-8') as f:
            for x in f:
                oral_l.append(x.strip('\n'))
    elif 'spotlight-submissions' in file_name:
        with open(file_name, encoding='utf-8') as f:
            for x in f:
                spotlight_l.append(x.strip('\n'))
    elif 'poster-submissions' in file_name:
        with open(file_name, encoding='utf-8') as f:
            for x in f:
                poster_l.append(x.strip('\n'))
    elif 'submitted-submissions' in file_name:
        with open(file_name, encoding='utf-8') as f:
            for x in f:
                submitted_l.append(x.strip('\n'))


with open('error.txt', encoding='utf-8') as fp:
    err_list = []
    for t in fp:
        text = t.strip('\n')
        if text not in err_list:
            err_list.append(text)
    for m in err_list:
        if 'oral-submissions' in m:
            file = m.split('#')[1]
            ret = [''.join(list(g)) for k, g in groupby(file, key=lambda x: x.isdigit())][0]
            url = oral_l[int(ret)]
            os.remove('F:\code\confidence score-master\ICLR_2022\\2022_oral-submissions' + '\\' + file)
            reptile_2022(url, '2022_oral-submissions.txt', ret)
        elif 'spotlight-submissions' in m:
            file = m.split('#')[1]
            ret = [''.join(list(g)) for k, g in groupby(file, key=lambda x: x.isdigit())][0]
            url = spotlight_l[int(ret)]
            os.remove('F:\code\confidence score-master\ICLR_2022\\2022_spotlight-submissions' + '\\' + file)
            reptile_2022(url, '2022_spotlight-submissions.txt', ret)
        elif 'poster-submissions' in m:
            file = m.split('#')[1]
            ret = [''.join(list(g)) for k, g in groupby(file, key=lambda x: x.isdigit())][0]
            url = poster_l[int(ret)]
            os.remove('F:\code\confidence score-master\ICLR_2022\\2022_poster-submissions' + '\\' + file)
            reptile_2022(url, '2022_poster-submissions.txt', ret)
        elif 'submitted-submissions' in m:
            file = m.split('#')[1]
            ret = [''.join(list(g)) for k, g in groupby(file, key=lambda x: x.isdigit())][0]
            url = submitted_l[int(ret)]
            os.remove('F:\code\confidence score-master\ICLR_2022\\2022_submitted-submissions' + '\\' + file)
            reptile_2022(url, '2022_submitted-submissions.txt', ret)