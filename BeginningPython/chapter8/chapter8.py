# 异常
# Python中，每个异常都是某个类的实例

###################################################
# 8.2.1 raise语句
# raise Exception
# raise Exception("我是异常")


#########################################################
# 8.2.2自定义的异常类
class SomeCustomException(Exception):
    pass


###################################################
# 8.3 捕获异常
'''
try:
    x = int(input("请输入x"))
    y = int(input("请输入y"))
    print(x / y)
except ZeroDivisionError:
    print("y不能为0")
'''


# 8.3.1可以继续抛出异常
'''
class MuffledCalcultor:
    muffled = False

    def calc(self, exp):
        try:
            return eval(exp)
        except ZeroDivisionError:
            if self.muffled:
                print('除0不合法')
            else:
                raise


calculator = MuffledCalcultor()
print(calculator.calc('10/2'))  # 5.0
print(calculator.calc('10/0'))  # 抛出异常

calculator.muffled = True
print(calculator.calc('10/0'))  # 除0是不合法的
'''
# 可使用raise ... from ...语句来提供自己的异常上下文，也可使用None来禁用上下文
'''
try:
    1/0
except ZeroDivisionError:
    raise ValueError from ZeroDivisionError

try:
    1/0
except ZeroDivisionError:
    raise ValueError from None
'''

### 8.3.2多个except语句
'''
try:
    x = int(input("请输入x"))
    y = int(input("请输入y"))
    print(x / y)
except ZeroDivisionError:
    print("y不能为0")
except ValueError:
    print("输入内容无法转换为int")
'''

### 8.3.3 一个except多种异常
# 传给except元组来指定多种异常
'''
try:
    x = int(input("请输入x"))
    y = int(input("请输入y"))
    print(x / y)
except (ZeroDivisionError, NameError, ValueError):
    print("出异常了")
'''

### 8.3.4 捕获异常对象
'''
try:
    x = int(input("请输入x"))
    y = int(input("请输入y"))
    print(x / y)
except (ZeroDivisionError, NameError, ValueError) as e:
    print(e)
'''
### 8.3.5 捕获所有异常
'''
try:
    x = int(input("请输入x"))
    y = int(input("请输入y"))
    print(x / y)
except:
    print("捕获所有异常")
'''
# 更好的选择是使用except Exception as e并对异常对象进行检查。这样做将让不是从 Exception派生而来的为数不多的异常成为漏网之鱼，防止将键盘终止事件也作为异常处理掉

### 8.3.6 万事大吉时
# 当没有任何异常发生的时候 通过else来执行代码
'''
while True:
    try:
        x = int(input('请输入x：'))
        y = int(input('请输入y：'))
        value = x / y
        print('x/y is', value)
    except Exception as e:
        print("非法输入:", e)
        print('请重新操作')
    else:
        break

'''
### 8.3.7 最后
'''
x = None
try:
    x = 1/0
finally:
    print("finally")
    del x

'''
## 8.4异常和函数
def faulty():
    raise Exception("Something is wrong")

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print("Exception handled")

handle_exception()  # Exception handled



ignore_exception()
# Traceback (most recent call last):
#   File "E:/zjx/PycharmProjects/LearnPython/BeginningPython/chapter8/chapter8.py", line 146, in <module>
#     ignore_exception()
#   File "E:/zjx/PycharmProjects/LearnPython/BeginningPython/chapter8/chapter8.py", line 137, in ignore_exception
#     faulty()
#   File "E:/zjx/PycharmProjects/LearnPython/BeginningPython/chapter8/chapter8.py", line 134, in faulty
#     raise Exception("Something is wrong")
# Exception: Something is wrong


## 8.5 异常之禅
# 有时需要考虑用异常来提升代码效率
def describePerson(person):
    print("Description of", person['name'])
    print("Age:", person['age'])
    if 'occupation' in person:
        print('Occupation:', person['occupation'])


person = {"name": "zjx", 'age': 26, "occupation": 'Tester'}

describePerson(person)


# 使用异常处理来减少在person中查找occupation的次数
def describePerson2(person):
    print("Description of", person['name'])
    print("Age:", person['age'])
    try:
        print('Occupation:', person['occupation'])
    except KeyError:
        pass


person2 = {"name": "ckx", 'age': 26}
describePerson2(person2)

# 利用异常处理检查对象是否包含特定属性
'''
try:
    obj.write
except AttributeError:
    print('The object is not writable')
else:
    print('The object is writeable')
    
'''

## 8.6 不那么异常的情况
# 通过warning模块中的warn来发出警告
from warnings import warn, filterwarnings

warn("我只是警告一下")

# 可以用函数filterwarnings来抑制发出的警告 比如采取error或ignore
'''
filterwarnings("ignore")
warn("我试试是不是被ignore了") #没有输出

filterwarnings('error')
warn("我被处理成error")
# Traceback (most recent call last):
#   File "/Users/zjx/PycharmProjects/LearnPython/BeginningPython/chapter8/chapter8.py", line 194, in <module>
#     warn("我被处理成error")
# UserWarning: 我被处理成error

'''

filterwarnings("error")
warn("This function is really old...", DeprecationWarning)  # 正常输出为异常

# 根据异常来过滤掉特定类型的警告
filterwarnings("ignore", category=DeprecationWarning)
warn("Another deprecation warning.", DeprecationWarning)  # 不会输出，被过滤了
warn("Something else.")  # 正常输出
