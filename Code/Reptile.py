from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import re
import json
#service = Service(executable_path='chromedriver.exe')
def crawler(url):
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    time.sleep(4)
    k = browser.find_elements(By.CLASS_NAME, "note_content_field")

    title = []
    for x in k:
        #print(x.text)
        title.append(x.text)
    v = browser.find_elements(By.CLASS_NAME, "note_content_value")
    text = []
    for m in v:
        #print(m.text)
        text.append(m.text)
    #print(title, text)
    dict = {key: value for key, value in zip(title, text)}
    return dict
train_list = {}
dev_list = {}
test_list = {}
with open('train.txt', encoding='utf-8') as f:
    train_file = f.readlines()
    for x in train_file:
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
        url = re.findall(pattern, x)[0]
        train_dict = crawler(url)
        file_name = x.replace(url, '').strip()
        if 'Recommendation:' in train_dict:
            train_list[file_name] = train_dict['Recommendation:']
        elif 'Decision:' in train_dict:
            train_list[file_name] = train_dict['Decision:']
        else:
            train_list[file_name] = 'None'
with open('dev.txt', encoding='utf-8') as f:
    dev_file = f.readlines()
    for x in dev_file:
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
        url = re.findall(pattern, x)[0]
        dev_dict = crawler(url)
        file_name = x.replace(url, '').strip()
        if 'Recommendation:' in dev_dict:
            dev_list[file_name] = dev_dict['Recommendation:']
        elif 'Decision:' in dev_dict:
            dev_list[file_name] = dev_dict['Decision:']
        else:
            dev_list[file_name] = 'None'
        #dev_list.append(dev_dict)
with open('test.txt', encoding='utf-8') as f:
    test_file = f.readlines()
    for x in test_file:
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
        url = re.findall(pattern, x)[0]
        test_dict = crawler(url)
        file_name = x.replace(url, '').strip()
        #test_list[file_name] = test_dict['Recommendation:']
        if 'Recommendation:' in test_dict:
            test_list[file_name] = test_dict['Recommendation:']
        elif 'Decision:' in test_dict:
            test_list[file_name] = test_dict['Decision:']
        else:
            test_list[file_name] = 'None'
        #test_list.append(test_dict)
fp = open('train_result.txt', "w")
for k, v in train_list.items():
    fp.writelines(k)
    fp.writelines(' '+ v)
    fp.writelines('\n')
fp.close()
fp = open('dev_result.txt', "w")
for k, v in dev_list.items():
    fp.writelines(k)
    fp.writelines(' '+ v)
    fp.writelines('\n')
fp.close()
fp = open('test_result.txt', "w")
for k, v in test_list.items():
    fp.writelines(k)
    fp.writelines(' '+ v)
    fp.writelines('\n')
fp.close()

print(train_list,dev_list,test_list)