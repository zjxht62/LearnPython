# 给python脚本结尾增加行号                                  #  1
import fileinput                                   #  2
for line in fileinput.input(inplace=True):         #  3
    line = line.rstrip()                           #  4
    num = fileinput.lineno()                       #  5
    print('{:<50} # {:2d}'.format(line, num))      #  6
                                                   #  7
