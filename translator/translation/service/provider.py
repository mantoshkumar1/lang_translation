import abc


class Provider ( metaclass=abc.ABCMeta ):
    """
    Define the interface of objects the _get_service_provider method creates.
    """

    @abc.abstractmethod
    def translate ( self, text, src_lang, target_lang ):
        """
        Abstract class that will be concertedly implemented by its children classes.
        :param text: str
        :param src_lang: str
        :param target_lang: str
        :return:
        """
        pass

    @abc.abstractmethod
    def get_supported_language_code ( self ):
        """
        Abstract class that will be concertedly implemented by its children classes.
        :return:
        """
        pass

    @abc.abstractmethod
    def get_supported_languages ( self ):
        """
        Abstract class that will be concertedly implemented by its children classes.
        :return:
        """
        pass
