import requests
import os # os 모듈 추가

def file_download(result_dir: str, data_name: str, data_id: str, file_id: str) -> None:
    # 디렉토리가 없으면 생성
    os.makedirs(result_dir, exist_ok=True)
    
    file_download_url = f"https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId={file_id}&fileDetailSn=1"

    print(f"'{data_name}.csv' 다운로드 중...")
    response = requests.get(file_download_url)

    if response.status_code == 200:
        try:
            # 1. 응답 받은 바이너리 데이터를 'cp949'로 디코딩하여 문자열로 변환
            decoded_content = response.content.decode('cp949')

            # 2. 파일을 텍스트 모드('w')와 'utf-8' 인코딩으로 열기
            with open(f"{result_dir}/{data_name}.csv", "w", encoding="utf-8", newline="") as f:
                f.write(decoded_content)
            
            print(f"데이터 변환 성공: CP949 감지 및 UTF-8로 변환 완료.")

        except UnicodeDecodeError:
            with open(f"{result_dir}/{data_name}.csv", "wb") as f:
                f.write(response.content)
        
    else:
        print(f"실패: 파일 다운로드에 실패했습니다. (상태 코드: {response.status_code})")