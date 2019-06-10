import json
import redis

class redis_deal:
    def __init__(self, host = 'localhost', port = '6379'):
        self.port = port
        self.host = host
        self.link = redis.StrictRedis(host=self.host, port=self.port, decode_responses=True)

    def insert_to_redis(self, key, datas):
        if self.link.exists(key):
            self.link.delete(key)
        self.link.set(key, json.dumps(datas))

    def read_from_redis(self, key):
        if not self.link.exists(key):
            return None
        else:
            return json.loads(self.link.get(key))

if __name__ == '__main__':
    redis_dealer = redis_deal()
    redis_dealer.insert_to_redis('test_wxw', {'aa': 1, 'bb': 2})
    keys = str(redis_dealer.read_from_redis('test_wxw'))
    print(keys)




