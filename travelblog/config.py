  
import os


class Config:
    SECRET_KEY = "9abe157dd743dcb5c11aa3d952c2726b"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/site'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')