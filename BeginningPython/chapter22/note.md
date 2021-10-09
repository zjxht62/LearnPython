# 第22章：万能的XML

XML可以表示各种信息，竟然连音乐都可以用XML表示。

## 有用的工具

Python提供了对XML的支持  
可以执行下面的代码验证是否具有SAX解析器

```python
from xml.sax import make_parser

parser = make_parser()
```

## 准备工作

我们自己定义了一个存储网页的XML，其中包括website、directory、page元素，示例如下

```xml

<website>
    <page name="index" title="Home Page">
        <h1>Welcome to My Home Page</h1>
        <p>Hi, there. My name is Mr. Gumby, and this is my home page.
            Here are some of my interests:
        </p>
        <ul>
            <li>
                <a href="interests/shouting.html">Shouting</a>
            </li>
            <li>
                <a href="interests/sleeping.html">Sleeping</a>
            </li>
            <li>
                <a href="interests/eating.html">Eating</a>
            </li>
        </ul>
    </page>
    <directory name="interests">
        <page name="shouting" title="Shouting">
            <h1>Mr. Gumby's Shouting Page</h1>
            <p>...</p>
        </page>
        <page name="sleeping" title="Sleeping">
            <h1>Mr. Gumby's Sleeping Page</h1>
            <p>...</p>
        </page>
        <page name="eating" title="Eating">
            <h1>Mr. Gumby's Eating Page</h1>
            <p>...</p>
        </page>
    </directory>
</website>
```
## 初次实现
XML解析常见的方式有两种：SAX和文档对象模式
（DOM）。 SAX解析器读取XML文件并指出发现的内容（文本、标签和属性），但每次只存储
文档的一小部分。这让SAX简单、快捷且占用的内存较少。  
DOM采用的是另一种方法：创建一个表示整个文档的数据结构（文档树）。这种
方法的速度更慢，需要的内存更多，但在需要操作文档的结构时很有用。