import yagmail
import csv
import keyring
import getpass
from tqdm.auto import tqdm
from time import sleep
import os
import readline
#from PIL import Image,ImageDraw,ImageFont


def csv_list(csv_file):

	if csv_file.endswith('.csv'):
		file = csv_file
		while True:
			try:
				r_name = input("\n>Please enter the column name with receiver names:")
				r_email = input(">Please enter the column name with receiver email-id:")

				with open(csv_file,'r') as csv_file:
					x=csv.DictReader(csv_file)
					receivers = []
					for row in x:
						Name = row[str(r_name)]
						email_receiver = row[str(r_email)]
						receivers.append([Name,email_receiver])

			except:
				csv_file = file
				print("\n######### Please enter valid column names #########")

			else:
				break
				
		return receivers

	else:
		print("Entered file format is not CSV")

		return 0


def send_email(subject='', body='', attachment='', receivers=[]): 

	if receivers == []:
		print("The receivers list was empty please enter location of the csv file")
		receivers = input('csv_file:').strip("'")
		receivers = csv_list(str(receivers.strip()))

	if subject == '':
		print('\n>The subject is empty please add the email subject')
		subject = input('subject:').strip("'")


	if attachment == '':
		print('\n>Please add attachment to the email')
		attachment = input('attachment:').strip().strip("'")

	while True:
		if os.path.isfile(attachment):
			break
		else:
			print("\n######### The attachment doesn't seem to be a file #########")
			print("#########  If the issue continues rename the file  #########")
			print('\n>Please add attachment to the email')
			attachment = input('attachment:').strip().strip("'")

	if body == '':
		print('The body is empty please fill the email body')
		body = input('body:').strip("'")


	try:

		print("\n>Please enter your email address:")
		email = input()

		print("\n>Please enter your password")
		password = getpass.getpass()

		yagmail.register(str(email),password)

	except:
		print('\n>login failed...')

	if isinstance(subject, str) == False:
		subject = str(subject)

	if isinstance(body, str) == False:
		body = str(body)

	if isinstance(attachment, str) == False:
		print('\n>Facing issue with attachment location pls. reattach the file')
		attachment = input('attachment:').strip().strip("'")

	if '{name}' in body:
		try:
			for receiver in tqdm(receivers):
				usermail = yagmail.SMTP(str(email))
				usermail.send(receiver[1],subject,[body.format(name = receiver[0]),attachment])
			print("\n>Emails Sent Successfully")
		except:
			print("\n>Email Sending failed")
		

	else:
		try:
			for receiver in tqdm(receivers):
				usermail = yagmail.SMTP(str(email))
				usermail.send(receiver[1],subject,[body,attachment])
			print("\n>Emails Sent Successfully")

		except:
			print("\n>Email Sending failed") 
