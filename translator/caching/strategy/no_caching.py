from werkzeug.contrib.cache import NullCache

from ..select_caching import Caching


class NullCacheStrategy ( Caching ):
    """
    Implement the apply_cache_strategy using the Caching interface.
    """

    def apply_cache_strategy ( self, **kwargs ):
        # default_timeout: the default timeout seconds that is used if no timeout is
        default_timeout = kwargs.get ( 'default_timeout' )
        if not default_timeout:
            default_timeout = 0

        self.cache_strategy = NullCache ( default_timeout=default_timeout )
