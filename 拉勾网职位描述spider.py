'''
    Author: Monty
    Date: 2019-08-13
    Version: 1.0
    Function: 获取拉勾网上数据分析岗位的职位描述，并用词云展现出来
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

def get_JobDescribText(url, headers):
    '''获取职位描述文本'''
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        bs = BeautifulSoup(res.text, 'lxml')
        text = bs.find(class_='job-detail').text
        return text
    except:
        return 'banned'


def save_JobDescribText(path, text):
    '''把职位描述文本信息存到本地'''
    with open(path, mode='a', encoding='utf-8') as f:
        f.write(text)

def main():
    df = pd.read_json('Download/拉勾网职位数据.json', encoding='utf-8')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    path = 'Download\lagou_job_describe.txt'
    n = 1
    for id in df.positionId:
        url = 'https://www.lagou.com/jobs/{}.html'.format(id)
        text = get_JobDescribText(url, headers)
        time.sleep(10)
        save_JobDescribText(path, text)
        print('已完成{0}/450'.format(n))
        print('-----------{}-------------'.format(text[:20]))
        n += 1

if __name__ == '__main__':
    main()