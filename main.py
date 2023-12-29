from Crypto.Cipher import AES
from Crypto.Hash import SHA256

cipher = AES.new(b'16 byte key', AES.MODE_EAX)
