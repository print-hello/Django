import requests
from lxml import etree
import pymysql
import datetime
import queue
import threading


q = queue.Queue()


def get_id():
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', password='123456',
                           db='storenvy', charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute('SELECT * from storenvy')
    results = cursor.fetchall()
    for res in results:
        store_id = res['store_id']
        q.put(store_id)
    cursor.close()


def get_sale_num():
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', password='123456',
                           db='storenvy', charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    while q.qsize() > 0:
        store_id = q.get()
        url = 'https://www.storenvy.com/stores/' + str(store_id)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        page = requests.get(url, headers=headers)
        tree = etree.HTML(page.text)
        sale_text = tree.xpath('//span[@class="order-count"]')
        if sale_text:
            sale_num = sale_text[0].text.split(' ')[0].strip()
        else:
            sale_num = 0
        cursor.execute('SELECT * from storenvy where store_id=%s' % store_id)
        res = cursor.fetchone()
        if res:
            last_time = res['spider_time']
            sale_all = res['sale_all']
            last_sale_all = res['last_sale_all']
            if str(last_time) == str(current_time):
                sale_today = int(sale_num) - int(last_sale_all)
                cursor.execute(
                    'UPDATE storenvy set sale_all=%s, sale_today=%s, spider_time=%s where store_id=%s', (sale_num, sale_today, current_time, store_id))
            elif str(last_time) < str(current_time):
                last_sale_all = sale_all
                sale_today = int(sale_num) - int(last_sale_all)
                cursor.execute(
                    'UPDATE storenvy set sale_all=%s, last_sale_all=%s, sale_today=%s, spider_time=%s where store_id=%s', (sale_num, last_sale_all, sale_today, current_time, store_id))
            conn.commit()
            # print(store_id, sale_num)
    cursor.close()
    conn.close()


def start_crawl():
    get_id()
    for i in range(15):
        threading.Thread(target=get_sale_num).start()
