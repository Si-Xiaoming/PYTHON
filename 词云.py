from PIL import Image
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
import numpy as np
text=open("./2020214.txt",encoding='utf-8').read()
text=text.replace('\n',"").replace("\u3000","") #替换掉换行符和空格
text_cut=jieba.lcut(text)#分词，返回词的列表
text_join=' '.join(text_cut) #将分好的词用‘ ’隔开连成字符串

stop_word=open("./stopword.txt",encoding='utf-8').read().split('\n')
background=Image.open("./back.png")
graph=np.array(background)
word_cloud=WordCloud(scale=12,
                    font_path='C:\Windows\Fonts\STXINGKA.ttf',
                     background_color='white',
                     mask=graph,
                     #min_font_size=9,
                      width=1000,
                       height=800,
                     stopwords=stop_word)
word_cloud.generate(text_join)
plt.subplots(figsize=(12,8))
plt.imshow(word_cloud)
plt.axis("off")
word_cloud.to_file("a.png")
