from setuptools import setup

with open("README.md","r") as fh:
	long_description = fh.read()

classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Communications :: Email",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	]

setup(
	name = "Automail",
	version = "0.1.0",
	description ="sends bulk automated emails",
	py_modules = ["Automail"],
	package_dir = {'':'src'},
	classifiers=classifiers,
	keywords = "Email",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = 'https://github.com/Preetam2114/Automail',
	author = "Preetam Rane",
	author_email = "preetamrane2114@gmail.com",
	install_requires = ['yagmail','keyring','tqdm'],
	zip_safe=False,
) 