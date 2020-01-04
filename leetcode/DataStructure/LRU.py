from collections import OrderedDict

class LRUCache(object):
	def __init__(self, capacity):
		self.dic = OrderedDict()
		self.remain = capacity

	def get(self, key):
		if key not in self.dic:
			return -1
		v = self.dic.pop(key)
		self.dic[key] = v 
		return v 

	def put(self, key, value):
		if key in self.dic:
			self.dic.pop(key)
		else:
			if self.remain > 0:
				self.remain -= 1
			else:
				self.dic.popitem(last = False) # 这里是FIFO当last=False
		self.dic[key] = value 

if __name__ == '__main__':
