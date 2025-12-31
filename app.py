import streamlit as st
import requests

st.title("📢 Slack通知アプリ")

st.write("メッセージを送るよ！")

message = st.text_input("送りたいメッセージを入れてね", "こんにちは！")

webhook_url = st.text_input("Slack Webhook URL", type="password")

if st.button("送信する"):
    if webhook_url:
        try:
            data = {"text": message}
            response = requests.post(webhook_url, json=data)
            if response.status_code == 200:
                st.success("メッセージを送ったよ！")
                st.balloons()
            else:
                st.error("送れなかったよ...")
        except Exception as e:
            st.error(f"エラーが出たよ: {e}")
    else:
        st.warning("Webhook URLを入れてね！")
