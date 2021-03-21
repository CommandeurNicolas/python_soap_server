class Config(object):
    ENV='Production'
    TESTING = False
    DEBUG = False
    API_HANDLER = '/soap/'
    WSDL_PATH = './wsdl/'
    HELLO = "world"
    TIMES = 1

class LocalConfig(object):
    ENV='Development'
    TESTING = True
    DEBUG = True
    API_HANDLER = '/soap/'
    WSDL_PATH = './wsdl/'
    HELLO = "world"
    TIMES = 1