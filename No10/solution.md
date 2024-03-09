## 暴力解法

每成功匹配一个字符，即可更新字符串，和通配符（状态无依赖）

因此，只需要考虑当前字符的匹配

设当前字符为 s[i], 剩余通配符 q，都是list

1. s[i] == q[0] or q[0] == ., if q[1] == *, skip, else pop(0)
2. s[i] != q[0]
    if q[1] == *, pop(0, 1), goto 1
    else return False

if len(q) == 0: True
== 1: False
== 2 and q[-1] == *: True
> 2: False

