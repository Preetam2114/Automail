[![PyPI version](https://badge.fury.io/py/Automail.svg)](https://badge.fury.io/py/Automail)

# Automail


Automail is a open source python package licensed under GNU General Public License v3 
for making bulk mailing easy.

The distribution is available on various platforms :
* [Automail on PyPI <img src="https://img.icons8.com/material-rounded/26/000000/external-link.png"/>](https://pypi.org/project/Automail)
* [Automail on Github <img src="https://img.icons8.com/material-rounded/26/000000/external-link.png"/>](https://github.com/Preetam2114/Automail)

Automail comes with a bunch of functions:

csv_list : The function returns a list of list containing the receipent name and email.
		the function has only one arguement 'csv_file' which is the reference to the csv file containing
		receipent details.

## Usage:
```
		from Automail import csv_list

		myvar = csv_list('location to the csv file')

```
```
		*Replace Column name as per your csv*
		output:
		Please enter the column name with receiver names: Column name
		Please enter the column name with receiver email-id: Column name
```


send_email : This function is responsible for structuring the email and sending it to the respective receipents
		the function include following arguements.

		subject: str argument for adding subject to email.

		body: This function argument is responsible for creating the body of the email it supports HTML and Text format,
			for case where you need to add name of the recepient use {name} the function will autoreplace it with the recepient name.

		attachment: This function argument is responsbile for providing the reference of the attachment file location.

		receivers : This function argument is list of list created using the csv_list().


## usage:
```
		from Automail import csv_list,send_email

		subject = 'This is the email subject'
		body  = 'This is the email body'
		attachment = 'location of attachment file'
		receivers = csv_list('location to the csv file')

		send_email(subject, body, attachment, receivers)
```
```
		output:
		Please enter your email address: xzy@gmail.com
		Please enter your password: .......
		(Input for password field won't be displayed)
```

