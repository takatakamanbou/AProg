##### AProg2021 第7回課題B

import re  # 「正規表現」を扱うモジュール (p.365)

fn = '11-0.txt'

# 本文より前の部分（ヘッダ）と本文との境目に記された文字列
markS = '*** START OF THIS PROJECT GUTENBERG EBOOK ALICE’S ADVENTURES IN WONDERLAND ***'

# 本文より後の部分（フッタ）と本文の境目に記された文字列
markE = '*** END OF THIS PROJECT GUTENBERG EBOOK ALICE’S ADVENTURES IN WONDERLAND ***'

# 除去したい記号パターンから正規表現オブジェクトを生成
prog = re.compile("[,\.;:'`?!\(\)\[\]‘’“”]")  # このパターンがどういう意味かは p.368,369 

# 単語の出現回数をカウントするディクショナリ
dWords = {}

with open(fn, 'r', encoding='utf-8') as f:
    skip = True
    n = 1
    for line in f:
        if skip:
            if line.find(markS) >= 0:  # markS を含む行以前をスキップ
                skip = False
            continue
        else:
            if line.find(markE) >= 0:  # markE を含む行以降をスキップ
                break
            #print(n, line, end="")

            # 空白区切りで単語に分割して辞書に登録
            line = line.replace("--", " ")
            for item in line.split():
                item = re.sub(prog, "", item)  # 正規表現を使って記号等を除去

                ### ここで item の文字列を全部小文字に変換しよう

                print(item, end = " ")

                ### ここで辞書に登録しよう．詳しくは課題のページ参照

            n += 1
print()


# 辞書の中身をリストとして取り出し，出現回数でソート
L = list(dWords.items())  # ディクショナリの items() メソッドについては p.195
L.sort(key = lambda x: x[1], reverse=True)  # キーワード引数 key に書いてるものについては p.233,234

# 結果を出力
print("単語数:", len(L))
for i in range(min(len(L), 5)):
    print(i+1, L[i][0], L[i][1])

