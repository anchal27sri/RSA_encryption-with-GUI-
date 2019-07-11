import random
from fractions  import gcd
import math

def modinv(a,m):
	for x in range(1,m):
		if (a*x)%m == 1:
			return x

def power(x,y,p):
	res = 1
	x = x%p
	while y>0:
		if y&1:
			res = (res*x)%p
		y = y//2
		x = (x*x)%p

	return res


def encrypt(x):
	global cypher_text
	y = int(power(x,e,n))
	cipher.append(y)
	cypher_text = cypher_text + str(chr(y%10000))


plain = ""
cipher = []
cypher_text = ""

p = '3'
q = '7'
e = 'b'
n = 5


######################################################################################################

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

text = ""
class Window(QWidget):

	def __init__(self, parent = None):
		super(Window, self).__init__(parent)
		self.setGeometry(300, 200, 450, 220)
		layout = QFormLayout()
		self.le = QLineEdit()
		self.le1 = QLineEdit()

		layout.addRow("Plaintext:",self.le)
		bingo = "press the 'Insert' button to enter the plaintext"
		self.le.setText(str(bingo))
		self.setWindowTitle("RSA encryptor")
		self.setWindowIcon(QIcon('icon.png'))
		self.setLayout(layout)
		layout.addRow("Ciphertext:",self.le1)
		self.home()

	def home(self):
		btn = QPushButton('Quit', self)
		btn.clicked.connect(QCoreApplication.instance().quit)
		btn.resize(btn.minimumSizeHint())
		btn.move(350,170)

		btn1 = QPushButton('Insert', self)
		btn1.clicked.connect(self.gettext)
		btn1.resize(btn.minimumSizeHint())
		btn1.move(350,95)


		btn2 = QPushButton('Encrypt', self)
		btn2.clicked.connect(self.Encrypt)
		btn2.resize(btn.minimumSizeHint())
		btn2.move(350,135)

		
		#self.show()

	def Encrypt(self):
		primes = ("1523","1531","1543","1549","1553","1559","1567","1571","1579","1583") 
		global p,q,e,plain,cypher_text,n
		p, ok1 = QInputDialog.getItem(self, "Value of first prime number p","Choose the value of p:", primes, 0, False)
		q, ok2 = QInputDialog.getItem(self, "Value of second prime number q","Choose the value of q:", primes, 0, False)
		p = int(p)
		q = int(q)
		n = p*q
		phi_n = (p-1)*(q-1)
		arr = []
		for i in range(1,phi_n):
			if gcd(i,phi_n) == 1:
				arr.append(i)
		es = []
		for i in range(1,10):
			es.append(str(arr[i]))

		es = tuple(es)
		e, ok3 = QInputDialog.getItem(self, "Value of the public key e", "Choose the value of public key(e): ",es, 0, False)
		e = int(e)
		d = modinv(e,phi_n)
		#print(len(plain))
		if ok1 and ok2 and ok3:
			for i in range(len(plain)):
				encrypt(ord(plain[i]))

		#print(cypher_text)
		self.le1.setText(str(cypher_text))


	def gettext(self):
		global plain
		text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter a message:')
		if ok:
			self.le.setText(str(text))		
			plain = str(text)
			#print(plain)


	def close_application(self):
		#print("Whooooaaa!!!")
		sys.exit()

def run():
	app = QApplication(sys.argv)
	GUI = Window()
	GUI.show()
	sys.exit(app.exec_())

run()
intput()