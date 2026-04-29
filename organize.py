import os
import shutil

# 当前文件夹路径（这个脚本在哪个文件夹，就整理哪个文件夹）
folder = os.path.dirname(os.path.abspath(__file__))

# 扩展名对应的文件夹
mapping = {
    ".jpg": "images", ".jpeg": "images", ".png": "images",
    ".pdf": "docs", ".txt": "docs", ".docx": "docs",
    ".zip": "archives", ".rar": "archives",
    ".mp4": "videos", ".mov": "videos"
}

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if not os.path.isfile(filepath):
        continue   # 注意这里的缩进（4个空格或1个Tab）
    ext = os.path.splitext(filename)[1].lower()
    if ext in mapping:
        target = os.path.join(folder, mapping[ext])
        os.makedirs(target, exist_ok=True)
        shutil.move(filepath, os.path.join(target, filename))
        print(f"Moved: {filename} -> {mapping[ext]}")

print("Done!")