
# Implement an algorithm to determine if a string has all unique characters or not. 
# str = 'shaurya' returns False
# str ='divya' return True

# The question to be asked to the interviewer : 
# Is the string ASCII or Unicode
# This determines the space required for the string in memory. Unicode holds a lot more data than an ASCII representation. 
class UniqueCharacter:
	def BruteUniqueChar(self,str):
		for char in range(0,len(str)):
			for secondChar in range(char+1,len(str)):
				if (str[char] == str[secondChar]):
					return False
		return True


	def OptimizedUniqueChar(self,str):
		maxString = 128

		if(len(str)>maxString):
			return False
		ASCIIarr = [False]*maxString
		for alphabet in range(len(str)):
			# ASCII representation of a character
			val = ord(str[alphabet])
			# print(val)
			if(ASCIIarr[val]):
				# print(ASCIIarr)

				return False
			#Set the corresponding ASCII index to True where character is found  
			ASCIIarr[val] = True

		return True


	def sortedUniqueChar(self,str):
		newstr = sorted(str)
		# print(newstr)
		for alphabet in range(1,len(newstr)):
			if newstr[alphabet-1]==newstr[alphabet]:
				return False
		return True



if __name__=="__main__":
	obj = UniqueCharacter();

	str = input('Enter the string you want to check using brute force : ')
	print('Brute Force result : ',obj.BruteUniqueChar(str));
	print('Optimized ASCII method result : ' , obj.OptimizedUniqueChar(str));
	print('Sorted answer result : ',obj.sortedUniqueChar(str));

