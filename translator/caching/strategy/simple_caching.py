from werkzeug.contrib.cache import SimpleCache

from ..select_caching import Caching


class SimpleCacheStrategy ( Caching ):
    """
    Implement the apply_cache_strategy using the Caching interface.
    """

    def apply_cache_strategy ( self, **kwargs ):
        # threshold: the maximum number of items the cache stores before SimpleCache starts deleting some.
        threshold = kwargs.get ( 'threshold' )
        if not threshold:
            threshold = 0

        # default_timeout: the default timeout seconds that is used if no timeout is
        default_timeout = kwargs.get ( 'default_timeout' )
        if not default_timeout:
            default_timeout = 0

        self.cache_strategy = SimpleCache ( threshold=threshold, default_timeout=default_timeout )
