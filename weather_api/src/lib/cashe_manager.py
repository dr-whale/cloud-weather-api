from .class_description import Singleton
from .redis_client import RedisClient

class CacheManager(Singleton):
    def cache_driver(self):
        return RedisClient()
    
    def remember(self, key, val, time: int = 60):
        return self.cache_driver().set(key, val, time)

    def get(self, key):
        return self.cache_driver().get(key)
    
    def forget(self, key):
        return self.cache_driver().delete(key)
    
    def amnesia(self):
        return self.cache_driver().flushall()
