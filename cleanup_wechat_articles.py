#!/usr/bin/env python3
"""
清理微信公众号导出的Markdown文件
删除CSS样式、元数据、原文地址、结尾的出品信息和交互按钮
"""

import os
import re
import glob
from pathlib import Path

def cleanup_file(file_path):
    """清理单个文件"""
    print(f"处理: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        print(f"  文件为空，跳过")
        return

    new_lines = []
    in_footer = False  # 是否进入页脚区域
    skip_next = False  # 是否跳过下一行（用于处理多行块）

    for i, line in enumerate(lines):
        # 跳过标记为跳过的行
        if skip_next:
            skip_next = False
            continue

        # 1. 删除第一行的CSS样式（通常包含 * { margin: 0; ...）
        if i == 0 and ('* {' in line or 'margin:' in line or 'padding:' in line):
            print(f"  删除CSS样式行")
            continue

        # 2. 删除元数据行（包含"原创"和公众号名称）
        if '原创' in line and ('吉林大学地球探测科学与技术学院' in line or '新媒体中心' in line or '欢迎关注' in line):
            print(f"  删除元数据行")
            continue

        # 3. 删除原文地址引用块
        if line.strip().startswith('> 原文地址:'):
            print(f"  删除原文地址行")
            continue

        # 4. 检测是否进入页脚区域
        # 页脚通常以"出品 |"、"撰稿 |"、"编辑 |"、"审阅 |"、"指导老师 |"开始
        if any(line.strip().startswith(prefix) for prefix in
               ['出品 |', '撰稿 |', '编辑 |', '审阅 |', '指导老师 |', '文字 |', '摄影 |']):
            in_footer = True

        # 5. 如果进入页脚区域，跳过这些行
        if in_footer:
            # 检测页脚结束：包含"一起为"、"点赞"、"分享"、"推荐"等
            if '一起为' in line or '点赞' in line or '分享' in line or '推荐' in line:
                print(f"  进入交互按钮区域，跳过剩余行")
                # 跳过当前行及之后的所有行
                break
            # 否则跳过当前行
            print(f"  删除页脚行: {line.strip()[:50]}...")
            continue

        # 6. 删除SVG data URL行（通常包含data:image/svg+xml）
        if 'data:image/svg+xml' in line:
            print(f"  删除SVG data URL行")
            continue

        # 7. 删除阅读统计行（包含"阅读![](data:image/svg+xml)"）
        if '阅读![](' in line and 'data:image/svg+xml' in line:
            print(f"  删除阅读统计行")
            continue

        # 8. 删除学院二维码行（包含"吉林大学地球探测科学与技术学院"和二维码）
        if '吉林大学地球探测科学与技术学院' in line and 'wx_fmt=png' in line:
            print(f"  删除学院二维码行")
            continue

        # 9. 删除空行过多的情况（连续3个以上空行保留为2个）
        if line.strip() == '':
            if len(new_lines) >= 2 and new_lines[-1].strip() == '' and new_lines[-2].strip() == '':
                print(f"  删除多余空行")
                continue

        # 保留该行
        new_lines.append(line)

    # 写入清理后的内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"  完成，保留 {len(new_lines)} 行")

def main():
    # 目标目录
    target_dir = r"D:\JLU-GIS\01-学习篇\02.实习篇\公众号-兴城实习"

    # 获取所有.md文件
    md_files = glob.glob(os.path.join(target_dir, "*.md"))

    print(f"找到 {len(md_files)} 个Markdown文件")

    for md_file in md_files:
        try:
            cleanup_file(md_file)
        except Exception as e:
            print(f"  处理失败: {e}")

    print("\n清理完成！")

if __name__ == '__main__':
    main()