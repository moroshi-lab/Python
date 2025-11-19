# フォルダ内の.txtファイルを整理済みフォルダに移動するスクリプト

import os, shutil

src = "C:/Users/username/OneDrive/デスクトップ/整理前"
dst = "C:/Users/username/OneDrive/デスクトップ/整理済み"

if not os.path.exists(dst):
    os.makedirs(dst)

for file in os.listdir(src):
    if file.endswith(".txt"):
        shutil.move(os.path.join(src, file), dst)

print("移動完了")