import urllib


class URL:
	def __init__(self, host, port=None, path=None, params=None):
		self.host = host
		self.port = port
		self.path = path
		self.params = params

	def __str__(self):
		url = "http://" + self.host
		if self.port is not None:
			url += ":" + self.port
		url += "/"
		if self.path is not None:
			url += self.path
		if self.params is not None:
			url += "?"
			url += urllib.urlencode(self.params)
		return url