#!/bin/env python
#coding=utf-8

import os

root = os.path.abspath(".")

settings = {
    "debug":True,
    'static_path':os.path.join(root, "static"),
    'template_path':os.path.join(root, "views"),
    'db_string':"mysql+mysqldb://sandhub:sm87Mp*#@@localhost/sandhub?charset=utf8",
    "port":9099
}
