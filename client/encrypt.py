from cryptography.fernet import Fernet

symkey = Fernet.generate_key()

f=Fernet(symkey)

with open('symkey','wb') as kf:
    kf.write(symkey)

with open('test.pdf','rb') as tf:
    crypto=f.encrypt(tf.read())

with open('test.pdf','wb') as tf:
    tf.write(crypto)




