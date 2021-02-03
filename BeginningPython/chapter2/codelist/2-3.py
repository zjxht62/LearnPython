from past.builtins import raw_input

sentence = raw_input("请输入一句话")

screenWidth = 80
textWidth = len(sentence)
boxWidth = textWidth+6

leftMargin = (screenWidth - boxWidth) // 2

print()
print(' ' * leftMargin + '+'  + '-' * (boxWidth-2) +  '+')
print(' ' * leftMargin + '| ' + ' ' * textWidth    + ' |')
print(' ' * leftMargin + '| ' +       sentence     + ' |')
print(' ' * leftMargin + '| ' + ' ' * textWidth    + ' |')
print(' ' * leftMargin + '+'  + '-' * (boxWidth-2) +  '+')

