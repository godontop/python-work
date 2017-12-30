# 001——统计文件text中字符“char”出现的次数
def count_char(text, char):
	count = 0
	for c in text:
		if c == char:
			count += 1
	return count