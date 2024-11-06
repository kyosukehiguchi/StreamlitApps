import streamlit as st
import random

def randomize_sentences(text):
    # 100万字までの制限
    if len(text) > 1_000_000:
        raise ValueError("入力可能な文章は100万字までです。")

    # 句点で文を区切り、リストに分ける
    sentences = text.split("。")
    
    # 空文字列の除去
    sentences = [sentence for sentence in sentences if sentence]

    # ランダムに並び替える
    random.shuffle(sentences)

    # 各文を改行なしで結合し、最後に1つだけ句点を追加
    randomized_text = "。".join(sentences) + "。"
    
    return randomized_text

# Streamlitアプリの構築
st.title("Text Randomizer")
st.write("入力された日本語の文章をランダムに並び替えます。")

# ユーザーからのテキスト入力
user_input = st.text_area("テキストを入力してください（100万字まで）", height=200)

# 並び替えボタン
if st.button("Randomize"):
    try:
        # テキストをランダムに並び替えてHTML形式で表示
        result = randomize_sentences(user_input)
        st.markdown(f"<p>{result}</p>", unsafe_allow_html=True)
    except ValueError as e:
        # エラーメッセージの表示
        st.error(e)
