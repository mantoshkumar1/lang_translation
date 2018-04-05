import googletrans
from flask import abort
from hyper.http20.exceptions import StreamResetError

from ..provider import Provider


class GoogleProvider ( Provider ):
    """
        Implements the Provider interface.
    """

    def __init__ ( self ):
        self.translator = googletrans.Translator ( )
        self.lang_codes = self.get_supported_language_code ( )

    def translate ( self, text, src_lang, target_lang ):
        """
        This function calls the  googletrans API and get the translation and \
        in case of any error abort the calls and returns appropriate HTTP status code.
        # Reference: https://pypi.python.org/pypi/googletrans
        :param text: str
        :param src_lang: str
        :param dest_lang: str
        :return: translated text (str)
        """
        target_lang = target_lang.lower ( )

        if not self.lang_codes.get ( target_lang ):
            # 415 Unsupported Media Type
            abort ( 422, "Google does not support {0} language yet!".format ( target_lang ) )

        if len ( text ) > 15000:
            # 413 Payload Too Large
            abort ( 413, "The maximum character limit on a single text is 15k." )

        # not using src_lang language as relying over auto source language detection of google.
        try:
            translated_obj = self.translator.translate ( text=text, dest=self.lang_codes[ target_lang ] )
        except ValueError:
            abort ( 424, "Google does not support this combination of language translation." )
        except StreamResetError:
            abort ( 424, "Google is not able to serve your request at this moment. Please try again." )
        except Exception as e:
            # If you get HTTP 5xx error or errors like #6, it’s probably because Google has banned your client IP address.
            abort ( 424, e.message ( ) )

        return translated_obj.text

    def get_supported_languages ( self ):
        """
        Returns the list of languages supported by Google Translation
        :return: list of str
        """
        # returns a list of str. e.g; ['hindi', 'english']
        return googletrans.LANGCODES.keys ( )

    def get_supported_language_code ( self ):
        """
        returns a dict with supported language by Google Translation and their code
        :return:
        """
        # e.g; {'sindhi': 'sd', 'italian': 'it'}
        return googletrans.LANGCODES
