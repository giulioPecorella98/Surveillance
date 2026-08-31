#!/usr/bin/env python3
#
#  sorv.py
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
import time
from email.message import EmailMessage
from picamera2 import Picamera2
from gpiozero import MotionSensor
from signal import pause	



# Email address to send the photo to
Mail = 'gigifinizio@gmail.com'

# Password linked to the email account
Password = 'sbucciati_personalmente'

# Path to photo to be sent
Photo = '/home/Pictures/photo.jpg'



def photo():
    
    cam = Picamera2()
    cam.start()
    cam.capture_file(Photo)
    cam.stop()
    cam.close()
    
    msg = EmailMessage()
    msg['Subject'] = 'Photo'
    msg['From'] = Mail
    msg['To'] = Mail
    
    with open(Photo,'rb') as f:
        dati = f.read()
        
    msg.add_attachment(dati, maintype='image',subtype='jpeg',filename='photo.jpg')
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Mail, Password)
            smtp.send_message(msg)
            
    finally:
        if os.path.exists(Photo):
            os.remove(Photo)
    
    return 

def main(args):
    
    pir = MotionSensor(17)
    time.sleep(2)

    pir.when_motion = photo
    pir.when_no_motion = lambda: print('no movement detected')

    pause()
    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
