from bs4 import BeautifulSoup, NavigableString, Declaration, Comment
from urllib.request import Request, urlopen
import re


def get_recipe(url):
    site=url
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "lxml")

    #レシピのタイトルを取得
    title = soup.find("h1", class_="recipe-title").text

    #レシピの人数を取得
    servnum = soup.find("span", class_="servings_for").text

    name = []
    ammo = []

    #レシピの材料と量のブロックを取得
    block = soup.find("div", id="ingredients_list")
    rows = block.find_all("div", class_="ingredient_row")

    #ブロックから列を一つずつ抽出し、材料と量を配列に格納する
    for row in rows:
        name.append(row.find("span", class_="name").text)
        ammo.append(row.find("div", class_="amount").text)

    #取得した値を返り値に渡す
    TITLE = title
    SERVNUM = servnum
    INGREDIENTNAME = name
    INGREDIENTAMO = ammo

    return TITLE,SERVNUM,INGREDIENTNAME,INGREDIENTAMO



if __name__ == "__main__":

    TITLE,SERVNUM,INGREDIENTNAME,INGREDIENTAMO = get_recipe("https://cookpad.com/recipe/3970570")
    print(TITLE)
    print(SERVNUM)
    print(INGREDIENTNAME)
    print(INGREDIENTAMO)
