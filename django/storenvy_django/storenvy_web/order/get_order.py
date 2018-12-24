import time
import requests
from lxml import etree
import pymysql


def get_sale_num():
    conn = pymysql.connect(host='localhost', port=3306,
        user='root', password='123456',
        db='storenvy', charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    id_list = get_id(conn)
    for store_id in id_list:
        url = 'https://www.storenvy.com/stores/' + str(store_id)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        page = requests.get(url, headers=headers)
        tree = etree.HTML(page.text)
        sale_text = tree.xpath('//span[@class="order-count"]')
        if sale_text:
            sale_num = sale_text[0].text.replace('Sale', '').strip()
        else:
            sale_num = 0
        cursor.execute('UPDATE storenvy set sale_all=%s where store_id=%s', (sale_num, store_id))
        conn.commit()
        print(sale_num)
    cursor.close()

def get_id(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * from storenvy')
    results = cursor.fetchall()
    id_list = []
    for res in results:
        store_id = res['store_id']
        id_list.append(store_id)
    # print(id_list)
    cursor.close()
    return id_list


if __name__ == '__main__':
    get_sale_num()

