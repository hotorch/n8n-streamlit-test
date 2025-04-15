# N8N 워크플로우 & 스트림릿 채팅 인터페이스

이 프로젝트는 n8n 워크플로우와 Streamlit 채팅 인터페이스를 결합하여 사용자 정의 AI 챗봇을 구현하는 예제입니다.

## 프로젝트 개요

- **N8N 워크플로우**: AI 모델(LLM)과 연결하여 채팅 로직을 처리합니다.
- **Streamlit 인터페이스**: 사용자 친화적인 채팅 웹 인터페이스를 제공합니다.

## 설치 방법

1. 저장소 클론하기:
    ```bash
    git clone https://github.com/yourusername/streamlit-n8n.git
    cd streamlit-n8n
    ```

2. 필요한 패키지 설치:
    ```bash
    pip install -r requirements.txt
    ```

## 사용 방법

1. Streamlit 앱 실행:
    ```bash
    streamlit run app.py
    ```

2. 웹 브라우저에서 앱 접속 (기본적으로 http://localhost:8501)

3. 사이드바에서 N8N 웹훅 URL을 입력하고 채팅 시작

## N8N 워크플로우 설정

1. N8N에 로그인하고 새 워크플로우 생성 또는 제공된 JSON 파일 가져오기:
   - `simple_chat_X_streamlit.json` 파일을 N8N으로 가져와서 워크플로우 설정

2. 워크플로우 활성화 후 웹훅 URL 복사:
   - 워크플로우에서 웹훅 노드를 선택하고 웹훅 URL을 복사합니다.

3. 해당 웹훅 URL을 Streamlit 앱의 사이드바에 있는 입력란에 붙여넣기

## 워크플로우 커스터마이징

n8n 워크플로우를 다음과 같이 커스터마이징 할 수 있습니다:

1. 다른 AI 모델 사용 (GPT-4, Claude 등)
2. 프롬프트 엔지니어링 변경
3. RAG (Retrieval Augmented Generation) 시스템 추가
4. 외부 API 통합

## 참고사항

- 이 프로젝트는 교육 목적으로 작성되었습니다.
- 실제 프로덕션 환경에서는 보안 및 오류 처리를 강화해야 합니다.

## 라이센스

MIT 