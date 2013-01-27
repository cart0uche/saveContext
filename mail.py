#!/usr/bin/python
# -*- coding: utf-8 -*-
# saveContext

import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.MIMEMultipart import MIMEMultipart

COMMASPACE = ', '

class Mail:
	def sendMail(self,sendFrom,sendTo,fileToSend):
		print '# send mail to' + str(sendTo) + ' with file ' + fileToSend
		msg = MIMEMultipart()

		msg['Subject'] = 'saveContext send you the file ' + fileToSend
		msg['From'] = sendFrom
		msg['To'] = COMMASPACE.join(sendTo)

		attachedFile = MIMEBase('application', 'zip')
		attachedFile.set_payload(open(fileToSend,'rb').read())
		encoders.encode_base64(attachedFile)
		attachedFile.add_header('Content-Disposition','attachment',filename=fileToSend)
		msg.attach(attachedFile)
		s = smtplib.SMTP('localhost')
		s.sendmail(sendFrom, sendTo, msg.as_string())
		s.quit()

def main():
	print '# main'

if __name__ == '__main__':
	main()