# Streamlit LLM 채팅 앱

이 앱은 n8n 웹훅을 통해 LLM과 채팅할 수 있는 Streamlit 애플리케이션입니다.

## 🚀 빠른 시작 (강의용)

### 1. 웹훅 URL 설정
`config.txt.example` 파일을 참고하여 `config.txt` 파일을 생성하고 웹훅 URL을 입력하세요:

```bash
# config.txt.example 파일을 복사
cp config.txt.example config.txt

# config.txt 파일을 편집하여 웹훅 URL 입력
# 예시: https://your-n8n-instance.app.n8n.cloud/webhook/your-webhook-id
```

### 2. 앱 실행
```bash
# 필요한 패키지 설치
pip install -r requirements.txt

# 앱 실행
streamlit run app.py
```

브라우저에서 `http://localhost:8501`로 접속하여 채팅을 시작하세요!

## ⚙️ 설정 방법

이 앱은 웹훅 URL을 다음 순서로 찾습니다:

1. **config.txt 파일** (추천 - 강의용)
2. **환경 변수** (.env 파일 또는 시스템 환경 변수)

### 방법 1: config.txt 파일 사용 (추천)

```bash
# 1. config.txt 파일 생성
echo "https://your-webhook-url-here" > config.txt

# 2. 앱 실행
streamlit run app.py
```

### 방법 2: 환경 변수 사용

#### .env 파일 사용:
```bash
# .env.example 파일을 복사하여 .env 파일 생성
cp .env.example .env

# .env 파일을 편집하여 실제 웹훅 URL 입력
```

#### 직접 환경 변수 설정:
```bash
# Windows
set WEBHOOK_URL=your_webhook_url_here

# Mac/Linux
export WEBHOOK_URL=your_webhook_url_here
```

## 설치 및 실행 방법

1. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

2. 로컬에서 앱 실행:
```bash
streamlit run app.py
```

## 배포 방법

### Streamlit Cloud를 통한 배포

1. [Streamlit Cloud](https://streamlit.io/cloud)에 가입하세요.
2. GitHub에 이 프로젝트를 업로드하세요.
3. Streamlit Cloud에서 "New app" 버튼을 클릭하세요.
4. GitHub 저장소, 브랜치, 앱 파일 경로(app.py)를 선택하세요.
5. **고급 설정에서 반드시 `WEBHOOK_URL` 환경 변수를 설정하세요.**
6. "Deploy"를 클릭하세요.

### Heroku를 통한 배포

1. [Heroku](https://www.heroku.com/)에 가입하세요.
2. Heroku CLI를 설치하세요.
3. 프로젝트 루트에 다음 내용의 `Procfile`을 생성하세요:
```
web: streamlit run app.py --server.port=$PORT
```
4. 환경 변수 설정:
```bash
heroku config:set WEBHOOK_URL=your_webhook_url_here
```
5. 배포:
```bash
git push heroku main
```

### 기타 플랫폼

- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [AWS EC2](https://aws.amazon.com/ec2/)
- [Google Cloud Run](https://cloud.google.com/run)

## 환경 변수

이 앱은 다음 환경 변수를 **필수로** 사용합니다:

- `WEBHOOK_URL`: n8n 웹훅 URL (보안을 위해 반드시 환경 변수로 설정해야 합니다)

## 보안 주의사항

- 웹훅 URL을 코드에 하드코딩하거나 공개 저장소에 포함시키지 마세요.
- 항상 환경 변수나 비밀 관리 서비스를 통해 관리하세요.
- 배포 플랫폼의 보안 설정을 확인하고 환경 변수가 안전하게 관리되는지 확인하세요. 