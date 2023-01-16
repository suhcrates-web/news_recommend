from flask import Flask, render_template, url_for, request, redirect, jsonify
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import mysql.connector
import binascii, codecs
import time
import mysql.connector
import requests
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import gensim
import gensim.downloader as api
import json
from database import cursor, db
import codecs
from konlpy.tag import Kkma, Komoran, Okt
import numpy as np
from collections import Counter

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


def find_10(gijun_array):
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
    return html0


@app.route('/', methods=['get'])
def main0():
    ## ip 고유 번호
    ip = request.remote_addr

    config = {
        'user': 'root',
        'password': 'Seoseoseo7!',
        'host': 'localhost',
        'port': '3306'
    }
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    cursor.execute(
        """
        select ip, vec from news_stuffs.ip_vector
        """
    )

    vec_dic = Counter()
    for ip0, vec0 in cursor.fetchall():
        if vec0 == None:
            vec0 = np.zeros(50)
        else:
            vec0 = np.array(json.loads(vec0))
        vec_dic[ip0] = vec0

    if ip in vec_dic.keys():
        vec_send = vec_dic[ip]
    else:
        cursor.execute(
            f"""
            insert into news_stuffs.ip_vector values("{ip}","{list(np.zeros(50))}")
            
            """
        )
        db.commit()
        vec_send = np.zeros(50)

    objs = []
    ran0 = np.random.rand(50)
    title_10 = find_10(ran0)
    for num in range(len(titles)):
        objs.append({
            'title': titles[num],
            'date' : time0[num],
            'num0' : num
        })
    return render_template('bot_v3.html', objs=objs, top10= title_10, vec= vec_send.round(4), ip=ip)


@app.route('/repl', methods=['POST', 'GET'])
def read_article():
    if request.method == 'POST':

        num0 = int(request.form['ind'])
        vec_article = vectors[num0]

        ip = request.remote_addr
        config = {
            'user': 'root',
            'password': 'Seoseoseo7!',
            'host': 'localhost',
            'port': '3306'
        }
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        cursor.execute(
            f"""
            select vec from news_stuffs.ip_vector where ip = "{ip}"
            """
        )
        vec_user = np.array(json.loads(cursor.fetchall()[0][0]))

        p = 0.3
        vec_user = (1-p) * vec_article + p * vec_user

        top10 = find_10(vec_user)

        cursor.execute(
            f"""
            update news_stuffs.ip_vector set vec = "{list(vec_user)}" where ip="{ip}"
            """)
        db.commit()


        return {'vec_article':list(vec_article.round(2)), 'vec_user':list(vec_user.round(2)), 'top10':top10}
        # return render_template('vec.html', vec_article=vectors[num0].round(4))


#
# ## 요약작성 ##
# @app.route('/donga/dangbun/naver/write', methods = ['POST','GET'])
# def write():
#     if request.method == 'POST':
#         url = request.form['url']
#         press = request.form['press']
#         title = request.form['title']
#         ind = request.form['ind']
#         lead = giveme_lead(url, press, ind)
#         if '[속보]' in title:
#             text = f"@{press}/{title} {url}"
#         else:
#             text = f"@{press}/{title} = {lead} {url}"
#         return text
#
#
# ##실수로 들어왔을때 ##
# @app.route('/donga/dangbun/', methods = ['POST','GET'])
# def mistake_2_1():
#     return redirect('http://testbot.ddns.net:5234/donga/dangbun/')


if __name__ == "__main__":
    # serve(app, host = '0.0.0.0', port = '3389', threads=1)
    with open('C:/stamp/port.txt', 'r') as f:
        port = f.read().split(',')[0]  # 노트북 5232, 데스크탑 5231
        # port = port[0]
    # print(port)
    # host = '0.0.0.0'
    if port == '5232':
        port ='5235'
        host = '172.30.1.58'
        host = '0.0.0.0'

    elif port == '5231':
        port = '5235'
        host = '0.0.0.0'
    # port = 5233
    # 172.30.1.53
    # 0.0.0.0
    app.run(host=host, port=port, debug=True)
