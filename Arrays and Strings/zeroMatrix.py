from rich import print

class ZeroMatrix : 
	def zeroMatrix(self,matrix):
		n = len(matrix)
		if n ==0:
			return matrix

		m= len(matrix[0])
		ZERO_ROWS ,ZERO_COLS=[],[]
		for rows in range(n):
			for cols in range(m):
				if matrix[rows][cols] ==0 :
					ZERO_ROWS.append(rows)
					ZERO_COLS.append(cols)
					break
		for rows in ZERO_ROWS:
			for cols in range(m):
				matrix[rows][cols]= 0
		for cols in ZERO_COLS:
			for rows in range(n):
				matrix[rows][cols]= 0

		return matrix





if __name__ == '__main__':
	obj = ZeroMatrix();
	matrix = [[1,2,3],
			  [4,5,6],
			  [7,8,0],
			  [3,4,1]]
	print('[bold magenta]The original matrix : [/bold magenta]',matrix);
	print('The zero Matrix : ', obj.zeroMatrix(matrix))