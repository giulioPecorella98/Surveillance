# Raspberry Pi Motion Camera 

A simple security camera system for **Raspberry Pi zero W** that uses a PIR motion sensor to detect movement, takes pictures, and sends them by email.

The project is designed to run on Raspberry Pi zero W with a Pi Camera and a PIR motion sensor connected through GPIO.

## Hardware

The project requires:

* Raspberry Pi zero W
* Raspberry Pi Camera
* PIR motion sensor
* Internet connection

### GPIO connection

The PIR sensor is connected to:

```text
PIR OUT → GPIO 17
PIR VCC → 5V
PIR GND → GND
```

The GPIO pin can be changed in the Python script:

```python
pir = MotionSensor(17)
```

## Software requirements

The program requires:

* Python 3
* `picamera2`
* `gpiozero`

The required Python packages can be installed using:

```bash
pip install -r requirements.txt
```

On Raspberry Pi OS, `picamera2` and its dependencies are generally best installed through the system package manager:

```bash
sudo apt install python3-picamera2 python3-gpiozero
```

## Installation

Clone the repository:

```bash
git clone https://github.com/giulioPecorella98/Surveillance.git
```

Install the required dependencies:

```bash
sudo apt update
sudo apt install python3-picamera2 python3-gpiozero
```

Make the script executable:

```bash
chmod +x bbiwy.py
```

### Mail and password

You need to change Mail and Password in bbiwy.py. You should **not use your normal Gmail password** in the Python source code.

If you have two-factor authentication enabled on your Google account, create a Google **App Password** and use that instead.


## How it works

The program initializes the PIR sensor. When motion is detected, the program runs the following actions.

1. Initializes the camera.
2. Takes three photographs.
3. Saves the photographs locally.
4. Opens the three files.
5. Attaches them to an email.
6. Connects to Gmail's SMTP server.
7. Logs into the Gmail account.
8. Sends the email.
   

## License

Copyright © 2026 Giulio Pecorella

This program is free software: you can redistribute it and/or modify it under the terms of the **GNU General Public License v2 or later**, as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**.

See the GNU General Public License for more details.

## Author

**Giulio Pecorella**
