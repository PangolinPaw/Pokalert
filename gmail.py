#!/usr/bin/python

import smtplib
import string
import poplib
from email import parser

import email
import mimetypes
import email.mime.application

def attach(sender, password, to, subject, message, filename):
	# Create a text/plain message
	msg = email.mime.Multipart.MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = to

	# The main body is just another attachment
	body = email.mime.Text.MIMEText(message)
	msg.attach(body)

	# Attachment
	fp=open(filename,'rb')
	att = email.mime.application.MIMEApplication(fp.read(),_subtype="dat")
	fp.close()
	att.add_header('Content-Disposition','attachment',filename=filename)
	msg.attach(att)

	# send via gmail
	s = smtplib.SMTP('smtp.gmail.com')
	s.starttls()
	s.login(sender, password)
	s.sendmail(sender, [to], msg.as_string())
	s.quit()

