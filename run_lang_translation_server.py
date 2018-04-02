from flask import Flask, render_template

app = Flask ( __name__,
              static_url_path='',  # removes any preceding path from the URL (as the default is /static)
              static_folder='web/static',  # will tell Flask to serve the files found at web/static.
              template_folder='web/templates'  # will tell Flask to serve the htmls found at web/templates.
              )


@app.route ( '/' )
def index ( ):
    return render_template ( 'index.html' )


@app.errorhandler ( 404 )
def page_not_found ( error ):
    return render_template ( 'page_not_found.html' ), 404


if __name__ == '__main__':
    app.run ( debug=True )
