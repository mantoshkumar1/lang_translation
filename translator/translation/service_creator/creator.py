"""
Using Factory pattern to defines an interface for creating an object, but let subclasses decide \
which class to instantiate. The Factory Method lets a class defer instantiation to subclasses.
"""
import abc


class ServiceCreator ( metaclass=abc.ABCMeta ):
    """
    Declare the factory method, which returns an object of type Provider.
    Call the _get_service_provider method to create a Provider object.
    """

    def __init__ ( self ):
        self.company = self._get_service_provider ( )

    @abc.abstractmethod
    def _get_service_provider ( self ):
        """
        Abstract class that will be concertedly implemented by its children classes.
        :return:
        """
        pass

    def get_translation ( self, text, src_lang, target_lang ):
        """
        This function calls the translate function of the Provider
        :param text: str
        :param src_lang: str
        :param target_lang: str
        :return: translated message (str)
        """
        return self.company.translate ( text, src_lang, target_lang )

    def company_supported_languages ( self ):
        """
        This function gets all the supported language by service provider
        :return: supported lang (list of dict key)
        """
        # returns a list of str
        return self.company.get_supported_languages ( )
