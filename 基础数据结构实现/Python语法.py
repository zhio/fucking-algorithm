reduce(function, iterable[, initializer])
    reduce(lambda x,y:x * y,ns) # 数组之乘积 (ns[0] * ns[1]) * ns[2]
    reduce(lambda x,y:x + y,ns) # 数组之和
# 记忆化搜索
@functools.lru_cache(None)
res = helper(0,N,0)
helper.cache_clear()
tuple(ns) 可以hash做参数
# 大根堆
q = list(map(lambda x:-x,ns))
heapq.heapify(q)
key = -heapq.heappop(q)
# 过滤函数
filter(function, iterable)
    filter(lambda x: 2 < x < 10 and x % 2 == 0, range(18))
    filter(dfs, range(len(graph)))
# 除数
div, mod = divmod(sum(ns), 4)
random.randint(i,len(self.ns)-1)
#第一个降序，第二个升序
sorted(pss,key = lambda x:[x[0],-x[1]])

# 不可变str 常见函数
split(sep=None, maxsplit=-1)  # 以sep来分割字符串
strip([chars])  # 去除首末两端的字符, 默认是 \r,\n," "
join(iterable)  # 将iterable内的元素拼接成字符串,如','.join(['leet', 'code'])="leet,code"
replace(old, new[, count])  # 字符串替换, old to new
count(sub[, start[, end]])  # 统计子字符串sub的个数
startswith(prefix[, start[, end]])  # 以prefix开始的字符串
endswith(suffix[, start[, end]])  # 以suffix结束的字符串
cs in chrs: # chrs 中包含 cs

# deque 常见函数
queue = deque([iterable[, maxlen]])
queue.append(val)  # 往右边添加一个元素
queue.appendleft(val)  # 往左边添加一个元素
queue.clear()  # 清空队列
queue.count(val)  # 返回指定元素的出现次数
queue.insert(val[, start[, stop]])  # 在指定位置插入元素
queue.pop()  # 获取最右边一个元素，并在队列中删除
queue.popleft()  # 获取最左边一个元素，并在队列中删除
queue.reverse()  # 队列反转
queue.remove(val)  # 删除指定元素
queue.rotate(n=1)  # 把右边元素放到左边

# list 常见函数
lst.sort(*, key=None, reverse=False)
lst.append(val)  # 也可以 lst = lst + [val]
lst.clear()  # 清空列表
lst.count(val)  # val个数
lst.pop(val=lst[-1])  # (默认)从末端移除一个值
lst.remove(val)  # 移除 val
lst.reverse()  # 反转
lst.insert(i, val)  # 在 i 处插入 val

# 字典dict 常见函数
d = defaultdict(lambda : value) # 取到不存在的值时不会报错，用{}时、需要设置get的default值
pop(key[, default])  # 通过键去删除键值对(若没有该键则返回default(没有设置default则报错))
setdefault(key[, default])  # 设置默认值
update([other])  # 批量添加
get(key[, default])  # 通过键获取值(若没有该键可设置默认值, 预防报错)
clear()  # 清空字典
keys()  # 将字典的键组成新的可迭代对象
values()  # 将字典中的值组成新的可迭代对象
items()  # 将字典的键值对凑成一个个元组, 组成新的可迭代对象
dict1 = dict2 #两个字典完全相等，滑窗时可用

# 集合set 常见函数
s = set(lambda : value)
add(elem)  # 向集合中添加数据
update(*others)  # 迭代着增加
clear()  # 清空集合
discard(elem)  # 删除集合中指定的值(不存在则不删除)

# 堆heapq 常见函数
heap = []  # 建堆
heapq.heappush(heap,item)  # 往堆中插入新值
heapq.heappop(heap)  # 弹出最小的值
heap[0]  # 查看堆中最小的值, 不弹出
heapq.heapify(x)  # 以线性时间将一个列表转为堆
heapq.heappoppush(heap, item)  # 弹出最小的值.并且将新的值插入其中.
heapq.merge(*iterables, key=None, reverse=False)  # 将多个堆进行合并
heapq.nlargest(n, iterable, key=None)  # 从堆中找出最大的 n 个数，key的作用和sorted( )方法里面的key类似, 用列表元素的某个属性和函数作为关键字
heapq.nsmallest(n, iterable, key=None)  # 从堆中找出最小的 n 个数, 与 nlargest 相反


# 二分查找函数
bisect.bisect_left(ps, T, L=0, R=len(ns))  #二分左边界
bisect.bisect_right(ps, T, L=0, R=len(ns)) #二分右边界
bisect.insort_left(a, x, lo=0, hi=len(a))  # 二分插入到左侧
bisect.insort_right(a, x, lo=0, hi=len(a)) # 二分插入到右侧

# bit操作
& 符号，x & y ，会将两个十进制数在二进制下进行与运算
| 符号，x | y ，会将两个十进制数在二进制下进行或运算
^ 符号，x ^ y ，会将两个十进制数在二进制下进行异或运算
<< 符号，x << y 左移操作，最右边用 0 填充
>> 符号，x >> y 右移操作，最左边用 0 填充
~ 符号，~x ，按位取反操作，将 x 在二进制下的每一位取反

# 整数集合set位运算
# 整数集合做标志时，可以做参数加速运算
vstd 访问 i ：vstd | (1 << i)
vstd 离开 i ：vstd & ~(1 << i)
vstd 不包含 i : not vstd & (1 << i)

并集 ：A | B
交集 ：A & B
全集 ：(1 << n) - 1
补集 ：((1 << n) - 1) ^ A
子集 ：(A & B) == B
判断是否是 2 的幂 ：A & (A - 1) == 0
最低位的 1 变为 0 ：n &= (n - 1)
        while n:
            n &= n - 1
            ret += 1
最低位的 1：A & (-A)，最低位的 1 一般记为 lowbit(A)

# ^     ：匹配字符串开头
# [\+\-]：代表一个+字符或-字符
# ?     ：前面一个字符可有可无
# \d    ：一个数字
# +     ：前面一个字符的一个或多个
# \D    ：一个非数字字符
# *     ：前面一个字符的0个或多个
matches = re.match('[ ]*([+-]?\d+)', s)
