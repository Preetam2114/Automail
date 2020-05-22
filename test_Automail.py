from Automail import csv_list,send_email


def test_Automail_with_param():

	subject ='this is the test mail'
	body = 'this is the test mail {name}'
	attachment = '/Users/preetamrane/Desktop/Screenshot 2020-05-07 at 5.38.57 PM.png '
	receivers = csv_list('/Users/preetamrane/Desktop/file.csv')

	send_email(subject, body, attachment, receivers)

	assert True