#!/usr/bin/env python
#coding=utf-8

import Base

@Base.route
class H(Base.BaseHandler):

    url = "/"

    def get(self):
        self.render("login.html")
