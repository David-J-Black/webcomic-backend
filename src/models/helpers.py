

# This one is a doozy, a work in progress
class Singleton(object):
    _singleton_instance = None
    def __new__(cls):
        if cls._singleton_instance is None:
            cls._singleton_instance = super(Singleton, cls).__new__(cls)
            cls._initialized = False
        return cls._singleton_instance
