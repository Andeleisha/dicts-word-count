# put your code here.
def build_dict(fname):
	"""Given a file, builds a dictionary of each word in the file."""
	
	with open(fname) as file:

		word_count_dict = {}

		for line in file:
			line = line.rstrip()
			# line = line.rstrip('"')
			line =line.split(' ')
			for word in line:
				word = word.strip('"!.,?_;():')
				word = word.lower()
				word_count_dict[word] = word_count_dict.get(word, 0) + 1
		#return word_count_dict

		for each in word_count_dict:
			count = word_count_dict[each]
			print(each, count)

		return






build_dict("twain.txt")