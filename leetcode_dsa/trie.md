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

