from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json
from itertools import chain
from module.sql import sql_init


def scrape_page(url):
    print('scrape url : ' + url)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)
    page = urlopen(req)
    return BeautifulSoup(page, "lxml")


def get_page_items(url, category_code):
    soup = scrape_page(url)
    tags = soup.find_all("li", class_="jsFlatHeight_list")

    items = []

    category_code_formated = {
        # 大項目
        'category1code': int(category_code['category1code']),
        # 中項目
        'category2code': int(category_code['category2code']),
        # 小項目
        'category3code': int(category_code['category3code'])
    }

    for tag in tags:
        name = tag.find("div", class_="nameRw").find("strong").text.strip()
        # 中黒以降の単位文字列の取得
        names_sub = ''.join(re.findall(r'\u30fb([一-龥ぁ-んa-zァ-ン0-９]*)', name))
        icon = tag.find("img").get("data-original")
        price = int(
            tag.find("span", class_="price").find('strong')
            .text.replace(',', '')
        )
        # 値がない場合全角スペースが入っているため削除する
        sub = tag.find("div", class_="nameRw").find_all('small')[1].text.strip()

        # names_subとsubは同時に存在しないはず
        # 存在する場合は調整する必要あり
        if len(names_sub) > 0 and len(sub) > 0:
            print(sub, names_sub)
            raise Exception('names and sub is exists')

        item = {
            # アイコンの画像URL
            'icon': icon,
            # 商品名
            'name': name,
            # 補足情報(~個, ~gあたり...)
            'sub': names_sub or sub,
            # 値段
            'price': price
        }

        items.append({**item, **category_code_formated})

    print('this page items length : ' + str(len(items)))

    return items


def get_page_num(url):
    soup = scrape_page(url)
    listnum = soup.find("small", class_="categoryTitle__small").text
    listnum = re.findall(r'\d+', listnum)
    listnum = int(listnum[0])
    pageNum, mod = divmod(listnum, 50)

    return pageNum


if __name__ == "__main__":
    con, cur = sql_init()

    all_items = []

    with open('tmp/link.json', 'r') as f:
        json_data = json.load(f)
        for url in json_data:
            pageNum = get_page_num(url) + 1
            print('pageNum : ' + str(pageNum))

            for x in range(0, pageNum):
                items = get_page_items(url + '&currentPage=' + str(x + 1), {
                    'category1code': re.findall(r'parent1Code=(\d+)', url)[0],
                    'category2code': re.findall(r'parent2Code=(\d+)', url)[0],
                    'category3code': re.findall(
                        r'searchCategoryCode=(\d+)', url
                    )[0]
                })
                all_items.append(items)

    # flatten
    all_items = list(chain.from_iterable(all_items))

    print("""
    ======================
      end scrape
      length : {}
    ======================
    """.format(len(all_items)))

    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(all_items)

    for item in all_items:
        arg = (item['name'], item['sub'], item['price'], item['icon'],
               item['category1code'], item['category2code'],
               item['category3code'])
        cur.execute("""
            INSERT INTO test.price
            (NAME,SUB,PRICE,ICON_IMG,CATEGORY1CODE,CATEGORY2CODE,CATEGORY3CODE)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, arg)
        con.commit()

    cur.close
    con.close
