class Config:
    SECRET_KEY = \
        '6f99c3f59d620d5831ffb22a707f8e50d33d9a22fa767830b245d00811823112'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'yuchen.xing96@gmail.com'
    MAIL_PASSWORD = 'xingyuchen1125'
