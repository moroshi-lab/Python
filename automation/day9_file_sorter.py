import os
import shutil
from datetime import datetime

# 指定フォルダ内のファイルを更新日ごとにサブフォルダに整理するスクリプト
def sort_files_by_date(folder_path):
    if not os.path.exists(folder_path):
        print("フォルダが存在しません")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # フォルダは無視
        if os.path.isdir(file_path):
            continue

        # 更新日を取得
        modified_time = os.path.getmtime(file_path)
        date_folder = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d")

        # 日付フォルダ作成
        dest_folder = os.path.join(folder_path, date_folder)
        os.makedirs(dest_folder, exist_ok=True)

        # ファイル移動
        shutil.move(file_path, os.path.join(dest_folder, file))

    print("整理完了！")

# 使い方：あなたのフォルダをここに書く
sort_files_by_date("C:/Users/あなた/Downloads")