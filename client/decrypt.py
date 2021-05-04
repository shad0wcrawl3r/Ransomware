from cryptography.fernet import Fernet


with open('symkey','rb') as kf:
    symkey=kf.read()

fern = Fernet(symkey)
with open('test.pdf','rb') as tf:
    crypto=fern.decrypt(tf.read())

with open('test.pdf','wb') as tf:
    tf.write(crypto)




