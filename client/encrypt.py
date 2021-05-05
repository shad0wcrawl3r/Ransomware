from cryptography.fernet import Fernet
from os.path import exists
from os import remove

def genKey():
	symkey = Fernet.generate_key()

	with open('symkey','wb') as kf:
	    kf.write(symkey)


def encrypt(file):
	if not exists ('symkey'):
		genKey()

	with open('symkey','rb') as kf:
		symkey=kf.read()
		f=Fernet(symkey)


	with open(file,'rb') as tf:
	    crypto=f.encrypt(tf.read())
	remove(file)
	

	with open(file+".enc",'wb') as tf,open('list_of_encrypted.plain','w') as encf:
	    tf.write(crypto)
	    encf.write(str(file)+"\n")





