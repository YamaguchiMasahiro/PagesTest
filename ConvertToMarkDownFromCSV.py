import csv
from os import replace
import re
LINK_FORMAT = "[%s1](%s2)"
def CreateStandardTable():
    # markdown_file = open('./convert.md',"w")
    records = ""
    with open('セキュリティ基準一覧.csv', 'r', encoding="utf-8-sig") as fr:
        csv_file = csv.DictReader(fr, escapechar='\\')
        # マークダウンの表ヘッダー出力
        header_output_flag = False
        for row in csv_file:
            # ヘッダーを一度だけ出力
            if(header_output_flag == False):
                records = "# 設定基準\n\n"
                header_list = [key for key in row.keys()]
                records = records + "| " + " | ".join(header_list) + " |" + "\n"
                records = records + "|" + " --- |" * len(header_list) + "\n"
                header_output_flag = True
            # 解説／対応方針の編集
            if(row["解説／対策"] != ""):
                file_path = row["基準"] + "/" + row["ID"] + ".md"
                # 詳細ファイル作成
                CreateDetailMarkdown(row,file_path)
                # テーブルの値を更新
                row["解説／対策"] = LINK_FORMAT.replace("%s1",row["ID"]).replace("%s2", file_path)
            column_list = [row[key] for key in row.keys()]
            record = "|" + "|".join(column_list) + "|"
            record = record.replace("\n","</br>")
            records = records + record + "\n"
    with open("設定基準一覧.md", mode='w', encoding='utf-8') as fw:
        fw.write(records)

def CreateDetailMarkdown(raw,file_path):
    with open(file_path, mode='w', encoding='utf-8') as f:
        records = raw["解説／対策"]
        records = "# " + raw["ID"] + "\n\n" + records
        records = records.replace("【①：リスク】","## リスク\n")
        records = records.replace("【②：対策】","\n## 対策\n")
        records = records.replace("【③：②を行わない場合のリスク軽減策】","\n## 対策を行わない場合のリスク軽減策\n")
        #records = records.replace("（実施時のTIP）","\n### 実施時のTIP\n") 
        records = re.sub(r'\n（(.*)）\n', "\n\n### \\1\n\n", records)
        # URL変換
        #records = re.sub(r'\n(https.*)\n', '\n  - <\\1>\n', records)
        records = re.sub(r'\n・?(https.*)\n', '\n- <\\1>\n', records)
        records = re.sub(r'\n・', "\n- ", records)
        records = re.sub(r'\n　・?', "\n  - ", records)
        f.write(records + "\n")
        f.close()
CreateStandardTable()
