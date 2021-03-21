class Config(object):
    ENV='Production'
    TESTING = False
    DEBUG = False
    SHIPPING = "shipping"
    DISTANCE = 0
    WEIGHT = 0
    TIMES = 1

class LocalConfig(object):
    ENV='Development'
    TESTING = True
    DEBUG = True
    SHIPPING = "shipping"
    DISTANCE = 0
    WEIGHT = 0
    TIMES = 1