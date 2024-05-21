from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import re
import requests


year_list = [2019, 2021, 2022]
ICLR_2019_list = ['poster-presentations', 'oral-presentations', 'withdrawn-rejected-submissions']
ICLR_2021_list = ['oral-presentations', 'spotlight-presentations', 'poster-presentations', 'withdrawn-rejected-submissions']
ICLR_2022_list = ['oral-submissions', 'spotlight-submissions', 'poster-submissions', 'submitted-submissions', 'desk-rejected-withdrawn-submissions']
for year in year_list:
    url = "https://openreview.net/group?id=ICLR.cc"
    url = url + '/' + str(year) + '/Conference'
    if year == 2019:
        for rev_name in ICLR_2019_list:
            url_list = []
            rev_url = url + '#' + rev_name
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get(rev_url)
            time.sleep(20)
            x = browser.find_elements(By.TAG_NAME, "a")
            for item in x:
                m = item.get_attribute('href')
                if "forum" in m:
                    url_list.append(m)
            file_name = str(year) + '_' +rev_name + '.txt'
            fp = open(file_name, "w")
            for paper_url in url_list:
                fp.writelines(paper_url)
                fp.writelines('\n')
            browser.quit()
            fp.close()
    if year == 2021:
        for rev_name in ICLR_2021_list:
            url_list = []
            rev_url = url + '#' + rev_name
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get(rev_url)
            time.sleep(20)
            x = browser.find_elements(By.TAG_NAME, "a")
            for item in x:
                m = item.get_attribute('href')
                if "forum" in m:
                    url_list.append(m)
            file_name = str(year) + '_' + rev_name + '.txt'
            fp = open(file_name, "w")
            for paper_url in url_list:
                fp.writelines(paper_url)
                fp.writelines('\n')
            browser.quit()
            fp.close()
    if year == 2022:
        for rev_name in ICLR_2022_list:
            url_list = []
            rev_url = url + '#' + rev_name
            browser = webdriver.Chrome('chromedriver.exe')
            browser.get(rev_url)
            time.sleep(20)
            x = browser.find_elements(By.TAG_NAME, "a")
            for item in x:
                m = item.get_attribute('href')
                if "forum" in m:
                    url_list.append(m)
            file_name = str(year) + '_' + rev_name + '.txt'
            fp = open(file_name, "w")
            for paper_url in url_list:
                fp.writelines(paper_url)
                fp.writelines('\n')
            browser.quit()
            fp.close()
