[![PyPI version](https://badge.fury.io/py/Automail.svg)](https://badge.fury.io/py/Automail)

# Automail


Automail is an open source python package for making bulk mailing easy.

The distribution is available on following platforms:
* [Automail on PyPI](https://pypi.org/project/Automail):link:
* [Automail on Github](https://github.com/Preetam2114/Automail):link:

# Installation :

```bash
		pip install Automail
```


## Package Functions:

Automail has 2 user function:
1. csv_list(CSV_FILE): This user function generates list of list
		containing maiiling details of the receivers
   - Function arguments:
     - CSV_FILE: points towards the file location
#### usage:	 
```py
		from Automail import csv_list

		myvar = csv_list('location to the csv file')

```
output:
```bash
		Please enter the column name with receiver names: Column name
		Please enter the column name with receiver email-id: Column name
```
2. send_email(subject, body, attachment, receivers): send_email is a stand-alone function 
						which can work without passing any argument	
   - Function Parameter:
     - subject: This argument is responsible for subject of the email.
     - body: This argument is responsible for the email body.
       - Supports:
         * [x] HTML TEMPLATES
	 * [x] TEXT
	 * [ ] Forms (not tested)
     - attachment :This argument is responsible for attachment source and supports varities of file formats.
     - receivers : This argument passes the list of list careated using __csv_list__ finction.

#### usage:
```py
		from Automail import csv_list,send_email

		subject = 'This is the email subject'
		body  = 'This is the email body'
		attachment = 'location of attachment file'
		receivers = csv_list('location to the csv file')

		send_email(subject, body, attachment, receivers)
```
#### usage:
```bash
		Please enter your email address: xzy@gmail.com
		Please enter your password: .......
```
>NOTE: input for password field won't be displayed while typing for secutity purposes.

## Running test

```bash
pip install -r requirements.txt
pytest -s
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contact
[![twitter][1.1]][1]
[![linkedIn][2.1]][2]
[![github][3.1]][3]

[1.1]: http://i.imgur.com/tXSoThF.png
[2.1]: https://www.iconfinder.com/icons/107092/download/png/64
[3.1]: http://i.imgur.com/0o48UoR.png

[1]: https://twitter.com/pvr_rane
[2]: https://img.icons8.com/wired/64/000000/linkedin.png
[3]: https://github.com/Preetam2114

## Wanna Contribute?

Your contribution is welcome!

Pull Requests will be merged if they match the project requirements.

For prototypes, pure python implementations using ctypes are also welcome.
We will probably port it to a proper extension in the future.

Please ask questions [here](https://github.com/Preetam2114/Automail/issues).
