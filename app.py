import streamlit as st
import requests
import uuid
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

def load_webhook_url():
    """config.txt 파일에서 웹훅 URL을 읽어오거나, 없으면 환경변수에서 가져옴"""
    # 1. config.txt 파일에서 읽기 시도
    try:
        with open('config.txt', 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content and not content.startswith('#'):
                return content
    except FileNotFoundError:
        pass
    
    # 2. 환경변수에서 읽기 (fallback)
    webhook_url = os.environ.get("WEBHOOK_URL")
    if webhook_url:
        return webhook_url
    
    return None

# Constants
WEBHOOK_URL = load_webhook_url()
if not WEBHOOK_URL:
    st.error("웹훅 URL이 설정되지 않았습니다. config.txt 파일에 웹훅 URL을 입력하거나 환경 변수 WEBHOOK_URL을 설정해주세요.")
    st.info("config.txt 파일을 생성하고 첫 번째 줄에 웹훅 URL을 입력해주세요.")
    st.stop()

def generate_session_id():
    return str(uuid.uuid4())

def send_message_to_llm(session_id, message):
    payload = {
        "sessionId": session_id,
        "chatInput": message
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        return response.json()["output"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.title("Chat with LLM")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = generate_session_id()

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Get LLM response
        llm_response = send_message_to_llm(st.session_state.session_id, user_input)

        # Add LLM response to chat history
        st.session_state.messages.append({"role": "assistant", "content": llm_response})
        with st.chat_message("assistant"):
            st.write(llm_response)

if __name__ == "__main__":
    main()