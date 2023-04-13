import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2, column_3 = st.columns([5, 0.5, 6])

with column_1:
    st.title("辞書 API")
    st.write("メインファイルをターミナルで実行してください。ブラウザのアドレスバーにフォーマットを"
                 "コピー＆ペーストし「word」のところに調べたい単語を入力します。📖 "
                 "Python ディクショナリでその単語と意味が記載されたデータを取得できます :)"
                 "プログラム開発などにお使いいただけます。")

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.title("お天気 API")
    st.subheader("(「ホーム」タブでも「Weather API」というタイトルで紹介しています！)")
    st.write("メインファイルをターミナルで実行してください。ブラウザのアドレスバーに"
                 "３つあるフォーマットのうちから１つを選び、ブラウザのアドレスバーに、"
                 "コピー＆ペーストします。ステーション ID 番号を選択して貼り付け"
                 " Python ディクショナリでお天気データを取得できます。🌞⛅☔ :)")
    st.write("")
    st.write("[ソースコード](https://github.com/ten87tak/Weather_API)")


with column_3:
    st.write("")
    st.write("")
    st.write("")
    st.image("images/dict_api_urlbar.PNG")
    st.image("images/dict_api.PNG")

    st.write("[ソースコード](https://github.com/ten87tak/Dictionary_API)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image("images/weather_api_home.PNG")
