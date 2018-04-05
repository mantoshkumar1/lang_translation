import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template

from translator.translator_app import TranslatorApp

translator_app = TranslatorApp.get_app_instance ( )

app = Flask ( __name__,
              static_url_path='',  # removes any preceding path from the URL (as the default is /static)
              static_folder='web/static',  # will tell Flask to serve the files found at web/static.
              template_folder='web/templates'  # will tell Flask to serve the htmls found at web/templates.
              )


@app.route ( '/' )
def index ( ):
    return render_template ( 'index.html' )


# endpoint to get a list of supported languages
@app.route ( "/translate", methods=[ 'GET' ] )
def get_company_supported_languages ( ):
    return translator_app.get_supported_languages ( )


# endpoint to post msg for getting a translation
@app.route ( "/translate", methods=[ 'POST' ] )
def add_emp_schedule ( ):
    return translator_app.get_translation ( )


@app.errorhandler ( 400 )
def client_bad_request ( error ):
    app.logger.info ( error )
    return error


@app.errorhandler ( 404 )
def page_not_found ( error ):
    app.logger.info ( error )
    return render_template ( 'page_not_found.html' ), 404


@app.errorhandler ( 405 )
def method_not_implemented ( error ):
    app.logger.info ( error )
    return "This method has not been implemented.", 405


@app.errorhandler ( 413 )
def client_bad_request ( error ):
    app.logger.info ( error )
    return error


@app.errorhandler ( 422 )
def service_not_supported ( error ):
    app.logger.info ( error )
    return error


if __name__ == '__main__':
    handler = RotatingFileHandler ( filename='./logs/app.log', mode='a', maxBytes=200000, backupCount=10 )
    handler.setLevel ( logging.DEBUG )
    app.logger.addHandler ( handler )
    app.run ( threaded=True, debug=False )
