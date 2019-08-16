'''
    Author: Monty
    Date: 2019-08-15
    Version: 1.0
    Function: 将从拉勾网下载的职位描述中的技术标签用词云展示
'''

from wordcloud import WordCloud
from wordcloud import STOPWORDS
from scipy.misc import imread
import re
import matplotlib.pyplot as plt

# 读取职位描述文本
with open('lagou_job_describe.txt', 'r', encoding='utf-8') as f:
    jd_text = f.read()


# 剔除原文本中的英文招聘，并不能完全去除，但是能去除大半
jd_text_no_English = re.sub(r'[a-zA-Z]+\s', '', jd_text, count=0)

# 提取文本中的技能标签，多表示为英文
pattern = re.compile(r'[a-zA-Z]+', re.S|re.I)
skillLabels_list = pattern.findall(jd_text)

# 把标签转换为字符串
skillLabels_text = ' '.join(skillLabels_list)

# 添加停用词
sw = set(STOPWORDS)
sw.add('banned') # 爬取失败的jd返回的是'banned'

# 添加蒙版
mask = imread('mask.png')

# 构建词云
wc = WordCloud(font_path='C:\\Windows\\Fonts\\msyh.ttf', stopwords=sw,
               background_color='white', mask=mask, collocations=False)
wc.generate(skillLabels_text)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('skillLabes_WordCloud.png')