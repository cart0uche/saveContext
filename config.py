#!/usr/bin/python
# -*- coding: utf-8 -*-
# saveContext

import os
import ConfigParser

CONFIG_FILE            = "config.ini"
CONFIG_GENERAL_SECTION = "General"
CONFIG_PROGRAM         = "program"
CONFIG_SEND_MAIL       = "sendMail"
CONFIG_ASK_DESCRIPTION = "askDescription"

CONFIG_ZIP_SECTION     = "Zip"
CONFIG_LOGS            = "logs"
CONFIG_EXTENTIONS      = "extentions"
CONFIG_ARCHIVE         = "archive"

CONFIG_MAIL_SECTION    = "Mail"
CONFIG_SEND_FROM       = "sendFrom"
CONFIG_SEND_TO         = "sendTo"

class Config:

	def __init__(self,configFile=CONFIG_FILE):
		config = ConfigParser.SafeConfigParser()
		if os.path.isfile(configFile):
			config.read(configFile)

		# Section General
		self.__programName    = self.__loadConfigValue(config,CONFIG_GENERAL_SECTION,CONFIG_PROGRAM)
		self.__sendMail       = self.__loadConfigValue(config,CONFIG_GENERAL_SECTION,CONFIG_SEND_MAIL)
		self.__askDescription = self.__loadConfigValue(config,CONFIG_GENERAL_SECTION,CONFIG_ASK_DESCRIPTION)

		# Section Zip
		self.__logsPath       = self.__loadConfigValue(config,CONFIG_ZIP_SECTION,CONFIG_LOGS)
		self.__extentions     = self.__loadConfigValue(config,CONFIG_ZIP_SECTION,CONFIG_EXTENTIONS)
		self.__archivePath    = self.__loadConfigValue(config,CONFIG_ZIP_SECTION,CONFIG_ARCHIVE)

		# Section Mail
		self.__sendFrom       = self.__loadConfigValue(config,CONFIG_MAIL_SECTION,CONFIG_SEND_FROM)
		self.__sendTo         = self.__loadConfigValue(config,CONFIG_MAIL_SECTION,CONFIG_SEND_TO).split(',')

	def __loadConfigValue(self,config,section,option):
		return config.get(section,option)

	@property
	def programName(self):
		return self.__programName

	@property
	def sendMail(self):
		return self.__sendMail

	@property
	def askDescription(self):
		return self.__askDescription

	@property
	def logsPath(self):
		return self.__logsPath

	@property
	def extentions(self):
		return self.__extentions

	@property
	def archivePath(self):
		return self.__archivePath

	@property
	def sendFrom(self):
		return self.__sendFrom

	@property
	def sendTo(self):
		return self.__sendTo


def main():
	conf = Config()

if __name__ == '__main__':
	main()
