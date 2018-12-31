# project/server/main/views.py

import requests
from flask import render_template, Blueprint,request
from env_variables import CAPTCHA_SECRET_KEY, MAIL_PASSWD, SMTP_ADDRESS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def home():
    return render_template('main/home.html')


@main_blueprint.route("/datachallenge/")
def datachallenge():
    return render_template("main/datachallenge_ipynb.html")


@main_blueprint.route("/tos/")
def tos():
    return render_template("terms_of_service.html")


@main_blueprint.route("/guide/")
def guide():
    return render_template("main/guide.html")


@main_blueprint.route("/dev/")
def dev():
    return render_template("main/dev.html")


@main_blueprint.route("/meteor/")
def meteor():
    return render_template("main/meteor.html")

@main_blueprint.route("/contact/", methods = ['GET','POST'])
def contact():
    info=""
    if request.method == 'POST':
        gresponse=request.form['g-recaptcha-response']
        data={"secret":CAPTCHA_SECRET_KEY,"response":gresponse}
        r=requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        if r.json()['success']:
            sender = request.form['sender']
            message = request.form['message']
            mailserver = smtplib.SMTP(SMTP_ADDRESS)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.login("wattstrat@alwaysdata.net", MAIL_PASSWD)
            msg = MIMEMultipart()
            msg['From'] = str(sender)
            msg['To'] = "ws@wattstrat.com"
            msg['Subject'] = "[WattStrat] Message du formulaire"
            msg.attach(MIMEText(str(message)))
            mailserver.sendmail("wattstrat@alwaysdata.net", "ws@wattstrat.com", msg.as_string())
            mailserver.quit()
            info = "Message envoyé"	
    return render_template("main/contact.html", info=info)


@main_blueprint.route("/robots.txt")
def robots():
    return render_template("robots.txt")


@main_blueprint.route("/sitemap.xml")
def sitemap():
    return render_template("sitemap.xml")

