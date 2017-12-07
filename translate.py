class Numcode:
	def __init__(self, message, location):
		self.message=message #Original message
		self.location=location #Location to which the message is to be sent
		self.translation = '' #Variable which stores the translation into the cipher
		self.alpha='abcdefghijklmnopqrstuvwxyz' #Just used to simplify code later on
		self.numb=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
		for x in range(len(self.message)):
           	if self.message[x].isalpha(): 
            	self.numb[x]=self.alpha[x]
				return self.translation.append(self.numb)
			else:
				if self.message[x] == '.':
					self.numb[x] == '.'
				elif self.message[x] == ' ':
					self.numb[x] == ' '
				else: 
					self.numb[x] == ''
				return self.translation.append(self.numb)
	
	
	
		'''for i in range(len(self.message)):
		    if(i.isalpha()):
		        self.message.append(str(ord(i)-ord('a') + 1))
		    else:
		        self.message.append(i)''' #Code found online, wasn't working in terminal.