import os
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/works'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY =os.urandom(24)