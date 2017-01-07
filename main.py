#!/bin/env python
#coding=utf-8

import util.app
import model
import conf

if __name__ == "__main__" :
    application = util.app.CronApplication(**conf.settings)
    application.do()
