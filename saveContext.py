#!/usr/bin/python
# -*- coding: utf-8 -*-
# saveContext

import os
import subprocess
import config
import compress
import mail
import description


def main():
	conf = config.Config()

	try:
		print "Launch %s ..." % conf.programName
		subprocess.check_call([conf.programName])
	except Exception as e:
		print "# Oops! %s crashs" % conf.programName
		c = compress.Compress(conf.logsPath,conf.extentions)
		c.zipContext()
		if conf.askDescription == '1':
			app = description.Description(None)
			c.zipDescription()
		if conf.sendMail == '1':
			m = mail.Mail()
			m.sendMail(conf.sendFrom,conf.sendTo,c.fileToSend)
		c.archiveContext()

if __name__ == "__main__":
  main()
