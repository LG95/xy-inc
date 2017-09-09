from collections.abc import Callable
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

""" Module implementing the RESTful server. """

class RESTfulRequestHandler(BaseHTTPRequestHandler):
	""" Class implementing how the server handles RESTful methods. """

	__BASE_URI = "xy-inc/points"
	__methods = dict()	# methods exposed through REST

	@classmethod
	def register(cls, services):
		""" Register the public methods of services to expose. """

		# add all public (doesn't start with _) methods (Callable instances)
		aux = [(name, getattr(services, name)) for name in dir(services)]
		cls.__methods.update((name, value) for name, value in aux
							 if name[0] != "_" and isinstance(value, Callable))

	def do_GET(self):
		""" Treat HTTP GET requests. """

		if self.__BASE_URI not in self.path:
			self.send_error(404, self.path + " not found. Try /" + self.__BASE_URI)
			return

		questions = self.path.count("?")

		if questions > 1:
			self.send_error(406, "Too many ? in " + self.path)
			return

		# separate parameters from the rest of path
		method, params = self.path.split("?") if questions == 1 else (self.path, None)
		method = method.split("/")[-1]	# get method name from the last /

		if params is not None:	# convert key-value pairs into dictionary
			params = dict(param.split("=") for param in params.split("&"))
		else: params = dict()	# no parameters

		try: result = self.__methods[method](**params)
		except KeyError: self.send_error(405, "No method " + method)
		except (AssertionError, TypeError) as e:
			self.send_error(406, str(e))	# error due to parameters
		else:
			if result is None: result = []	# no return message
			self.send_response(200)
			self.send_header("Content-type", "text")
			self.end_headers()

			# send each result in a line by itself
			for name in result: self.wfile.write(bytes(name, "utf-8") + b"\r\n")

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	""" Class implementing a multithread HTTP server. """

	pass	# only needs inherited behavior

def serve(services, host = "localhost", port = 8080):
	""" Run a server at host:port exposing methods from services. """

	RESTfulRequestHandler.register(services)
	httpd = ThreadedHTTPServer((host, port), RESTfulRequestHandler)

	try: httpd.serve_forever()
	except KeyboardInterrupt: pass
