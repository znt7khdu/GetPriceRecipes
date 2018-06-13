from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def get_recipe(url):
    site = url
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)

    try:
        page = urlopen(req)
    # HTTP Error 404の場合Noneを返す
    except:
        TITLE = ""
        SERVNUM = ""
        INGREDIENTNAME = [""]
        INGREDIENTAMO = [""]
        return TITLE, SERVNUM, INGREDIENTNAME, INGREDIENTAMO

    soup = BeautifulSoup(page, "lxml")

    # レシピのタイトルを取得
    title = soup.find("h1", class_="recipe-title").text

    # レシピの人数を取得
    servnum = soup.find("span", class_="servings_for")
    # 人数が空白の場合を考慮する
    if servnum is None:
        servnum = ""
    else:
        servnum = servnum.text

    name = []
    ammo = []

    # レシピの材料と量のブロックを取得
    block = soup.find("div", id="ingredients_list")
    rows = block.find_all("div", class_="ingredient_row")

    # ブロックから列を一つずつ抽出し、材料と量を配列に格納する
    for row in rows:
        # 空行とカテゴリ行を取得する
        space = row.find("div", class_="ingredient_spacer")
        category = row.find("div", class_="ingredient_category")

        # 空行だったりとカテゴリ行でなかった場合のみ名前と量を取得する
        if space is None:
            if category is None:
                name.append(row.find("span", class_="name").text)
                ammo.append(row.find("div", class_="amount").text)

    # 取得した値を返り値に渡す
    TITLE = re.sub('\n', '', title, flags=re.MULTILINE)
    SERVNUM = re.sub('\n', '', servnum, flags=re.MULTILINE)
    INGREDIENTNAME = name
    INGREDIENTAMO = ammo

    return TITLE, SERVNUM, INGREDIENTNAME, INGREDIENTAMO


if __name__ == "__main__":

    # とりあえず10個のレシピで検証
    for num in range(400001, 400005):
        url = "https://cookpad.com/recipe/" + str(num)
        TITLE, SERVNUM, INGREDIENTNAME, INGREDIENTAMO = get_recipe(url)

        print(url)
        print(TITLE)
        print(SERVNUM)
        print(INGREDIENTNAME)
        print(INGREDIENTAMO)
