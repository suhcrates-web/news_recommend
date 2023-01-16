from database import cursor, db
import codecs
from konlpy.tag import Kkma, Komoran, Okt


okt = Okt()

cursor.execute(
    """
    select article from news_stuffs.naver_news_test
    """
)

temp =[codecs.decode(i[0], 'utf-8') for i in cursor.fetchall()]


all_sample =[[i[:-5] for i in okt.pos(sample_list, norm=True, join=True) if i[-4:] =='Noun'] for sample_list in temp]

print(all_sample)
# for sample_list in temp:
#     parsed = okt.pos(sample_list, norm=True, join=True)
#     all_sample.append([i[:-5] for i in parsed if i[-4:] =='Noun'])
# print(all_sample)