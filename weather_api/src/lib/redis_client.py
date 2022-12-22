import redis
import json
from .class_description import Singleton

class RedisClient(Singleton):
    def __init__(self):
        self.client = redis.Redis()

    def set(self, key, val, time: int = 60):
        val = json.dumps(val) 
        return self.client.set(key, val, ex = time)
    
    def get(self, key):
        result = self.client.get(key)
        if result == None:
            return result
        return json.loads(self.client.get(key))
    
    def delete(self, key):
        return self.client.delete(key)
    
    def flushall(self):
        return self.client.flushall()
