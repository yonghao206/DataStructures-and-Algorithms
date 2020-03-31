# Trie



### [208. Implement Trie \(Prefix Tree\)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)

Difficulty: **中等**

Implement a trie with `insert`, `search`, and `startsWith` methods.

**Example:**

```text
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

**Note:**

* You may assume that all inputs are consist of lowercase letters `a-z`.
* All inputs are guaranteed to be non-empty strings.

**Solution**

Language: **Python3**

```python
​class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.size = 0

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root 
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        if 'is_word' not in cur:
            self.size += 1
        cur['is_word']=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root 
        for ch in word:
            if ch not in cur:
                return False 
            cur = cur[ch]
        return 'is_word' in cur 

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root 
        for ch in prefix:
            if ch not in cur:
                return False 
            cur = cur[ch]
        return True 

```



### [820. Short Encoding of Words](https://leetcode-cn.com/problems/short-encoding-of-words/)

Difficulty: **中等**

Given a list of words, we may encode it by writing a reference string `S` and a list of indexes `A`.

For example, if the list of words is `["time", "me", "bell"]`, we can write it as `S = "time#bell#"` and `indexes = [0, 2, 5]`.

Then for each index, we will recover the word by reading from the reference string from that index until we reach a `"#"` character.

What is the length of the shortest reference string S possible that encodes the given words?

**Example:**

```text
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
```

**Note:**

1. `1 <= words.length <= 2000`.
2. `1 <= words[i].length <= 7`.
3. Each word has only lowercase letters.

**Solution**

Language: **Python3**

```python
​class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        if not words: return 0
        res = 0
        # time, me, bell 
        # time#bell# [0, 2, 5]=>[4, 9]
        # [0:4], [2:4], [5:9]
        # 几条路径+每条路径的最大值
        trie = Trie()
        words.sort(key = lambda x:-len(x))
        for word in words:
            res += trie.insert(word[::-1])
        return res 

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        new_word = False 
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
                new_word = True 
            cur = cur[ch]
        return len(word)+1 if new_word else 0

```

