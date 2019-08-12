'''
    Author: Monty
    Date: 2019-08-08
    Version: 1.0
    Function: 爬取拉勾网上的指定职位信息，保存为json格式
'''

import requests
import json
import time


url_index = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput='

url_position = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

session = requests.Session()

r = session.get(url_index, headers=headers)

cookies = r.cookies

position_info = []
keys = ['city', 'companyFullName', 'companyId', 'companyLabelList', 'companyShortName', 'companySize',
        'district', 'education', 'financeStage', 'industryField', 'industryLables', 'positionAdvantage',
        'positionId', 'positionLables', 'positionName', 'salary', 'skillLables', 'workYear']

for page in range(1,31):
    data = {'first': 'true',
    'pn': page,
    'kd': '数据分析'}

    res = session.post(url_position, headers=headers, data=data, cookies=cookies)

    time.sleep(30)

    content = json.loads(res.text)

    result = content['content']['positionResult']['result']

    print('正在爬取第{}页'.format(page))

    for i in range(15):
        info = dict((key, value) for key, value in result[i].items() if key in keys)
        position_info.append(info)

path = './Download/拉钩网职位数据.json'

with open(path, 'w', encoding='utf-8') as f:
    json.dump(position_info, f, ensure_ascii=False)


