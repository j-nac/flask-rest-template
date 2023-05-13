from flaskapp import create_app

if __name__ == '__main__':
    create_app('flaskapp.config.DevelopmentConfig').run()