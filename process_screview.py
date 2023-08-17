import json
import string
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

#from text_reptile import reptile_2021, reptile_2022
with open('2021_withdrawn-rejected-submissions.txt', encoding='utf-8') as f:
    i = 0
    for x in f:
        if '#' in x:
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get(x[1:].strip('\n'))
            time.sleep(4)
            k = browser.find_elements(By.CLASS_NAME, "note_content_field")
            title = []
            decision_num = 0
            for n in range(len(k)):
                # print(x.text)
                if 'Review:' in k[n].text:
                    title.append(n)
                elif 'Decision:' in k[n].text:
                    decision_num = n
                # title.append(x.text)
            v = browser.find_elements(By.CLASS_NAME, "note_content_value")
            reviews = []
            if len(title) == 0:
                print('no review')
            for m in title:
                review = {}
                review_text = v[m].text
                rating_score = v[m + 1].text
                confidence_score = v[m + 2].text
                review['review_text'] = review_text
                review['rating_score'] = rating_score
                review['confidence_score'] = confidence_score
                reviews.append(review)
            # print(title, text)
            result_dic = {}
            ids = str(i) + '_review'
            result_dic['ids'] = ids
            result_dic['Decision:'] = v[decision_num].text
            result_dic['reviews'] = reviews

            write_file_name = './ICLR_2021/' + '2021_withdrawn-rejected-submissions' + '/' + str(i) + '.json'
            with open(write_file_name, 'w') as fp:
                json.dump(result_dic, fp)
            print(ids + ' wrote down')
        i = i + 1