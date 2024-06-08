#!/usr/bin/env python3

import argparse
from explorer.explorer import FunnyJsonExplorer

def run_explorer(json_file, style, icon):
    # 加载 JSON 文件
    with open(json_file, 'r') as f:
        json_data = f.read()
    
    # 创建并运行 FunnyJsonExplorer
    explorer = FunnyJsonExplorer(style, icon)
    explorer._load(json_data)
    explorer.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', required=True, help='Visualization style')
    parser.add_argument('-i', '--icon', required=True, help='Icon family')

    args = parser.parse_args()

    run_explorer(args.file, args.style, args.icon)
