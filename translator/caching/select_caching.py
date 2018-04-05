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

    def get_translation_from_cache ( self, text, src_lang, target_lang ):
        """
        If a translated text for a same request [wrto a key: (text, src_lang, target_lang)] has earlier \
        been made and it is available in cache, then this function fetches the result from cache. \
        Otherwise it returns None.

        Reference: # http://flask.pocoo.org/docs/0.12/patterns/caching/

        :param text: The text that needs to be translated to target_lang (str)
        :param src_lang: str
        :param target_lang: str
        :return: cached translated text (str)
        """
        item_key = (text, src_lang, target_lang)
        cached_translated_text = self.cache_strategy.get ( item_key )
        return cached_translated_text

    def set_translation_to_cache ( self, text, src_lang, target_lang, translated_text ):
        """
        This function set the translated_text wrto a key: (text, src_lang, target_lang) into the cache. \
        Reference: # http://flask.pocoo.org/docs/0.12/patterns/caching/

        :param text: The text that was needed to be translated to target_lang (str)
        :param src_lang: str
        :param target_lang: str
        :param translated_text: str
        :return:
        """
        if not translated_text: return

        item_key = (text, src_lang, target_lang)
        self.cache_strategy.set ( item_key, translated_text )
