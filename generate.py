
#!/usr/bin/env python3
import sys
import subprocess

# 引数チェック
try:
    contest = sys.argv[1]  # 開催コンテスト番号
except IndexError:
    print('Error: コンテストの番号を入力してください')
    exit()

# ファイル名
files = [f'{contest}-{problem}.py' for problem in ['a', 'b', 'c', 'd']]

template = """def main():
    pass
if __name__ == "__main__":
    main()
"""

# ファイルの生成
for file in files:
    with open(file, 'w') as f:
        f.write(template)

# VSCodeでファイルを開く
for file in files:
    subprocess.run(['code', file])