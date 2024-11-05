import streamlit as st
import time
import html

# ページの設定
st.set_page_config(page_title="野村日魚子「幽体について」")

# カスタムCSSの適用
st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Mincho';
        src: local('Yu Mincho'), local('游明朝'), local('MS Mincho'), local('Hiragino Mincho ProN'), serif;
    }
    body, p {
        background-color: black;
        color: white;
        font-family: 'Mincho', serif;
        margin: 0;
        white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True
)

text = '''
import time
import sys

text = 
事件のあとに会う幽霊たちみなわずかに傾いている十月の午後

足がなくなっているから死んだと思ったわけじゃないんだ　思い出をお金に換えられるようになったから

みえない箱をこわれないように持ち運ぶあなたが監視カメラに映っている

階下には眠りに就こうとする人たちがひしめき天国なのにいたるところ冷蔵庫のにおい

あなたは機械のからだをもらってそれ以降もう神童とは呼ばれなかった

怪物の死後　恋愛は存在しないということになり踊られた暴力的で透明なダンス

これが映画だとしたらエンドロールではないかと聞かれる　ちがうと思います答える

つぎに生まれたら足よりも海の方が役に立つよね　そうかな　そうかも　駅が見えてきた

少年期の終わり　わたしは血の付いた手で冠にさわることをゆるされる

予言はおしまい　あこがれの犬と話すからいますぐベッドからおりなくちゃ

for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)
'''

# テキスト内の全角スペースを半角スペースに置き換え
text = text.replace('　', ' ')

# テキスト表示のプレースホルダー
placeholder = st.empty()
display_text = ''

# 起動後に1秒待機
time.sleep(1)

# テキストを一文字ずつ表示
for char in text:
    display_text += char
    # 特殊文字をエスケープ
    escaped_text = html.escape(display_text)
    html_text = f'<p>{escaped_text}</p>'
    placeholder.markdown(html_text, unsafe_allow_html=True)
    time.sleep(0.2)
