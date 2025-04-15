import streamlit as st
import requests
import uuid

# 초기 웹훅 URL 예시
DEFAULT_WEBHOOK_URL = ""  # 빈 값으로 시작

def generate_session_id():
    return str(uuid.uuid4())

def send_message_to_llm(session_id, message, webhook_url):
    payload = {
        "sessionId": session_id,
        "chatInput": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        return response.json()["output"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.title("Chat with LLM")

    # 사이드바에 웹훅 URL 입력 필드 추가
    with st.sidebar:
        st.header("설정")
        st.markdown("""
        ### N8N 웹훅 URL 설정
        
        1. n8n에서 워크플로우를 생성하거나 가져오세요
        2. 워크플로우의 웹훅 노드에서 URL을 복사하세요
        3. 아래 입력란에 붙여넣으세요
        
        예시 형식: `https://your-n8n-instance.com/webhook/path-to-webhook`
        """)
        
        webhook_url = st.text_input(
            "N8N 웹훅 URL", 
            value=st.session_state.get("webhook_url", DEFAULT_WEBHOOK_URL),
            placeholder="https://your-n8n-instance.com/webhook/path-to-webhook"
        )
        
        if webhook_url:
            st.session_state.webhook_url = webhook_url
        
        if not webhook_url:
            st.warning("웹훅 URL을 입력해야 채팅을 시작할 수 있습니다.")
        else:
            st.success("웹훅 URL이 설정되었습니다. 채팅을 시작할 수 있습니다.")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = generate_session_id()
    if "webhook_url" not in st.session_state:
        st.session_state.webhook_url = DEFAULT_WEBHOOK_URL

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User input - 웹훅 URL이 설정된 경우에만 활성화
    user_input = st.chat_input("메시지를 입력하세요...", disabled=not st.session_state.webhook_url)

    if user_input and st.session_state.webhook_url:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Get LLM response
        with st.spinner("응답을 생성 중입니다..."):
            llm_response = send_message_to_llm(
                st.session_state.session_id, 
                user_input, 
                st.session_state.webhook_url
            )

        # Add LLM response to chat history
        st.session_state.messages.append({"role": "assistant", "content": llm_response})
        with st.chat_message("assistant"):
            st.write(llm_response)

if __name__ == "__main__":
    main()