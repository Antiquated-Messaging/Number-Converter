class Numcode:
	def __init__(message, translation, location):
		self.message = message
		self.translation = translation
		self.location = location
		letter = ['abcdefghijklmnopqrstuvwxyz']
	
	def value(message):
	    self.message = []
		for i in letter:
		    if(i.isalpha()):
		        self.message.append(str(ord(i)-ord('a') + 1))
		        print(self.message)
		    else:
		        self.message.append(i)
