Readme file for QRCode

Open your terminal and install this two libraries with the codes below:

Pip install pyqrcode and also pip install pypng

Immediately you are down installing the two stated libraries, you open a python file and import the libraries as follows:

Import pyqrcode
Import pypng
From pyqrcode import QRcode

#Then write what you want to display when the read the QRcode. Whether a url or a product name in a string and pass it to a variable.

url = “www.bj-medical-lab.com”
url = pyqrcode.create(url)

#Then create a file where it will be saved

url.svg(“url.svg”,)
url.png(“url.png”, scale = 8) #scale it up so that you can see it properly

Run the code and then check the created file
