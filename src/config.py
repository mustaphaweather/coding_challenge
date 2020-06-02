import os
from environs import Env
import logbook

### insitalise env 
env = Env()

log_dict = {
	"NOTSET": logbook.NOTSET ,
	"DEBUG":  logbook.DEBUG ,
	"INFO":   logbook.INFO ,
	"WARNING":   logbook.WARNING ,
	"ERROR":  logbook.ERROR
}



#Flask configuration file

#Developpement Config
class Devconfig():
	ENVIRONEMENT = "developement"
	DEBUG = True
	LOG_LEVEL = log_dict.get(env("LOG_LEVEL", "NOTSET"))

#Production Config
class Prodconfig():
	ENVIRONEMENT = "production"
	DEBUG = False
	LOG_LEVEL = log_dict.get(env("LOG_LEVEL", "NOTSET"))

#Developpement Config
class Testconfig():
	ENVIRONEMENT = "test"
	TESTING = True
	LOG_LEVEL = log_dict.get(env("LOG_LEVEL", "NOTSET"))

