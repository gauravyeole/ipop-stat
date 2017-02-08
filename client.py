#!/usr/bin/env python

import datetime
import json
import hashlib
import urllib2

data = json.dumps({
  "xmpp_host" : hashlib.sha1("127.0.0.1").hexdigest(),
  "uid": hashlib.sha1("abcd").hexdigest(),
  "xmpp_username":hashlib.sha1("username").hexdigest(), 
  "time": str(datetime.datetime.now()), "controller": "test_client", 
  "version": 3})

try:
  url="http://" + "127.0.0.1" + ":" +str(8080) + "/api/submit"
  req = urllib2.Request(url=url, data=data)
  req.add_header("Content-Type", "application/json")
  res = urllib2.urlopen(req)
  print("Succesfully reported status to the stat-server({0})."
    ".\nHTTP response code:{1}, msg:{2}".format(url, res.getcode(),\
    res.read()))
  if res.getcode() != 200:
    raise
except:
  print("Status report failed.")

