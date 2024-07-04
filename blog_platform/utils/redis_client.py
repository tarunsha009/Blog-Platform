# blog_platform/redis_client.py

from redis import Redis
from blog_platform.config import BaseConfig

# Initialize Redis client
# config = config_by_name['dev']  # Adjust as necessary for your environment
redis_client = Redis.from_url(BaseConfig.REDIS_URL)
