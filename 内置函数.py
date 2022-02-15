# 绝对值 abs()
a = -1
print(abs(a))
print('-----abs-------')

# all(iterable) 如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
a = [0, 1, 2, 3, 4]
print(all(a))
print('-----all-------')

# any() 只要列表和元组里面一个为真，结果就是TRUE
a = [0, 1, 2, 3, 4]
print(any(a))
print('-----any-------')

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
a = 100
print(bin(a))
print('-----bin-------')

# bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
a = 0
print(bool(a))
print('-----bool-------')

# bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
s = b'alex'
print(type(s))
bytearray(s)
s_arr = bytearray(s)
s_arr[0] = 98
print(s_arr)
print('-----s_arr----12221112222222222222222111---')

# bytes 函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。
# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。
a = bytes([1, 3, 5, 7, 9])
print(a)
print('-----bytes---')


# callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
# 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。

def azb(a, b):
    return a + b


print(callable(azb))

print('-----callable---')

# chr() 用一个整数作参数，返回一个对应的字符。
b = 71
print(chr(b))
print('-----chr---')

# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
s = 'Alex'
print(dir(s))
print('-----dir---')

# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
# eval(expression[, globals[, locals]])
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

x = 7
print(eval('3*x'))
h = '[9,3,2,3,2,1,3]'
print(eval(h))
print(eval(h)[0])
print('-----eval---')

# exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。
# exec(object[, globals[, locals]])
# object：必选参数，表示需要被指定的 Python 代码。它必须是字符串或 code 对象。如果 object 是一个字符串，该字符串会先被解析为一组 Python 语句，然后再执行（除非发生语法错误）。如果 object 是一个 code 对象，那么它只是被简单的执行。
# globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
# locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与 globals 相同的值。
z = 10
expr = """
c = 30
sum = z + b + c
print(sum)
"""


def fuv():
    b = 20
    exec(expr)
    exec(expr, {'z': 5, 'b': 2})
    exec(expr, {'z': 1, 'b': 2}, {'z': 3, 'c': 4})


fuv()
