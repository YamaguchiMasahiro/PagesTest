import csv
###########################
##########テスト############
###########################
def Convert():
    ## アップロードされている記事リストを取得
    # csv_file = open('./セキュリティ基準一覧.csv',"r")
    # markdown_file = open('./convert.md',"w")

    print('ok_reader')
    with open('./aaa.csv', 'r') as f:
    #with open('./セキュリティ基準一覧.csv', 'r',encoding="utf-8") as f:
        ok_reader = csv.DictReader(f, escapechar='\\')
        for row in ok_reader:
            print(row)

Convert()
