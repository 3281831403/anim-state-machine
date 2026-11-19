# 动画状态机：转移、条件与层

角色在 idle/run/attack 之间抖动、事件丢失：转移表只认当前状态，条件求值没有全匹配，混合权重没归一化，打断优先级反了，事件没有按状态派发，层遮罩位运算错，同步相位没有取模，冷却判断用了绝对值，缓存键漏了状态机名，批量状态只提交一半。

## 目录结构

```
README.md
conftest.py
.gitignore
animation/__init__.py
animation/state_machine.py
tests/test_state_machine.py
```

## 当前状态

`animation/state_machine.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_state_machine.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 转移按当前状态查表
2. 条件全匹配才转移
3. 混合权重归一化
4. 打断优先级比较
5. 事件按状态派发
6. 层遮罩位运算
7. 同步相位取模
8. 冷却按时间差
9. 缓存键含状态机名
10. 批量状态统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `animation/state_machine.py`
后 15 条用例应全部通过。
