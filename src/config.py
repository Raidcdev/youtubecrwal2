import os
import json
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수 설정
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
PROJECT_NAME = os.getenv('PROJECT_NAME')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

def get_service_account_info():
    """서비스 계정 정보를 환경변수에서 가져와 딕셔너리로 반환"""
    return {
        "type": os.getenv('GOOGLE_SERVICE_ACCOUNT_TYPE'),
        "project_id": os.getenv('GOOGLE_PROJECT_ID'),
        "private_key_id": os.getenv('GOOGLE_PRIVATE_KEY_ID'),
        "private_key": os.getenv('GOOGLE_PRIVATE_KEY'),
        "client_email": os.getenv('GOOGLE_CLIENT_EMAIL'),
        "client_id": os.getenv('GOOGLE_CLIENT_ID'),
        "auth_uri": os.getenv('GOOGLE_AUTH_URI'),
        "token_uri": os.getenv('GOOGLE_TOKEN_URI'),
        "auth_provider_x509_cert_url": os.getenv('GOOGLE_AUTH_PROVIDER_X509_CERT_URL'),
        "client_x509_cert_url": os.getenv('GOOGLE_CLIENT_X509_CERT_URL')
    }

def validate_config():
    """환경변수가 올바르게 설정되었는지 확인"""
    required_vars = [
        'YOUTUBE_API_KEY',
        'GOOGLE_SERVICE_ACCOUNT_TYPE',
        'GOOGLE_PROJECT_ID',
        'GOOGLE_PRIVATE_KEY_ID',
        'GOOGLE_PRIVATE_KEY',
        'GOOGLE_CLIENT_EMAIL',
        'GOOGLE_CLIENT_ID'
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

def create_service_account_file():
    """서비스 계정 정보를 임시 JSON 파일로 생성"""
    service_account_info = get_service_account_info()
    
    # config 디렉토리가 없으면 생성
    os.makedirs('config', exist_ok=True)
    
    # 서비스 계정 정보를 JSON 파일로 저장
    with open('config/service_account.json', 'w') as f:
        json.dump(service_account_info, f, indent=2)