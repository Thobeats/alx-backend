#!/usr/bin/python3
""" FIFOCache Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache Class
    """

    def put(self, key, item) -> None:
        """put

        Keyword arguments:
        key -- key value to be store in the cache
        item -- value to be store in cache
        Return: None
        """
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                del self.cache_data[keys[0]]
                print("DISCARD: {}".format(keys[0]))
            self.cache_data[key] = item

    def get(self, key):
        """get

        Keyword arguments:
        key -- the key value to retrieve a data from the cache
        Return: the stored value or None if the key does not exist
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
