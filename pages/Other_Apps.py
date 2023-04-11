import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2, column_3 = st.columns([5, 0.5, 6])

with column_1:
    st.header("ジオメトリ・ゲーム")

    st.write("ランダムに生成された２つの座標が作り出す長方形の中に、任意に選んだ座標の点が"
                 "入っているかどうかを当てるコマンドラインで操作するゲームです。")

    st.write("プロンプトが表示されたら、画面に従って任意の X 座標と Y 座標を入力します。"
                 "また、面積も推測します。")

    st.write("最後にウィンドウが表示され、その中にその長方形と任意に選んだ座標点を表示します。")

    st.write("")
    st.write("")
    st.write("")

    st.write("[ソースコード](https://github.com/ten87tak/OOP_App1_GeoGame)")


    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image("images/astro_pic.jpg")

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.header("幸福度データ測定アプリ")
    st.write("GDP（国内総生産）、幸せ度、寛容の度合のデータの相互関係をグラフに表示します！:)")

    st.write("")
    st.write("")

    st.write("[ソースコード](https://github.com/ten87tak/New_Happiness_Data_App)")

    st.write("")
    st.write("")

    st.write("[ウェブアプリ](https://ten87tak-new-happiness-data-app-main-7i0xd2.streamlit.app/)")


with column_3:
    st.write("")
    st.image("images/OOP_App1.PNG")

    st.write("")
    st.write("")
    st.write("")

    st.header("宇宙 ～ 本日の一枚 🌏🌕")
    st.write("左側の「Astronomy Pic Of Day」タブをご覧ください:) NASA API で作成しました。")

    st.write("")
    st.write("")

    st.write("[ソースコード](https://github.com/ten87tak/Astronomy_Today)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.image("images/happiness_app.PNG")

