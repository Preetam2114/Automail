import yagmail
import csv
import keyring
import getpass
from tqdm.auto import tqdm
from time import sleep
#from PIL import Image,ImageDraw,ImageFont


def csv_list(csv_file):

	if csv_file.endswith('.csv'):
		r_name = input("Please enter the column name with receiver names:")
		r_email = input("Please enter the column name with receiver email-id:")

		with open(csv_file,'r') as csv_file:
	            x=csv.DictReader(csv_file)

	            receivers = []
	            for row in x:
	                Name = row[str(r_name)]
	                email_receiver = row[str(r_email)]
	                receivers.append([Name,email_receiver])
		return receivers

	else:
		print("Entered file format is not CSV")

		return 0



def send_email(subject, body, attachment, receivers): 

	if receivers == []:
		print("The receivers list was empty please enter location of the csv file")
		receivers = input('csv_file:')
		receivers = csv_list(csv_file)

	if subject == '':
		print('The subject is empty please add the email subject')
		subject = input('subject:')

	if attachment == '':
		print('Please add attachment to the email')
		attachment = input('attachment:')

	if body == '':
		print('The body is empty please fill the email body')
		body = input('body:')


	try:

		print("Please enter your email address:")
		email = input()

		print("Please enter your password")
		password = getpass.getpass()

		yagmail.register(str(email),password)

	except:
		print('login failed...')

	if '{name}' in body:
		try:
			for receiver in tqdm(receivers):
				subject = str(subject)
				body = str(body)
				attachment = str(attachment)
				usermail = yagmail.SMTP(str(email))
				usermail.send(receiver[1],subject,[str(body).format(name = receiver[0]),attachment])
			print("Emails Sent Successfully")
		except:
			print("Email Sending failed")
		

	else:
		try:
			for receiver in tqdm(receivers):
				subject = str(subject)
				body = body
				attachment = attachment
				usermail = yagmail.SMTP(str(email))
				usermail.send(receiver[1],subject,[body,attachment])
			print("Emails Sent Successfully")

		except:
			print("Email Sending failed")
