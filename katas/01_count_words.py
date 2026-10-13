def count_words(text):
	counts = {}
	text = text.lower()
	text = text.replace('!', '').replace(',', '').replace('?', '').replace('.', '')
	text_split = text.split()
	for word in text_split:
		if word in counts: 
			counts[word] =  counts[word]+1
		else: 
			counts[word] = 1 
	return counts  
print(count_words("Тест, тест! Баг."))
