class crawler:
	def __init__(self, dbname):
		pass

	def __del__(self):
		pass
	
	def db_commit(self):
		pass

	def get_entry_id(self, table, field, value, create_new=True):
		return None
	
	def add_to_index(self, url, soup):
		print("Indexing %s", url)

	def get_text_only(self, soup):
		return None

	def separate_words(self, text):
		return None

	def is_indexed(self, url):
		return False

	# 두 페이지 간의 링크를 추가
	def add_link_ref(self, url_from, url_to, link_text):
		pass

	# 페이지 목록으로 시작해서 BFS를 주어진 깊이만큼
	# 그 페이지들을 색인
	def crawl(self, pages, depth=2):
		pass

	def create_index_tables(self):
		pass
