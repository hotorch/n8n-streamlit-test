# Streamlit LLM 채팅 앱

이 앱은 n8n 웹훅을 통해 LLM과 채팅할 수 있는 Streamlit 애플리케이션입니다.

## ⚠️ 중요: 환경 변수 설정 필수

애플리케이션을 실행하기 전에 반드시 `WEBHOOK_URL` 환경 변수를 설정해야 합니다. 이는 보안상의 이유로 코드에 직접 URL을 포함시키지 않기 위함입니다.

### 환경 변수 설정 방법:

1. 직접 환경 변수 설정:
```bash
# Windows
set WEBHOOK_URL=your_webhook_url_here

# Mac/Linux
export WEBHOOK_URL=your_webhook_url_here
```

2. .env 파일 사용 (추천):
```bash
# .env.example 파일을 복사하여 .env 파일 생성
cp .env.example .env

# .env 파일을 편집하여 실제 웹훅 URL 입력
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