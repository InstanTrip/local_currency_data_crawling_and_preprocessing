import requests

def file_download(result_dir: str, data_name: str, data_id: str, file_id: str) -> None:
    file_download_url = f"https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId={file_id}&fileDetailSn=1"

    response = requests.get(file_download_url)

    if response.status_code == 200:
        with open(f"{result_dir}/{data_name}.csv", "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download file: {response.status_code}")