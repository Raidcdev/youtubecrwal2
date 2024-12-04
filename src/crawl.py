from config import validate_config, PROJECT_NAME, DEBUG, create_service_account_file

def main():
    try:
        validate_config()
        create_service_account_file()
        print(f"프로젝트 '{PROJECT_NAME}'이(가) 성공적으로 시작되었습니다!")
        print(f"디버그 모드: {DEBUG}")
        print("서비스 계정 설정이 완료되었습니다.")
    except ValueError as e:
        print(f"설정 오류: {e}")

if __name__ == "__main__":
    main() 