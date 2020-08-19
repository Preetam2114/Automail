#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:13:13 2018

__author__ = "PREETAM RANE"
__copyright__ = "Copyright 2018, IEEE-VIT STUDENT BRANCH"
__license__ = "GPL"
__version__ = "0.1.5"
"""
import yagmail
import keyring
import csv
from PIL import Image,ImageDraw,ImageFont


def sending_mail(email_receiver,Name):

    subject = 'Certificate of participation for IMaRC 2019'
    body = '''
    Dear Friend,
    Thank you so much for attending IMaRC 2019 at VMCC, IIT-Bombay this month. The conference was a huge success, thanks to the speakers, presenters, sponsors, exhibitors and, last but not the least, the participants. I am sure this conference has given you opportunities for global networking and sharing knowledge with the participants of the similar fields.

    On behalf of the organizing team, I would like to express my heartfelt thanks to each of you who participated in Conference.
    Please find Certificate of participation attached herewith.

    Best regards,

    General Chair
    IMaRC 2019
    '''
    img = "/Users/preetam/Desktop/emailing/{}.pdf".format(Name)
    yag = yagmail.SMTP('imarc.2019.ieee@gmail.com')
    yag.send(email_receiver,subject,[body,img])



def invitation(csvfile):

    password = keyring.get_password('imarc','imarc.2019.ieee@gmail.com')
    yagmail.register('imarc.2019.ieee@gmail.com',password)
    with open(csvfile,'r') as csv_file:
            x=csv.DictReader(csv_file)

            for row in x:
                #image1=Image.open(img).convert('RGBA')
                Name=row['Name']
                Lname=row['LastName']
                email_receiver=row['Email id']
                 txt = Image.new('RGBA', image1.size, (255,255,255,0))
                 font_type = ImageFont.truetype(textfont,60)
                 font_type2 = ImageFont.truetype(textfont,60)
                 d=ImageDraw.Draw(txt)
                 i=ImageDraw.Draw(txt)
                 x,y = image1.size
                 a,b = font_type.getsize(Fname)
                 m,n = font_type.getsize(Lname)
                 d.text(xy = (1200,),text=Fname, font = font_type, fill=(232, 201, 165,255))#change 440 and 240 with desired x y positions fill=(...) is the color of font
                 i.text(xy = (410,360),text=Lname, font = font_type2, fill=(232, 201, 165,255))
                 out = Image.alpha_composite(image1, txt)
                 out.save("{} {}.png".format(Fname,Lname))
                 print("{} {}.png".format(Fname,Lname))
                 out.show()
                sending_mail(email_receiver,Name)

invitation('file.csv')


 
