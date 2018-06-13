import re


def clean_html_tags(text):
    replaced_text = re.sub(r'<[^>]*>', '', text)
    return replaced_text


def clean_text(text):
    # replaced_text = '\n'.join(s.strip() for s in text.splitlines()[2:] if s != '')  # skip header by [2:]
    # replaced_text = replaced_text.lower()
    replaced_text = re.sub(r'[【】]', ' ', text)       # 【】の除去
    # replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
    replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)   # ［］の除去
    # replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    # replaced_text = re.sub(r'https?:\/\/.*?[\r\n ]', '', replaced_text)  # URLの除去
    # replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
    return replaced_text
