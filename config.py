class Config(object):
    ENV='Production'
    TESTING = False
    DEBUG = False
    HELLO = "world"
    TIMES = 1

class LocalConfig(object):
    ENV='Development'
    TESTING = True
    DEBUG = True
    HELLO = "world"
    TIMES = 1