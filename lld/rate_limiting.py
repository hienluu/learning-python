from math import ceil
from typing import Dict, List, Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass
import time


class Limiter(ABC):
    @abstractmethod
    def is_allowed(self, key: str) -> bool:
        pass

class TokenBucket:
    def __init__(self, tokens: float, last_refill_time: float):
        self.tokens = tokens
        self.last_refill_time = last_refill_time

class TokenBucketLimiter(Limiter):
    def __init__(self, capacity: int, refill_rate_per_second: int):
        self._capacity = capacity
        self._refill_rate_per_second = refill_rate_per_second
        self._buckets: Dict[str, TokenBucket] = {}

    def _get_or_create_bucket(self, key: str):
        if key not in self._buckets:
            self._buckets[key] = TokenBucket(tokens=self.capacity, last_refill_timestamp=int(time.time() * 1000))

        return self._buckets[key]


    def allow(self, key: str):
        bucket = self._get_or_create_bucket(key)

        now = int(time.time() * 1000) # current time in milliseconds
        elapsed = now - bucket.last_refill_time # time since last refill in milliseconds
        tokens_to_add = (elapsed * self._refill_rate_per_second) / 1000 # calculate how many tokens to add based on elapsed time
        bucket.tokens = min(bucket.tokens + tokens_to_add, self._capacity)
        bucket.last_refill_time = now # update last refill time

        if bucket.tokens >= 1:
            bucket.tokens -= 1 # consume a token
            remaining = int(bucket.tokens)
            return RateLimitResult(allowed=True, remaining=remaining, retry_after_ms=None)
        else:                    
            tokens_needed = 1 - bucket.tokens
            retry_after_ms = ceil ((tokens_needed * 1000) / self._refill_rate_per_second)
            return RateLimitResult(allowed=False, remaining=0, retry_after_ms=retry_after_ms)

@dataclass 
class RateLimitResult:
    allowed: bool
    remaining: int
    retry_after_ms: Optional[int]

    def is_allowed(self) -> bool:
        return self.allowed
    
    def get_remaining(self) -> int:
        return self.remaining
    
    def get_retry_after_ms(self) -> Optional[int]:
        return self.retry_after_ms


class LimiterFactory:
    def create(self, config: Dict):
        algorithm = config.get("algorithm")
        algo_config = config.get("algoConfig", {})

        if algorithm == "TokenBucket":
            return TokenBucketLimiter(
                capacity=algo_config.get("capacity", 0), 
                refill_rate_per_second=algo_config.get("refillRatePerSecond", 0)
            )
        
        raise ValueError(f"Unsupported algorithm: {algorithm}")

class RateLimiter:
    def __init__(self, configs: List[Dict], default_config: Dict):
        factory = LimiterFactory()
        self._limiters: Dict[str, Limiter] = {}

        for config in configs:
            endpoint = config.get("endpoint")
            if endpoint is None:
                continue
            limiter = factory.create(config)
            self.limiter[endpoint] = limiter

        self._default_limiter = factory.create(default_config)