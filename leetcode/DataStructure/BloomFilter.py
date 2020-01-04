#BloomFilter
# 用于检验一个元素是否在一个集合中
# 查询时间和空间效率都远远高于一般的算法
# 缺点是有一定的误识别率和删除困难（模糊的查询）
# 一个元素所对应的二进制元素有一个为0，说明这个元素不在bloomfilter中，如果都为1，也不一定在


from bitarray import bitarray 
import mmh3

class BloomFilter:
	def __init__(self, size, hash_num):
		self.size = size # 总共的元素个数
		self.hash_num = hash_num # 一个元素分成多少个bit的个数
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)

	def add(self, s):
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1

	def lookup(self, s):
		for seed in range(self.hash_num):
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0:
				return "Nope"
		return "Probably"

if __name__ == '__main__':
	bf = BloomFilter(500000, 7)
	bf.add("yonghaoduan")
	print(bf.lookup("yonghaoduan"))
	print(bf.lookup("yhd"))
	