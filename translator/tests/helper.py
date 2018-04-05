from flask import json

class Helper:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def populate_dict ( given_dict, key_str, val ):
        if val:
            given_dict[ key_str ] = val

    def create_translation_request( self, text=None, src_lang=None, target_lang=None ):
        translation_req = dict()

        if src_lang:
            self.populate_dict ( translation_req, "source_lang", src_lang )

        if target_lang:
            self.populate_dict ( translation_req, "target_lang", target_lang )

        if src_lang:
            self.populate_dict ( translation_req, "text", text )

        return translation_req

    def send_translation_request( self, text=None, src_lang=None, target_lang=None ):
        translation_req_dict = self.create_translation_request(
            text=text,
            src_lang=src_lang,
            target_lang=target_lang
        )

        response = self.app.post ( '/translate',
                                   data=json.dumps ( translation_req_dict ),
                                   content_type='application/json',
                                   follow_redirects=True )

        return response

    def get_translator_lang_support( self ):
        response = self.app.get ( '/translate',
                                   content_type='application/json',
                                   follow_redirects=True )

        return response






