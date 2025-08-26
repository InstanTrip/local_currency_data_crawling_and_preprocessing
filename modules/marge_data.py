# result/ 의 csv 데이터 전부 병합하여 하나의 파일로 만들기

import os
import csv

def marge_csv_files():
    file_list = os.listdir("result")
    merged_file_path = "merged_data.csv"

    is_first_file = True

    with open(merged_file_path, "w", newline="", encoding="utf-8") as merged_file:
        csv_writer = csv.writer(merged_file)

        for file_name in file_list:
            if file_name.endswith(".csv"):
                with open(f"result/{file_name}", "r", encoding="utf-8") as f:
                    csv_reader = csv.reader(f)
                    try:
                        for row in csv_reader:
                            # 빈줄 스킵
                            if not row:
                                continue
                            if not is_first_file and csv_reader.line_num == 1:
                                continue
                            csv_writer.writerow(row)
                    except Exception as e:
                        print(f"Error processing {file_name}: {e}")
            is_first_file = False