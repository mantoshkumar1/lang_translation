import unittest

from run_lang_translation_server import app, translator_app
from .helper import Helper


class BasicTests ( unittest.TestCase ):

    # executed prior to each test
    def setUp ( self ):
        app.config[ 'TESTING' ] = True
        app.config[ 'WTF_CSRF_ENABLED' ] = False
        app.config[ 'DEBUG' ] = False

        self.app = app.test_client ( )

        self.helper = Helper (self.app)

    # executed after each test
    def tearDown ( self ):
        #  Clears the cache.
        translator_app.app_cache.clear ( )

    #### tests ####
    def test_main_page ( self ):
        response = self.app.get ( '/', follow_redirects=True )
        self.assertEqual ( response.status_code, 200 )

    def test_noexisting_page( self ):
        response = self.app.get ( '/', follow_redirects=True )
        self.assertTrue(response.status_code, 404)

    def test_post_invalid_target_lang( self ):
        response = self.helper.send_translation_request(text="Hello world!", src_lang="English", target_lang="failure")
        self.assertEqual(response.status_code, 422)

    def test_translator_lang_support( self ):
        response = self.helper.get_translator_lang_support()
        self.assertEqual(response.status_code, 200)

    def test_missing_userdata( self ):
        response = self.helper.send_translation_request ( src_lang="English", target_lang="failure" )
        self.assertEqual(response.status_code, 400)

    def test_post_invalid_text( self ):
        response = self.helper.send_translation_request(text=1, src_lang="English", target_lang="failure")
        self.assertEqual(response.status_code, 422)


