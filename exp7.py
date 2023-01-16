import mysql.connector
from collections import Counter
import numpy as np
import json

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
for ip0, vec0 in  cursor.fetchall():
    if vec0 ==None:
        vec0 = np.zeros(50)
    else:
        vec0 = np.array(json.loads(vec0))
    vec_dic[ip0] = vec0

print(vec_dic.keys())