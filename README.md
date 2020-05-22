[![PyPI version](https://badge.fury.io/py/Automail.svg)](https://badge.fury.io/py/Automail)

# Automail


Automail is a open source python package licensed under MIT 
for making bulk mailing easy.

The distribution is available on various platforms :
* [Automail on PyPI](https://pypi.org/project/Automail):link:
* [Automail on Github](https://github.com/Preetam2114/Automail):link:

## Usage:

Automail has 2 user function:
	1. csv_list:
		Function arguments:
		 * CSV_FILE: points towards the file location
		 
```py
		from Automail import csv_list

		myvar = csv_list('location to the csv file')

```
output:
```bash
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
## Running tests

```
pytest -s
```

## Contributing

Contribution is welcome.

Pull Requests will be merged if they match the [Development Guide](#).

For prototypes, pure python implementations using ctypes are also welcome.
We will probably port it to a proper extension in the future.

Please ask questions [here](https://github.com/Preetam2114/Automail/issues).
