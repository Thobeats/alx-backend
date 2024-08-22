#!/usr/bin/python3
""" LRUCache Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache Class
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_age = {}

    def put(self, key, item) -> None:
        """put

        Keyword arguments:
        key -- key value to be store in the cache
        item -- value to be store in cache
        Return: None
        """
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS:
                keys = sorted(self.cache_age.items(),
                              key=lambda kv: (kv[1], kv[0]))
                del self.cache_age[keys[0][0]]
                del self.cache_data[keys[0][0]]
                print("DISCARD: {}".format(keys[0][0]))
            self.cache_data[key] = item
            if len(self.cache_age) > 0:
                self.cache_age[key] = list(self.cache_age.values())[-1] + 1
            else:
                self.cache_age[key] = len(self.cache_age)

    def get(self, key):
        """get

        Keyword arguments:
        key -- the key value to retrieve a data from the cache
        Return: the stored value or None if the key does not exist
        """
        if key and key in self.cache_data:
            if len(self.cache_age) > 0:
                self.cache_age[key] = list(self.cache_age.values())[-1] + 1
            else:
                self.cache_age[key] = len(self.cache_age)
            return self.cache_data.get(key)
        return None
