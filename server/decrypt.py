from cryptography.fernet import Fernet

def decrypt():
	with open('symkey','rb') as kf:
	    symkey=kf.read()

	fern = Fernet(symkey)
	with open ('list_of_encrypted.plain','r') as encf:
		list_of_enc=encf.read().split('\n')
		lsit_of_enc.pop()
	
	for each in list_of_enc:
		with open(each+".enc",'rb') as tf:
		    crypto=fern.decrypt(tf.read())

		with open(each,'wb') as tf:
		    tf.write(crypto)




