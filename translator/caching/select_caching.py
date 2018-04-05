import abc


class Caching ( metaclass=abc.ABCMeta ):
    """
    Declare an interface common to all supported caching algorithms. TranslatorApp
    uses this interface to call the apply_cache_strategy defined by child classes of Caching.
     """

    def __init__ ( self ):
        self.cache_strategy = None

    @abc.abstractmethod
    def apply_cache_strategy ( self, **kwargs ):
        pass
