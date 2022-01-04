#!/usr/bin/env python3
# coding:utf-8
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--compare', '-c', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

parser.add_argument('--compare', '-c', type=str, nargs='+', dest='files')

args = parser.parse_args()
print(args)
