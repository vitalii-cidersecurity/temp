import flask
import os
import connexion

def create_app(app_name='MYAPPNAME'):
    flask_app = connexion.App(__name__, skip_error_handlers=False)
    return flask_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # nosem

else:
    pass