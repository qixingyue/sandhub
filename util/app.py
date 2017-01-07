#!/bin/env python
#coding=utf-8

import tornado.web
import tornado.ioloop
from tornado.options import define, options

class SandHubApplication(tornado.web.Application):

    def __init__(self, handlers=None, default_host="", transforms=None,
                 **settings):
        self.init_options(**settings)
        tornado.web.Application.__init__(self,[],"",None,**settings)

    def init_options(self,**settings):
        pass

    def init_model(self,model):
        model.init_engine(self)

    def start(self,model):
        self.model = model
        self.init_model(model)
        self.listen(self.settings["port"])
        import handlers.Base
        handlers.Base.set_app(self)
        handlers.Base.import_handlers()
        print "start 0.0.0.0:%d" % (self.settings['port'])
        tornado.ioloop.IOLoop.instance().start()

    def release(self):
        self.model.release



class CronApplication:

    def __init__(self,**settings):
        define("task", default="web", help="task you want to do" )
        tornado.options.parse_command_line()
        self.settings = settings

    def do(self):
        import importlib
        try:
            command = importlib.import_module("command." + options.task)
            if hasattr(command,"run") and hasattr(command.run,"__call__") :
                command.app = self
                command.run(self)
            else :
                print "command : %s  does not have run method!" % (options.task)

        except Exception,ex:
            print ex

