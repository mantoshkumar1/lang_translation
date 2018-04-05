import threading

from flask import abort
from flask import request, jsonify
from werkzeug.exceptions import BadRequest

from translator.caching.strategy.simple_caching import SimpleCacheStrategy
from translator.translation.service_creator.company.google_creator import GoogleServiceCreator


class TranslatorApp:
    """
    This class is the top most level hierarchy which envelopes whole application and employs singleton pattern.
    """
    __singleton_lock = threading.Lock ( )

    # this will hold the instance of app instance
    __app_instance = None

    def __init__ ( self ):
        # If at any point you want to change service provider, change it here and you are done.
        self.service_creator = GoogleServiceCreator ( )

        # holds instance of cache strategy
        self.app_cache = TranslatorApp.get_cache_strategy_instance ( )

    def get_set_translation_from_cache ( self, text, src_lang, target_lang ):
        """
        This function saves translated_text wrto a key: (text, src_lang, target_lang) into the cache. \
        If the item exist in cache then it immediately returns the value. If item does not exist \
        in the cache, it first get it from translator service, set it into cache and returns the \
        translated text.

        Reference: # http://flask.pocoo.org/docs/0.12/patterns/caching/

        :param text: The text that needs to be translated to target_lang (str)
        :param src_lang: str
        :param target_lang: str
        :return: translated text (str)
        """
        item_key = (text, src_lang, target_lang)
        translated_text = self.app_cache.get ( item_key )
        if translated_text is None:
            translated_text = self.service_creator.get_translation ( text, src_lang, target_lang )
            self.app_cache.set ( item_key, translated_text )

        return translated_text

    @staticmethod
    def get_cache_strategy_instance ( ):
        """
        If at any point you want to change cache strategy, change it here and you are done, \
        if you change cache strategy, change the passed values as well.
        :return:
        """
        caching_instance = SimpleCacheStrategy ( )
        caching_instance.apply_cache_strategy ( threshold=50, default_timeout=100 )
        return caching_instance.cache_strategy

    @staticmethod
    def verify_rpc_value ( user_dict ):
        """
        Verify POST RPC data. If data is not JSON format, it raises ValueError error.
        :param user_dict: json data
        :return:
        """
        for key in user_dict:
            if not isinstance ( user_dict[ key ], str ):
                # Error code 422
                raise ValueError ( 'Value of {0} is not a string'.format ( key ) )

    @staticmethod
    def verify_post_data ( ):
        """
        Verify POST RPC data. If data is not supposed format, it raises appropriate error.
        :return:
        """
        # check every field is present
        try:
            request.json[ 'source_lang' ]
            request.json[ 'target_lang' ]
            request.json[ 'text' ]

            TranslatorApp.verify_rpc_value ( request.json )

        except KeyError:  # All the values are not present
            # 400 Bad Request
            abort ( 400, "All mandatory fields are not provided" )
        except ValueError as err:
            # 422 Unprocessable Entity
            abort ( 422, "Unprocessable value: {0}".format ( err.args  ) )
        except BadRequest:
            # 400 Bad Request
            abort ( 400, "Provided values are having malformed syntax" )

    def get_translation ( self ):
        """
        This function serves the endpoint of POST translate and calls the translator service object \
        and gets the translation.
        :return: Json reply with translated message
        """
        self.verify_post_data ( )

        text = request.json[ 'text' ]
        src_lang = request.json[ 'source_lang' ]
        target_lang = request.json[ 'target_lang' ]

        # if translation is available in cache, just fetch it from there. Otherwise use translation service.
        translated_text = self.get_set_translation_from_cache ( text, src_lang, target_lang )

        return jsonify ( {"Translation": translated_text} )

    def get_supported_languages ( self ):
        """
        This function serves as the endpoint of GET translate and calls the translator service object \
        and returns the supported languages by translation service.
        :return: Json reply with supported translated message from service provider
        """
        supported_lang = self.service_creator.company_supported_languages ( )
        supported_lang = ", ".join ( supported_lang )
        return jsonify ( {"Supported languages": supported_lang} )

    @classmethod
    def get_app_instance ( cls ):
        """
        This function uses “Double Checked Locking” to return an instance of TranslatorApp.
        Once a TranslatorApp object is created synchronization among threads is no longer useful \
        because now obj will not be null and any sequence of operations will lead to consistent \
        results. So we will only acquire lock on the get_app_instance() once, when the obj is null. \
        This way we only synchronize the first way through, just what we want.
        :param cls: Don't pass this parameter when calling this function, as it's a classmethod
        :return: an instance of TranslatorApp
        """
        if not cls.__app_instance:
            with cls.__singleton_lock:
                if not cls.__app_instance:
                    cls.__app_instance = cls ( )

        return cls.__app_instance
