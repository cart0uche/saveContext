#!/usr/bin/python
# -*- coding: utf-8 -*-
# saveContext

import os
import glob
import zipfile
import time

DESCRIPTION_TEMP_FILE = 'desc.txt'

class Compress:

	def __init__(self,logsPath,extention):
		self.__logsPath = logsPath
		self.__extention = extention

	def zipContext(self):
		self.__zipFileName = 'context_'+time.strftime('%d-%m-%Y_%H-%M-%S',time.localtime())+'.zip'
		if self.__logsPath is not None:
			f = zipfile.ZipFile(self.__zipFileName,'w',zipfile.ZIP_DEFLATED)
			print "# logsPath : %s" % self.__logsPath
			logsFile = glob.glob(os.path.join(self.__logsPath,"*."+self.__extention))
			for logFile in logsFile:
				print "# zip : %s" % logFile
				f.write(logFile,arcname=os.path.basename(logFile))
			f.close()
			print "# " + self.__zipFileName + " created"

	def zipDescription(self):
		if os.path.exists(DESCRIPTION_TEMP_FILE):
			f = zipfile.ZipFile(self.__zipFileName,'a',zipfile.ZIP_DEFLATED)
			print "# zip : " + DESCRIPTION_TEMP_FILE
			f.write(DESCRIPTION_TEMP_FILE)
			f.close()
			os.remove(DESCRIPTION_TEMP_FILE)
		else:
			print "No description given"

	def archiveContext(self):
		os.rename(self.__zipFileName,os.path.join("archive",self.__zipFileName))
		print "# archive file " + self.__zipFileName

	@property
	def fileToSend(self):
		return self.__zipFileName


# TODO : gerer une liste de repertoire de logs


def main():
	c = Compress('test/log1/','log')
	c.zipContext()
	c.archiveContext()

if __name__ == '__main__':
	main()
