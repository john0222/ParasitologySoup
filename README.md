# 簡介
這是一個用於從 Google 圖片搜索中下載圖像的 Python 腳本。該腳本可以根據用戶提供的關鍵詞下載指定數量的圖像，並將圖像保存到檔案夾中。下載過程中的每個步驟都將記錄在日志文件中，以便後續查閱。

# 安裝要求

 - Python 3.x
- requests 庫
- beautifulsoup4 庫
- 可以通過以下命令安裝所需的包：

```bash=
pip install requests beautifulsoup4
```

# 使用方法

將項目代碼複製到本機或下載到本地文件夾中。

設置日志記錄模組（可選）：

如果你不用自定義的 datalogger 模組，你需要搞一個類似功能的模組。
你可以創一個簡單的 datalogger.py 文件，包含以下函數：

```python=
Copy code
def create_log():
    with open('log.txt', 'w') as f:
        f.write('')

def log(message):
    with open('log.txt', 'a') as f:
        f.write(message + '\n')

```

# 運行
在終端或命令行中導航到腳本所在的目錄，並運行：

```
python script_name.py
```
按照提示輸入信息：
其中 script_name.py 是你保存的文件名。

輸入用於搜索的關鍵詞（多個關鍵字用逗號分隔）。
輸入每個關鍵詞下要下載的圖像數量。
例如：

```pytho=
Enter keywords for the images (comma-separated): cat,dog
Enter the number of images to download per keyword: 5
#這將下載 5 張貓的圖片和 5 張狗的圖片。
```

# 查看結果

下載的圖像將被保存在 images/ 文件夾中，以關鍵詞為子文件夾進行分類。例如，images/cat/ 和 images/dog/。

日誌文件 log.txt 將記錄所有操作的詳細流程，包括成功下載的圖像和出現的任何錯誤。
