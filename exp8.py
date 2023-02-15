from flask import Flask, render_template, url_for, request, redirect, jsonify
import time
import json
from database import cursor, db
import codecs
from konlpy.tag import Kkma, Komoran, Okt
import numpy as np
from collections import Counter
import timeit

app = Flask(__name__)
cursor.execute(
    """
    select uri, article, title, cv_p, createDate, vectors from news_stuffs.naver_news_test
    """
)

uris = []
temp = []
titles = []
cv_ps = []
time0 = []
vectors = []
for uri, article, title, cv_p, date0, vector in cursor.fetchall():
    if uri not in uris:
        uris.append(uri)
        temp.append(codecs.decode(article, 'utf-8'))
        titles.append(title)
        cv_ps.append(cv_p)
        time0.append(date0)
        vectors.append(np.array(json.loads(vector)[0]))

okt = Okt()

vectors_mat = np.array(vectors)

def find_10(gijun_array):
    start = timeit.default_timer()
    points = Counter()
    titles_10 = []
    for num0, bigyo in enumerate(vectors):
        point = np.dot(gijun_array, bigyo)
        points[num0] = point

    top10 = points.most_common(10)
    html0 = ""
    for num, _ in top10:
        html0 += '#' +titles[num] + "<BR>"
        # titles_10.append(titles[num])
    end = timeit.default_timer()
    print(f"걸린 시간 : {end-start}")

    return html0

def find_10_alt(gijun_array):
    start = timeit.default_timer()
    points = Counter()
    titles_10 = []

    points = np.matmul(vectors_mat, gijun_array)
    top10 = np.argsort(points)[::-1][:10]

    html0 = ""
    for num in top10:
        html0 += '#' +titles[num] + "<BR>"
        # titles_10.append(titles[num])
    end = timeit.default_timer()
    print(f"걸린 시간 : {end-start}")

    return html0

v0 = np.array([-2.58,1.98,-0.35,0.09,0.32,-2.97,1.86,0.25,-2.62,3.6,-0.14,1.9,-2.59,0.32,-1.41,2.26,-2.13,-0.26,0.11,0.02,-0.22,-3.43,0.92,-2.24,0.21,0.43,2.67,-1.65,-1.94,-0.27,0.27,1.62,2.34,1.03,0.3,3,-1.23,-2.75,2.39,-0.69,0.9,0.41,-2.21,-4.9,1.93,-5.57,-0.36,-3.52,3.58,1.61])
print(find_10(v0))
print(find_10_alt(v0))
