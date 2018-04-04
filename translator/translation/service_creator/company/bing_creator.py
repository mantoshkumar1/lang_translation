from translator.translation.service.company.bing import BingProvider
from translator.translation.service_creator.creator import ServiceCreator


class BingServiceCreator ( ServiceCreator ):
    """
    Override the _get_service_provider method to return an instance of a BingProvider.
    """

    def _get_service_provider ( self ):
        """
        This function creates a BingProvider object
        :return: BingProvider object
        """
        return BingProvider ( )
