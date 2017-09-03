import requests
import json
import pyperclip
import os
import platform

#TODO: 
#	A. Proper banner
#	B. !LOOP/CALLBACK
#   C. Create Class Genrator to pass to a tkinter function
#		In TkApp
#		1. Be able enter text
#		2. Menu choose  font type

greeting = ''' PYL33T... so you can geek while you speak.these are the fonts... \n 
	0 = classic
	1 = Ultra 
	2 = Glyphtek
	3 = Wolstein
	4 = Ancy
	5 = Beey
	6 = Broadway
	7 = fullwidth'''


class const:

	def __init__(self, font, text):
		self.text = text
		self.font = font

	def txt_convert(self, font, text):
		parameters = {"genr8rsUserIpAddress": "null", "genr8rsUserId": "null","_sCharacterSet": self.font, "_sText": self.text}
		response = requests.get("http://api.genr8rs.com/Generator/Fun/LeetSpeakGenerator?", params=parameters)

		data = response.json()
		pyperclip.copy(data["_sResult"])
		print("TEXT : " + data["_sResult"])


done = False
while done == False:
	i = ['classic', 'ultra', 'glyphtek', 'wolfenstein', 'ancy', 'beefy', 'broadway', 'fullwidth']
	print(greeting)
	txt = input('\nENTER TEXT: \n')
	fnt = int(input('FONT? \n'))
	fnt = i[fnt]

	t = const(fnt, txt)
	t.txt_convert(fnt, txt)
	n = input('Q FOR QUIT OR ENTER TO CONTINUE')
	if n.lower() == "q":
		done = True
		if done == True:
			quit()