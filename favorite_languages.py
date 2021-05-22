from collections import OrderedDict
from random import randint
# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。
# 实例名和模块名都采用小写格式，并在单词之间加上下划线
# 创建了一个空的有序字典
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    # Jen's favorite language is Python.
    # Sarah's favorite language is C.
    # Edward's favorite language is Ruby.
    # Phil's favorite language is Python.
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 生成一个随机数 在1-6之间，包含1和6
x = randint(1, 6)
print(x)
