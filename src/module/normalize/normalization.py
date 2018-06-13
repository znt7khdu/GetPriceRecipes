import os
import re
import sys
import glob
from tqdm import tqdm
import neologdn

from clean import clean_html_tags, clean_text


def normalize_number(text):
    """
    pattern = r'\d+'
    replacer = re.compile(pattern)
    result = replacer.sub('0', text)
    """
    # 連続した数字を0で置換
    replaced_text = re.sub(r'\d+', '0', text)
    return replaced_text


def normalize(file_text):
    file_text = clean_html_tags(file_text)
    file_text = clean_text(file_text)
    # file_text = normalize_number(file_text)
    file_text = neologdn.normalize(file_text)
    return file_text


def normalize_file(read_file_path, output_file_path):
    with open(read_file_path, 'r') as r, open(output_file_path, 'w+') as w:
        for row in r:
            normalized_text = normalize(row)
            if normalized_text:
                w.writelines(normalized_text)


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise Exception(
            'glob_file_path is required parameter'
        )

    # python normalization.py
    # "~/Desktop/word2vec/wikiextractor/text/*/wiki*" ./wiki.txt
    glob_file_path = sys.argv[1]

    read_file_path = glob.glob(glob_file_path)

    # 処理の進捗バー
    bars = tqdm(total=len(read_file_path))

    # 吐き出し用のディレクトリ作成
    os.makedirs('./dist', exist_ok=True)

    for index, file_path in enumerate(read_file_path):
        normalize_file(file_path, './dist/{0}.txt'.format(index))
        bars.update(1)

    bars.close()
