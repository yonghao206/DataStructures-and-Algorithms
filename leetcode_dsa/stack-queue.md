# Stack/Queue



### [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

Difficulty: **简单**

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```text
Input: "()"
Output: true
```

**Example 2:**

```text
Input: "()[]{}"
Output: true
```

**Example 3:**

```text
Input: "(]"
Output: false
```

**Example 4:**

```text
Input: "([)]"
Output: false
```

**Example 5:**

```text
Input: "{[]}"
Output: true
```

**Solution**

Language: **Java**

```java
​// peek, push, pop, 
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] chars = s.toCharArray();
        for(char aChar: chars){
            if(stack.size() == 0){
                stack.push(aChar);
            }else if(isSym(stack.peek(), aChar)){
                stack.pop();
            } else{
                stack.push(aChar);
            }
        }
        return stack.size() == 0;
    }

    private boolean isSym(char c1, char c2){
        return (c1=='('&&c2==')') || (c1=='['&&c2==']') || (c1=='{'&&c2=='}');  
    }
}
```

### [71. Simplify Path](https://leetcode-cn.com/problems/simplify-path/)

Difficulty: **中等**

Given an **absolute path** for a file \(Unix-style\), simplify it. Or in other words, convert it to the **canonical path**.

In a UNIX-style file system, a period `.` refers to the current directory. Furthermore, a double period `..` moves the directory up a level.

Note that the returned canonical path must always begin with a slash `/`, and there must be only a single slash `/` between two directory names. The last directory name \(if it exists\) **must not** end with a trailing `/`. Also, the canonical path must be the **shortest** string representing the absolute path.

**Example 1:**

```text
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
```

**Example 2:**

```text
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
```

**Example 3:**

```text
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
```

**Example 4:**

```text
Input: "/a/./b/../../c/"
Output: "/c"
```

**Example 5:**

```text
Input: "/a/../../b/../c//.//"
Output: "/c"
```

**Example 6:**

```text
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
```

**Solution**

Language: **Python3**

```python
​class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        path = path.split('/')
        for item in path:
            if item == "..":
                if stk:
                    stk.pop()
            elif item and item !=".":
                stk.append(item)
        return "/"+"/".join(stk)
```

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



### [232. Implement Queue using Stacks](https://leetcode-cn.com/problems/implement-queue-using-stacks/)

Difficulty: **简单**

Implement the following operations of a queue using stacks.

* push\(x\) -- Push element x to the back of queue.
* pop\(\) -- Removes the element from in front of queue.
* peek\(\) -- Get the front element.
* empty\(\) -- Return whether the queue is empty.

**Example:**

```text
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
```

**Notes:**

* You must use _only_ standard operations of a stack -- which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
* Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque \(double-ended queue\), as long as you use only standard operations of a stack.
* You may assume that all operations are valid \(for example, no pop or peek operations will be called on an empty queue\).

**Solution**

Language: **Python3**

```python
​class MyQueue:
# # 用两个栈来模拟队列，第一个用来push数据，第二个用来pop和peek
# # 在用pop和peak时 当且仅当第二个为空的时候再把第一个instk都放到outstk里面
    def __init__(self):
        self.instk, self.outstk = [], []
    def push(self, x: int) -> None:
        self.instk.append(x)
    def pop(self) -> int:
        if self.outstk:
            return self.outstk.pop()
        else:
            while self.instk:
                self.outstk.append(self.instk.pop())
            return self.outstk.pop()
    def peek(self) -> int:
        if self.outstk:
            return self.outstk[-1]
        else:
            while self.instk:
                self.outstk.append(self.instk.pop())
            return self.outstk[-1]
    def empty(self) -> bool:
        return not self.instk and not self.outstk


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

