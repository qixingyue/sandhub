#!/bin/env python
#coding=utf-8

import util.app
import model
import conf

def run(cliapp):
    application = util.app.SandHubApplication([],"",None,**conf.settings)
    application.start(model)
