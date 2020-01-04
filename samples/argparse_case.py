# https://docs.python.org/zh-cn/dev/library/argparse.html

import argparse
parser = argparse.ArgumentParser()
parser.description='hyperparameters'
parser.add_argument("-a", "--lr", help="我是A", type=float)
parser.add_argument("-b", "--epoch", help="我是B", type=int)
args = parser.parse_args()
print(args.lr)
print(args.epoch)


