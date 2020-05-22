[![PyPI version](https://badge.fury.io/py/Automail.svg)](https://badge.fury.io/py/Automail)

# Automail


Automail is a open source python package licensed under MIT 
for making bulk mailing easy.

The distribution is available on various platforms :
* [Automail on PyPI](https://pypi.org/project/Automail):link:
* [Automail on Github](https://github.com/Preetam2114/Automail):link:

## Usage:

Automail has 2 user function:
 csv_list(CSV_FILE):
  Function arguments:
   CSV_FILE: points towards the file location
		 
```py
		from Automail import csv_list

		myvar = csv_list('location to the csv file')

```
output:
```bash
		Please enter the column name with receiver names: Column name
		Please enter the column name with receiver email-id: Column name
```



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
