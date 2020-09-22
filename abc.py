#!/usr/bin/python3.6
import psycopg2
import configparser
import sys, getopt
import os

exitScript=False

config = configparser.ConfigParser()
config.sections()


# read input argument
try:
	opts, args = getopt.getopt(sys.argv[1:],"h:c:",["","config="])
	if len(opts)==0:
		sys.exit(2)
except getopt.GetoptError:
	print ('mainscript.py -c <inputfile>')
	sys.exit(2)


for opt, arg in opts:
	if opt == '-h':
		print ('test.py -c <inputfile>')
		sys.exit()
	elif opt in ("-c", "--config"):
		inputfile = arg
		config.read(arg)

connection  = config['DEFAULT']['hostname']
username        = config['DEFAULT']['username']
password    = config['DEFAULT']['password']
database    = config['DEFAULT']['database']
output    = config['DEFAULT']['output']
sqlStringFile = config['DEFAULT']['sqlfile']


# empty and tune output file
def writeFile(data,filename):
	os.system('> '+filename)
	tmp=open(filename,'w+')
	for i in data:
		tmp.write(str(i).replace(')','').replace('(',''))
		tmp.write('\n')
	tmp.close()


sqlString = open(sqlStringFile)
C = psycopg2.connect( host=connection, user=username, password=password, dbname=database )
C = C.cursor()
result = C.execute(sqlString.read())
writeFile(C.fetchall(),output)

