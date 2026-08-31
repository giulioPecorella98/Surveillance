#!/usr/bin/env python3
#
#  bbiwy.py
#  
#  Copyright 2026 Giulio Pecorella
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os
import sys
import smtplib
import ssl
import time
from email.message import EmailMessage
from picamera2 import Picamera2
from gpiozero import MotionSensor
from signal import pause	



# Email configuration
port = 465
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()
Mail = 'gigifinizio@gmail.com'
Password = 'sbucciati_personalmente'

# Path to photo to be sent
Photo = '/home/Pictures/photo'

# Mail message configuration
msg = EmailMessage()
msg['Subject'] = 'Photo'
msg['From'] = Mail
msg['To'] = Mail



def take_photo():
    n = 0
    while n < 3:
        n += 1
        cam = Picamera2()
        cam.start()
        cam.capture_file(Photo + str(n) + '.jpg')
        time.sleep(1)
        cam.stop()
    cam.close()

def movement_revealed():
    
    take_photo()
    for n in range(1, 4):
        with open(Photo + str(n) + '.jpg', 'rb') as f:
            photograph = f.read()
        msg.add_attachment(photograph, maintype='image',
                           subtype='jpeg',filename='photo.jpg')

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(Mail, Password)
        smtp.send_message(msg)
            
    return 

def main(args):
    
    pir = MotionSensor(17)
    time.sleep(2)
    pir.when_motion = movement_revealed
    pir.when_no_motion = lambda: print('no movement detected')
    pause()
    
    return 0



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
