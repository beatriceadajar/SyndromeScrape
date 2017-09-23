import tornado.ioloop
import tornado.web
import tornado.autoreload

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(ioloop)
    ioloop.start()
