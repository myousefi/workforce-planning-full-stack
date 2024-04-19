# TODO: Implement the Redis service for the optimization workers
import redis
import os


class RedisService:
    def __init__(self):
        self.redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        self.redis_client = redis.Redis.from_url(self.redis_url)

    def publish(self, channel, message):
        self.redis_client.publish(channel, message)

    def subscribe(self, channel):
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(channel)
        return pubsub

    def get_message(self, pubsub):
        message = pubsub.get_message()
        if message:
            return message["data"]
        return None
