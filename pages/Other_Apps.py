import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2, column_3 = st.columns([5, 0.8, 5])

with column_1:
    st.title("ジオメトリ・ゲーム")
    st.subheader("ランダムに生成された２つの座標が作り出す長方形の中に、任意に選んだ座標の点が"
                 "入っているかどうかを当てるコマンドラインで操作するゲームです。")
    st.write("プロンプトが表示されたら、画面に従って任意の X 座標と Y 座標を入力します。"
             "また、面積も推測します。")
    st.write("最後にウィンドウが表示され、その中にその長方形と任意に選んだ座標点を表示します。")

    st.write("")
    st.image("images/OOP_App1.PNG")
    st.write("[ソースコード](https://github.com/ten87tak/OOP_App1_GeoGame)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.title("幸福度測定データアプリ")
    st.subheader("GDP（国内総生産）、幸福度、寛容度のデータの相互関係をグラフで表示します :)")

    st.write("")
    st.write("")
    st.write("")
    st.image("images/happiness_app.PNG")
    st.write("[ソースコード](https://github.com/ten87tak/New_Happiness_Data_App)")
    st.write("[ウェブアプリ](https://ten87tak-new-happiness-data-app-main-7i0xd2.streamlit.app/)")


with column_3:
    st.title("宇宙 ～ 本日の一枚 🌏🌕")
    st.subheader("左側の「Astronomy Pic Of Day」タブをご覧ください:) NASA API で作成しました。")

    st.write("")
    st.image("images/astro_pic.jpg")
    st.write("[ソースコード](https://github.com/ten87tak/Astronomy_Today)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.title("ムード・アナライザー")
    st.subheader("日記に書かれた文章を分析して、ポジティブ度とネガティブ度をグラフに表示します。📓")

    st.write("")
    st.write("")
    st.write("")
    st.image("images/diary_tone.PNG")
    st.write("[ソースコード](https://github.com/ten87tak/Visualizing_Moods_from_Diary)")


