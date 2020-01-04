class Trie:
	# Time: O(1)
	"""
	1. 每一个节点都是一个_Node类，包括了26的长度和is_word的判断
	2. Trie的属性，_root, _size; 方法: add, contains, is_prefix
	3. 快是因为用空间换时间
	"""
	class _Node:
		def __init__(self, is_word = False):
			self.is_word = is_word
			self.next = [None] * 26

	def __init__(self):
		self._root = self._Node()
		self._size = 0

	def get_size(self):
		return self._size 

	def add(self, word):
		cur = self._root 
		for ch in word:
			index = ord(ch.lower()) - ord('a')
			if cur.next[index] is None:
				cur.next[index] = self._Node()
			cur = cur.next[index]
		# make sure the word is added firstly, otherwise do not update size 
		if cur.is_word == False: 
			cur.is_word = True 
			self._size += 1

	# whether the word in the Trie
	def contains(self, word):
		cur = self._root
		for ch in word:
			index = ord(ch.lower()) - ord('a')
			if not cur.next[index]:
				return False
			else:
				cur = cur.next[index]
		return cur.is_word

	# whether some word regard `prefi` as prefix
	def isPrefix(self, prefix):
		cur = self._root
		for ch in prefix:
			index = ord(ch.lower()) - ord('a')
			if not cur.next[index]:
				return False
			cur = cur.next[index]
		return True 



if __name__ == '__main__':
	trie = Trie()
	words = ['panda', 'pandas', 'apple', 'app', 'banana']
	for word in words:
		trie.add(word)

	print('panda', trie.contains('panda'))
	print('pan', trie.contains('pan'))
	print('pana', trie.isPrefix('pana'))
	print('zzz', trie.contains('zzz'))
	print('pand', trie.isPrefix('pand'))