# 绝对值 abs()
a = -1
print(abs(a))
print('-----abs-------')

# all(iterable) 如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
a = [0,1,2,3,4]
print(all(a))
print('-----all-------')

# any() 只要列表和元组里面一个为真，结果就是TRUE
a = [0,1,2,3,4]
print(any(a))
print('-----any-------')

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
a = 100
print(bin(a))
print('-----bin-------')

# bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
a = 1
print(bool(a))
print('-----bool-------')

# bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
s = b'alex'
print(type(s))
bytearray(s)
s_arr = bytearray(s)
s_arr[0] = 98
print(s_arr)
print('-----s_arr----12222222222222222222111---')
