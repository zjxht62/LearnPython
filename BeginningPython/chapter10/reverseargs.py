# 反转命令行参数

import sys

args = sys.argv[1:]
args.reverse()
print(' '.join(args))