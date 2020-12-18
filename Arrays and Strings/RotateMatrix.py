from rich import print

# The task is to rotate a matrix by 90 degrees
 

class RotateMatrix:
	def rotateMatrix(self,matrix):
		rows = len(matrix)
		cols = len(matrix[0])
		# print(rows)
		if rows!=cols :
			return -1
		# Transpose of matrix
		for i in range(rows):
			for j in range(i+1,rows):
				matrix[i][j],matrix[j][i] =matrix[j][i],matrix[i][j]
				# print(matrix)
		# Mirror the matrix to get the output
		for i in range(rows):
			for j in range(rows//2):
				matrix[i][j],matrix[i][rows-1-j] =matrix[i][rows-1-j],matrix[i][j]
				# print(matrix)
		return matrix


if __name__ =="__main__":
	obj = RotateMatrix();

	matrix = [[1,2,3],
			  [4,5,6],
			  [7,8,0],]
	print('[bold magenta]Original Matrix[/bold magenta]:\n',matrix)
	print('\n')
	print('[bold magenta]Matrix after rotation[/bold magenta]:\n',obj.rotateMatrix(matrix))