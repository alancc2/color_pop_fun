import streamlit as st
import streamlit.components.v1 as components

# 設定頁面標題
st.title("Streamlit 載入 HTML 範例")

# 讀取 HTML 檔案
with open("color_pop_fun.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 在 Streamlit 中渲染 HTML (可指定高度 height 與捲動軸 scrolling)
components.html(html_data, height=600, scrolling=True)