#!/usr/bin/env python3

import argparse
import glob

def replace_str(file_path: str, replaced: str, replacing: str) -> None:
    with open(file_path, 'r') as f:
        pre_str = f.read()
    post_str = pre_str.replace(replaced, replacing)
    with open(file_path, 'w') as f:
        f.write(post_str)

parser = argparse.ArgumentParser()
parser.add_argument("--tar_file_path", type=str, help="target file path")
parser.add_argument("--str_replaced", type=str, help="a string replaced")
parser.add_argument("--str_replacing", type=str, help="a string replacing")
parser.add_argument('--all', action='store_true')
args = parser.parse_args()

if args.all:
    for a, b in [('、', ', '), ('。', '.')]:
        for p in glob.glob("tex/*"):
            replace_str(p, a, b)
else:
    replace_str(args.tar_file_path, args.str_replaced, args.str_replacing)