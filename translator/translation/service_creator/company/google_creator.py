from translator.translation.service.company.google import GoogleProvider
from translator.translation.service_creator.creator import ServiceCreator


class GoogleServiceCreator ( ServiceCreator ):
    """
    Override the _get_service_provider method to return an instance of a GoogleProvider.
    """

    def _get_service_provider ( self ):
        """
        This function creates a GoogleProvider object
        :return: GoogleProvider object
        """
        return GoogleProvider ( )
