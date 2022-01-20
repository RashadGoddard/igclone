import os
from jinja2 import Environment

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	 'postgres://zkqwlvseevrorl:a05fa0b755fc0c1c1ca9dd36ec4457996d4b23ea963a825b7262d8e65d60b2ef@ec2-3-224-157-224.compute-1.amazonaws.com:5432/d6sphjnnosbc2k'
	 #'mysql://root:''@localhost/User'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	jinja_env = Environment(extensions=['jinja2.ext.loopcontrols'])
	ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')