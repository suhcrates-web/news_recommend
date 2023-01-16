import requests
import json
from bs4 import BeautifulSoup
import time

url = 'https://news-stat-admin.navercorp.com/api/today?timeDimension=DATE&startDate=2023-01-14&section=total&device=TOTAL&channelMainTabType=ALL&_=1673680541938_61180'

headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,ru;q=0.6',
'Connection': 'keep-alive',
'Cookie': 'FRIEND.SES=iCWyXMKH84aK4pGLT55BAtz+fayk3JHYK74nBCxAGLvBbBtm+27P5blzuT4i00GUXNgKbxGM0B5Xtdqcc82/3JbC4SV3Btq15DInnQoMhE8TVtuN8c0NuSJp+fmfARUTGzk5EBx5AnRMEU5AHet1dT50ykMHSvsFLSJVeffaGB9fC/vH39OZh4kITqmm+8oGm82S72mxAbkgJe1+XPIxUWbYxjm/Jw7u/heJLVd3x7AB3L6g8+S70I8YdkYDwI71OeZiAVQq7Ea/c6h4maJuwbjd5Lj+62y6Gfzye5xO7W0S3MUfot6BbF88gd5JtlIznEExhbuaTq3cxN+ieYMvYbOxVqGH9lLX+BRRgkicRLmvMgYjqJ9uA4sR30HJA13U; FRIEND.SES_CHK=PZTO+AJBfWvbsLj1CVg9srBzjVvCc12sPUTQMNK+2/00h3AtzWHdLAUYrBw1OqO1X53InrSmTdPs5SCtPZ1ViYaLJsg9WwILRtx/BQhLM5TYD5/J2GXJrOOKov5tr79PMzby31UQpMe0zlL2vM2mIg==; iims2.privateKey=mINE5vjIvZCXWni9b1FwhpYik2MTv3DSKjjHYi6oFh6dL7NmYBQaFgU; clientLang=ko_KR; iims2.serviceInfo=q80_LEaLJAZaQ4-x7bIyQu4r0qPOIgAIuFzdthk0tb3IcB1AAaajvEGpUXu8nMRwNrwC3pjPVplQTzymGDzI79bexwRDe0b8hVatm2_bL8XDs-qoHZ0I74RTLXgnrP1Uata5o3YgqunRvJtqQXP9X5foOJDTxzzjBGdKsQ2DyATgbDad7pVmEWk-45lDlUe2Y8bxprzQVMG28DWKj-hBz9AmPS7p2hBB1jVn9drsOZnjOUS5ok-_1aiYo7jvxJHnpNfRyN83UM7d4yjfMFpao2JBgdffH6FT5O2nxRa4hSk86ssNTCc0xXgcE9P4iSSv6YM2GgW0wXoYiDqJ8EJg3Z4gaTEbBvgvyGqB7YfJ7w-lMqaOYwousoELhctV0TnB',
'Host': 'news-stat-admin.navercorp.com',
'Referer': 'https://news-stat-admin.navercorp.com/today?iims2.serviceInfo=q80_LEaLJAZaQ4-x7bIyQu4r0qPOIgAIuFzdthk0tb3IcB1AAaajvEGpUXu8nMRwNrwC3pjPVplQTzymGDzI79bexwRDe0b8hVatm2_bL8XDs-qoHZ0I74RTLXgnrP1Uata5o3YgqunRvJtqQXP9X5foOJDTxzzjBGdKsQ2DyATgbDad7pVmEWk-45lDlUe2Y8bxprzQVMG28DWKj-hBz9AmPS7p2hBB1jVn9drsOZnjOUS5ok-_1aiYo7jvxJHnpNfRyN83UM7d4yjfMFpao2JBgdffH6FT5O2nxRa4hSk86ssNTCc0xXgcE9P4iSSv6YM2GgW0wXoYiDqJ8EJg3Z4gaTEbBvgvyGqB7YfJ7w-lMqaOYwousoELhctV0TnB&',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
headers2 = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,ru;q=0.6',
'cache-control': 'max-age=0',
'cookie': 'NNB=4YQOEI3TEPAWG; BMR=; VISIT_LOG_CLEAN=1',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

temp = requests.get(url, headers=headers)

rows = json.loads(temp.content.decode())['result']['statDataList'][1]['data']['rows']
print(rows['title'])
exit()
time.sleep(3)

for n in range(len(rows['uri'])):
    uri = rows['uri'][n]
    date0 = rows['date'][n]
    cv = rows['cv_p'][n]
    title = rows['title'][n]
    temp = requests.get(uri, headers=headers2)
    temp = BeautifulSoup(temp.content, 'html.parser')
    article = temp.find('div', {'id':'newsct_article'})
    article = article.text.replace('\n','')

    time.sleep(5)