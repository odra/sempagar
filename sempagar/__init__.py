# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import pymongo
import redis
import utils
import sdks
import config
import handlers
import sys
sys.dont_write_bytecode = True


#redis://redistogo:742b9896c3849731f37ad20b60a49310@cobia.redistogo.com:9608/

redis = redis.StrictRedis(host='cobia.redistogo.com', port='9608', password='742b9896c3849731f37ad20b60a49310', db='redistogo')

routes = []
#users
routes.append((r'/users', handlers.Users))
routes.append((r'/users/login', handlers.UserSession))
routes.append((r'/users/logout', handlers.UserSession))
routes.append((r'/users/profile', handlers.UserProfile))

application = tornado.web.Application(routes, mongo=mongo, redis=redis, debug=True)

def run(port=5000):
	print 'Starting ark server....'
	application.listen(port)
	print 'Running on port %s' % port
	tornado.ioloop.IOLoop.instance().start()
