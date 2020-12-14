# Given two string,write a method to decide if one is a permutation of the other or not

# The basic approach would be to check if the sorted strings are similar or not

# Ask the question that is it case-insensitive? does whitespace count ? Here we have assumed white space doesn't count
#  and it is case-sensitive i.e dog != God

#The second approach is to count the number of characters in both the string and comparing them in seperated lists. 



class PermutationString:
	
	def brutePermutation(self,str1,str2):
		if sorted(str1).strip() == sorted(str2):
			return True
		else:
			return False
	def optimizedPermutation(self,str1,str2):
		# char_limit = 128
		count1= [0]*128
		count2 = [0]*128
		if(len(str1)!=len(str2)):
			return False

		for i in str1:
			count1[ord(i)]+=1
		for j in str2:
			count2[ord(j)]+=1

		if count1!=count2:
				return False
		else:
				return True

if __name__ == '__main__':
	obj = PermutationString()
	str1= input('Enter the first string :  ').strip()
	str2= input('Enter the second string :  ').strip()

	print(obj.optimizedPermutation(str1,str2))