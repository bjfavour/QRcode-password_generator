import pyqrcode
import png
from pyqrcode import QRCode

url = 'veld Antiseptic' 
url = pyqrcode.create(url)

url.svg('qr.svg',)
url.png('qr.png', scale = 8)