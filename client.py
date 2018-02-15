#!/usr/bin/env

import datetime
import json
import hashlib
import urllib.request as urllib2
import urllib.parse

report_data = {
  "xmpp_host": hashlib.sha1("127.0.0.1".encode("utf-8")).hexdigest(),
  "xmpp_username": hashlib.sha1("xmpp_username".encode("utf-8")).hexdigest(),
  "time": str(datetime.datetime.now()), "controller": "test_client", 
  "version": 3}

data = json.dumps(report_data).encode('utf8')

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
except Exception as error:
  print("Status report failed. Error is {0}".format(error))

