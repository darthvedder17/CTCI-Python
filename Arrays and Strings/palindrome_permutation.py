# Given a string,write a function to check if it is a permutation of a palindrome
# Example : 
# tact coa 
# Output : true(permutations : 'taco cat','atco cta' etc)


class PalindromePerm:
	def palindromePerm(self,str):
		# Join string together
		# str1 = str.replace(" ","")
		str1 = "".join(str.split())
		print(str1)
		countAlphabet = {}
		count=0
		for char in str1:
			if char in countAlphabet:
				countAlphabet[char]+=1
			else:
				countAlphabet[char]=1
		print(countAlphabet)
		for k,v in countAlphabet.items():
			if v%2!= 0:
				count+=1
			if count>1:
				return False

		return True


if __name__ == '__main__':
	obj = PalindromePerm()

	str = input('Enter the string to check : ')
	print(obj.palindromePerm(str))