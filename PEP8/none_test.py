"""
学习PEP8中的小知识点：关于None的判断。
比如说，想要验证一个默认为None的属性是否被设置为其他值了。
一定要用is not None来判断，因为传入的参数也可能被理解为false，就像下面传入了一个空列表。
"""


class A:
    def __init__(self, i=None):
        self.i = i


a = A([])
if a.i:
    print('if a.i')  # 此条语句不会执行，因为空列表在Python里也认为是False

if a.i is not None:
    print('if a.i is not None')  # 正常执行
