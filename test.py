from sandbox import *
from google.appengine.tools.devappserver2 import runtime_config_pb2

config = runtime_config_pb2.Config()
config.application_root = './temp'
enable_sandbox(config)


import os
for path, dirs, files in os.walk('./'):
    print path
    for f in files:
        print f
fileHandler = open('abc.txt', 'r')
print str(fileHandler)
