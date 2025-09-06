import os
import re
import sys
import traceback

def modify_tja_file(filepath):
    try:
        # 读取文件内容，使用 utf-8-sig 处理带 BOM 的 UTF-8 文件
        with open(filepath, 'r', encoding='utf-8-sig', errors='replace') as f:
            lines = f.readlines()

        # 存储 TITLE 和 SUBTITLE 相关行的内容
        title = None
        title_ja = None
        title_zh = None
        subtitle = None
        subtitle_ja = None
        subtitle_zh = None

        # 扫描前十行，查找相关字段
        for i, line in enumerate(lines[:10]):
            line = line.strip()
            if re.match(r'^TITLE:', line, re.IGNORECASE):
                title = (i, line)
            elif re.match(r'^TITLEJA:', line, re.IGNORECASE):
                title_ja = (i, line)
            elif re.match(r'^TITLEZH:', line, re.IGNORECASE):
                title_zh = (i, line)
            elif re.match(r'^SUBTITLE:', line, re.IGNORECASE):
                subtitle = (i, line)
            elif re.match(r'^SUBTITLEJA:', line, re.IGNORECASE):
                subtitle_ja = (i, line)
            elif re.match(r'^SUBTITLEZH:', line, re.IGNORECASE):
                subtitle_zh = (i, line)

        modified = False

        # 处理 TITLE 相关字段
        if title and title_ja:
            title_content = title[1][len('TITLE:'):]
            title_ja_content = title_ja[1][len('TITLEJA:'):]
            lines[title[0]] = f'TITLE:{title_ja_content}\n'
            lines[title_ja[0]] = f'TITLEJA:{title_content}\n'
            print(f"  交换 TITLE 和 TITLEJA: {title_content} <-> {title_ja_content}")
            modified = True
        elif title and title_zh:
            title_content = title[1][len('TITLE:'):]
            title_zh_content = title_zh[1][len('TITLEZH:'):]
            lines[title[0]] = f'TITLE:{title_zh_content}\n'
            lines[title_zh[0]] = f'TITLEZH:{title_content}\n'
            print(f"  交换 TITLE 和 TITLEZH: {title_content} <-> {title_zh_content}")
            modified = True

        # 处理 SUBTITLE 相关字段
        if subtitle and subtitle_ja:
            subtitle_content = subtitle[1][len('SUBTITLE:'):]
            subtitle_ja_content = subtitle_ja[1][len('SUBTITLEJA:'):]
            lines[subtitle[0]] = f'SUBTITLE:{subtitle_ja_content}\n'
            lines[subtitle_ja[0]] = f'SUBTITLEJA:{subtitle_content}\n'
            print(f"  交换 SUBTITLE 和 SUBTITLEJA: {subtitle_content} <-> {subtitle_ja_content}")
            modified = True
        elif subtitle and subtitle_zh:
            subtitle_content = subtitle[1][len('SUBTITLE:'):]
            subtitle_zh_content = subtitle_zh[1][len('SUBTITLEZH:'):]
            lines[subtitle[0]] = f'SUBTITLE:{subtitle_zh_content}\n'
            lines[subtitle_zh[0]] = f'SUBTITLEZH:{subtitle_content}\n'
            print(f"  交换 SUBTITLE 和 SUBTITLEZH: {subtitle_content} <-> {subtitle_zh_content}")
            modified = True

        # 如果文件被修改，写回文件，使用 utf-8-sig 编码
        if modified:
            with open(filepath, 'w', encoding='utf-8-sig') as f:
                f.writelines(lines)
            print(f"  文件 {filepath} 已修改")
        else:
            print(f"  文件 {filepath} 无需修改")

    except Exception as e:
        print(f"处理文件 {filepath} 时出错: {str(e)}")
        traceback.print_exc()

def main():
    # 指定文件夹路径
    folder_path = input("请输入要处理的文件夹路径：")
    
    # 确保文件夹存在
    if not os.path.isdir(folder_path):
        print("无效的文件夹路径！")
        return

    # 递归遍历文件夹及其子文件夹中的所有 .tja 文件
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.tja'):
                filepath = os.path.join(root, filename)
                print(f"正在处理文件: {filepath}")
                modify_tja_file(filepath)
    
    print("所有文件处理完成！")

if __name__ == "__main__":
    main()