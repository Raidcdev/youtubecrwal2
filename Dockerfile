FROM python:3.9-slim

WORKDIR /app

# 기본 개발 도구 설치
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 파이썬 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

CMD ["tail", "-f", "/dev/null"] 