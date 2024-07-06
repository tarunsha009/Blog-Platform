from redis import Redis
from blog_platform.config import BaseConfig

redis_client = Redis.from_url(BaseConfig.REDIS_URL)
