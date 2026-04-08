# 背景  

单链表是用链式存储方式实现的线性表，由节点组成，每个节点包含数据域和指针域。单链表可以带头节点或不带头节点，带头节点的实现更为方便。

# 描述  

实现带头节点的单链表初始化操作。给定链表类型（1表示带头节点，0表示不带头节点），初始化相应的单链表并返回头指针。

# 格式

## 输入  

一个整数 type，表示链表类型：
- 1: 带头节点的单链表
- 0: 不带头节点的单链表

## 输出  

根据输入类型，输出初始化结果：
- 如果 type=1，输出 "HEAD_NODE_INITIALIZED"，表示带头节点的单链表已初始化
- 如果 type=0，输出 "NO_HEAD_NODE_INITIALIZED"，表示不带头节点的单链表已初始化
- 如果 type不是0或1，输出 "INVALID_TYPE"

# 样例

```input1
1
```

```output1
HEAD_NODE_INITIALIZED
```

```input2
0
```

```output2
NO_HEAD_NODE_INITIALIZED
```

```input3
2
```

```output3
INVALID_TYPE
```

# 限制  

每个测试点：时间 1 秒，内存 1024 KiB。
只需要实现初始化逻辑，不需要实际分配内存。