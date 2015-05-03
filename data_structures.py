matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

print [[v**2 for i,v in enumerate(b)] for a,b in enumerate(reversed(matrix))]