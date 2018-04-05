from ..provider import Provider


class BingProvider ( Provider ):
    """
        Implements the Provider interface.
    """

    def __init__ ( self ):
        self.translator = None
        self.lang_codes = None

    def translate ( self, text, src_lang, target_lang ):
        """
        This function will implement functionality to get translated message from bing \
        in case of any error, it shoudld abort the calls and returns appropriate HTTP status code.
        :param text: str
        :param src_lang: str
        :param dest_lang: str
        :return: translated text (str)
        """
        raise NotImplementedError

    def get_supported_languages ( self ):
        """
        It should return the list of languages supported by Bing Translation
        :return: list of str
        """
        raise NotImplementedError

    def get_supported_language_code ( self ):
        """
        It should return a dict with supported language by Bing Translation and their code
        :return:
        """
        raise NotImplementedError
