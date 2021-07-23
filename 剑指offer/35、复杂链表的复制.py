"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

难点：在复制链表的过程中构建新链表各节点的 random 引用指向。

"""
class RandomList:
    def __init__(self,val:int,next:RandomList = None,random:RandomList = None) -> None:
        self.val = val
        self.next = next
        self.random = random

# 使用字典
def copyRandomList(self,head:RandomList) ->RandomList:
    if not head:return 
    dic = {}
    cur = head
    while cur:
        dic[cur] = RandomList(cur.val)
        cur = cur.next
    
    while cur:
        dic[cur].next = dic.get(cur.next)
        dic[cur].random = dic.get(cur.random)
        cur = cur.next
    return dic[head]

# 拼接 拆分
def copyRandomList2(self,head:RandomList) -> RandomList:
    if not head: return 
    cur = head
    # 复制各节点，并构建新链表
    while cur:
        tmp = RandomList(cur.val)
        tmp.next = cur.next
        cur.next = tmp
        cur = tmp.next

    # 构建各个新节点的random指向
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    
    cur = res = head.next
    pre = head
    while cur.next:
        pre.next = pre.next.next
        cur.next = cur.next.next
        pre = pre.next
        cur = cur.next

    pre.next = None
    return res