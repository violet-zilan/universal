def china(start, end):
	for page in range(start, end + 1):
		if page == 1:
			yield 'http://tech.china.com/articles/index.html'
		else:
			yield 'http://tech.china.com/articles/index_' + str(page) + '.html'