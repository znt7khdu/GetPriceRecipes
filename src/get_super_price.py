from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import MySQLdb
import re


def get_info(threadurl, endurl):
    site = threadurl
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "lxml")
    tags = soup.find_all("div", class_="advKeyword")

    NAME = []
    SUB = []
    PRICE = []
    ICON = []

    url1 = "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage="

    listnum = soup.find("small").text
    listnum = re.sub('該当商品：', '', listnum, flags=re.MULTILINE)
    listnum = int(listnum)
    q, mod = divmod(listnum, 50)

    for x in range(1, q):
        url = url1 + str(x) + endurl
        site = url
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "lxml")
        tags = soup.find_all("div", class_="advKeyword")

        for tag in tags:
            tr = tag.find("tr")
            ispan = tr.find("a", class_="itemImg-icon_set")
            icon = ispan.find("img").get("data-original")
            ndiv = tr.find("div", class_="name")
            name = ndiv.find("a").text
            sub = ndiv.find("span", class_="break").text
            pspan = tr.find("span", class_="priceBlk__price")
            price = pspan.find("strong").text

            NAME.append(name)
            SUB.append(sub)
            PRICE.append(price)
            ICON.append(icon)

    return NAME, SUB, PRICE, ICON


if __name__ == "__main__":

    con = MySQLdb.connect(
        user='',
        passwd='',
        host='',
        db='',
        charset='utf8')

    cur = con.cursor()

    aNAME = []
    aSUB = []
    aPRICE = []
    aICON = []

    urllist = [
        "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=1,90",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=91,105",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=106,120",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=121,150",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=151,180",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=181,195",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=196,235",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=236,270",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=271,295",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=296,350",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=351,400",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=401,500",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=501,600",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=601,750",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=751,950",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=951,1500",
        # "https://www.the-seiyu.com/front/app/catalog/list/init?searchWord=&searchMethod=0&searchContextPath=%2Ffront&selectSlot=&selectSlot2=&mode=image&pageSize=49&currentPage=1&alignmentSequence=2&resultMessage=&searchUnitPrice=1501,10000"
    ]

    eurllist = [
        "&alignmentSequence=2&resultMessage=&searchUnitPrice=1,90",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=91,105",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=106,120",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=121,150",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=151,180",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=181,195",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=196,235",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=236,270",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=271,295",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=296,350",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=351,400",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=401,500",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=501,600",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=601,750",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=751,950",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=951,1500",
        # "&alignmentSequence=2&resultMessage=&searchUnitPrice=1501,10000"
    ]

    # for num in range(1, 17):
    for num in range(0, 1):
        NAME, SUB, PRICE, ICON = get_info(urllist[num], eurllist[num])
        aNAME = aNAME + NAME
        aSUB = aSUB + SUB
        aPRICE = aPRICE + PRICE
        aICON = aICON + ICON

    for x in range(0, len(aNAME)):
        arg = (aNAME[x], aSUB[x], aPRICE[x], aICON[x])
        cur.execute(
            """INSERT INTO test.price (NAME,SUB,PRICE,ICON_IMG) VALUES (%s, %s, %s, %s);""", arg)
        con.commit()

    cur.close
    con.close
