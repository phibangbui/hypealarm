import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def send_email(hypelist):
	server = create_server()

	msg = MIMEMultipart()
	msg['From'] = "" 
	msg['To'] = "phibangbui.cs@gmail.com"
	msg['Subject'] = "HypeAlert"

	for hype in hypelist:
		body = body_generator(hype) 
		msg.attach(MIMEText(body, 'html'))

	email_body = msg.as_string()
	print('SENDING EMAIL')
	server.sendmail("", "phibangbui.cs@gmail.com, aland.luk@gmail.com", email_body)

def create_server():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login("hypealerter@gmail.com","generatehype")
	return server

def body_generator(hype):
	body = '<img src=' + hype[0].get('src') + '/> <br> <p><a href=\"https://instagram.com/' + hype[1] + '\">' + hype[1]+ '</a> : ' + hype[0].get('alt', '').encode('utf-8') + '</p>'
	return body

