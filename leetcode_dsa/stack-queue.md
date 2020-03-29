# Stack/Queue



### [150. Evaluate Reverse Polish Notation](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

Difficulty: **中等**

Evaluate the value of an arithmetic expression in .

Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.

**Note:**

* Division between two integers should truncate toward zero.
* The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

**Example 1:**

```text
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**

```text
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:**

```text
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

**Solution**

Language: **Python3**

```python
# T:O(n), S:O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ope = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
        stk = []
        for token in tokens:
            if token in ope:
                t1 = stk.pop()
                t2 = stk.pop()
                # # -6//132 自动下取整，这里我们要上取证，需要int(-6/132)
                stk.append(int(ope[token](int(t2), int(t1))))
            else:
                stk.append(token)
        return int(stk.pop())
```



### [225. Implement Stack using Queues](https://leetcode-cn.com/problems/implement-stack-using-queues/)

Difficulty: **简单**

Implement the following operations of a stack using queues.

* push\(x\) -- Push element x onto stack.
* pop\(\) -- Removes the element on top of the stack.
* top\(\) -- Get the top element.
* empty\(\) -- Return whether the stack is empty.

**Example:**

```text
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```

**Notes:**

* You must use _only_ standard operations of a queue -- which means only `push to back`, `peek/pop from front`, `size`, and `is empty` operations are valid.
* Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque \(double-ended queue\), as long as you use only standard operations of a queue.
* You may assume that all operations are valid \(for example, no pop or top operations will be called on an empty stack\).

**Solution**

Language: **Python3**

```python
​from collections import deque 
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q_push = deque()
        self.q_pop = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q_push.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q_push)>1:
            self.q_pop.append(self.q_push.popleft())
        ret = self.q_push.pop()
        self.q_push, self.q_pop = self.q_pop, self.q_push 
        return ret 

    def top(self) -> int:
        """
        Get the top element.
        """

        while len(self.q_push)>1:
            self.q_pop.append(self.q_push.popleft())
        ret = self.q_push.pop()
        self.q_push, self.q_pop = self.q_pop, self.q_push 
        self.q_push.append(ret)
        return ret 

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q_push and not self.q_pop 


# class MyStack:
#     def __init__(self):
#         self.q_push = collections.deque()
#         self.q_pop = collections.deque()

#     def push(self, x: int) -> None:
#         self.q_push.append(x)
#     def pop(self) -> int:
#         assert not self.empty(), "Empty Stack!"
#         while len(self.q_push) > 1:
#             self.q_pop.append(self.q_push.popleft())
#         ret = self.q_push.popleft()
#         self.q_push, self.q_pop = self.q_pop, self.q_push
#         return ret 
        
#     def top(self) -> int:
#         assert not self.empty(), "Empty Stack!"
#         while len(self.q_push) > 1:
#             self.q_pop.append(self.q_push.popleft())
#         ret = self.q_push.popleft()
#         self.q_pop.append(ret)
#         self.q_push, self.q_pop = self.q_pop, self.q_push
#         return ret 
#     def empty(self) -> bool:
#         return not self.q_push and not self.q_pop
```

