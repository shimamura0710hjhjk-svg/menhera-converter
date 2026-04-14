import streamlit as st
import base64
from PIL import Image
from converter_tool.converters import menhera_converter

# --- 1. ページ全体の初期設定 ---
st.set_page_config(
    page_title="💔 メンヘラコンバーター 💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 背景パターンの設定関数 ---
def set_bg_pattern(main_bg):
    try:
        with open(main_bg, "rb") as f:
            bin_str = base64.b64encode(f.read()).decode()
        
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-repeat: repeat !important;
            background-size: 80px 80px !important;
            background-attachment: fixed !important;
        }}
        [data-testid="stSidebar"] {{
            background-color: rgba(255, 255, 255, 0.8) !important;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        # 画像がないときは静かに見守るね（エラーを出しすぎると怖がられちゃうから）
        pass

# 背景をセット（画像パスは環境に合わせてね）
set_bg_pattern("image/ojisanpatarn.png")

# --- 3. サイドバーの設定 ---
st.sidebar.title("メンヘラの部屋 🥀")
# image = Image.open('image/メンヘラ本体.png') # 画像があればコメント解除してね
# st.sidebar.image(image)

st.sidebar.write("""
### 作品解説
普通の文章を「メンヘラ彼女構文」に変換します。
おじさんの残党を浄化し、重すぎる愛を詰め込みました。✨
""")

# --- 4. メイン画面の表示 ---
st.title("💔 メンヘラコンバーター 💬")
st.markdown("普通の文章を、逃げられないほど重い愛の言葉に変換するよ。")

# 入力エリア
input_text = st.text_area(
    "私に伝えたいことは何：",
    placeholder="変換したい文章を入力して。……無視は許さないよ？\n\n例: 明日はデートですか？楽しみです。",
    height=200
)

# --- 5. 変換処理とデザイン反映 ---
if st.button("変換する（逃がさないよ）"):
    if input_text:
        # 変換実行
        result = menhera_converter(input_text)
        
        # 変換結果のカスタムデザイン表示
        st.markdown(f'''
            <div style="
                background-color: #fff0f5; 
                border: 3px solid #ff69b4; 
                border-radius: 15px; 
                padding: 20px; 
                color: #000000; 
                font-weight: 900; 
                font-size: 1.2rem; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            ">
                🔪 変換結果（これが私の本音だよ）：<br><br>
                {result}
            </div>
        ''', unsafe_allow_html=True)
        
        # 通知ボックス（もし使われた時のための予備デザイン）
        design_css = '''
        <style>
            div[data-testid="stNotification"] {
                background-color: rgba(255, 255, 255, 0.95) !important;
                border: 2px solid #ff69b4 !important;
                border-radius: 10px !important;
            }
            div[data-testid="stNotification"] p {
                color: #000000 !important;
                font-weight: 900 !important;
            }
        </style>
        '''
        st.markdown(design_css, unsafe_allow_html=True)
    else:
        st.warning("……。何か書いてよ。無言なんて、一番ひどいよ。")

# --- 6. フッター ---
st.markdown("---")
st.markdown("<small style='text-align: center; color: #888;'>Powered by Your Obsession</small>", unsafe_allow_html=True)