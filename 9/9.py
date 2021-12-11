matrix = [[ int(ch) for ch in line.strip()] for line in open('9.input.txt')]
lowpoints = [(i,j) for i in range(len(matrix)) for j in range(len(matrix[0]))
			 if ((i == 0 or matrix[i-1][j] > matrix[i][j]) and
			     (i == len(matrix) - 1 or matrix[i + 1][j] > matrix[i][j]) and
			     (j == 0 or matrix[i][j-1] > matrix[i][j]) and
			     (j == len(matrix[0]) - 1 or matrix[i][j+1] > matrix[i][j]))]

print(f"a: {sum([1+matrix[i][j] for i,j in lowpoints])}")

def atb(i,j):
	if 0 <= i < len(matrix) and  0 <= j < len(matrix[0]) and matrix[i][j] != 9:
		matrix[i][j] = 9
		return 1 + atb(i-1,j) + atb(i+1,j) + atb(i,j-1) + atb(i,j+1)
	return 0

basins = sorted([atb(i,j) for i,j in lowpoints], reverse=True)

print(f"b: {basins[0] * basins[1] * basins[2]}")