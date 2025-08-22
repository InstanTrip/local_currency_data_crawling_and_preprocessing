import re
import json
import requests
from bs4 import BeautifulSoup

from modules.file_download import file_download

DATA_ID = "15100062"
RESULT_DIR = "result"

get_uddi_regex = re.compile(r"stdObj.fn_fileDataDetail\('(.+)'\)")

page_index = 0
while True:
    page_index += 1
    filelist=requests.get(f"https://www.data.go.kr/tcs/dss/stdFileList.do?publicDataPk={DATA_ID}&searchKeyword2=&pageIndex={page_index}&url=%2Ftcs%2Fdss%2FstdFileList.do")
    soup = BeautifulSoup(filelist.text, "lxml").find_all("div", {"class": "tit"})

    if len(soup) <= 0:
        break

    for item in soup:
        uddi = get_uddi_regex.match(item.find("a")["onclick"]).group(1)

        get_download_url = f"https://www.data.go.kr/tcs/dss/selectFileDataDownload.do?publicDataPk={DATA_ID}&publicDataDetailPk={uddi}&fileExtsn=csv"

        uddi_page = BeautifulSoup(requests.get(get_download_url).text, "lxml")

        data_name = json.loads(uddi_page.find("p").text).get("dataSetFileDetailInfo").get("dataNm")
        file_id = json.loads(uddi_page.find("p").text).get("fileDataRegistVO").get("atchFileId")

        file_download(result_dir=RESULT_DIR, data_name=data_name, data_id=DATA_ID, file_id=file_id)