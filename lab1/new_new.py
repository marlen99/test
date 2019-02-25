def find_z_c(n):
	for k in range(2, n+1):
		if n//k == (n+k-1)//k:
			break
	z = (k+1)//2*(n//k)
	c = k//2*(n//k)
	return (z, c)
	
def fill_square(square, x1, y1, x2, y2, n, cur):
	step_x = 1 if x2 > x1 else -1
	step_y = 1 if y2 > y1 else -1
	for i in range(x1, x2, step_x):
		for j in range(y1, y2, step_y):
			square[i][j] = cur

	
def fill_corner(square, x1, y1, x2, y2, z, c, cur):
	step_x = 1 if x2 > x1 else -1
	step_y = 1 if y2 > y1 else -1
	k = min(c, y2-y1-z)
	l = min(x2-x1-z, c)
	if square[x1+z+l][y1+l] != 0 or square[x1+k][y1+z+k] != 0:
		while square[ ########
	if square[x1+z-step_x][y1+z-step_y] == 0:
		for i in range(x1, x1+z, step_x):
			for j in range(y1, y1+z, step_y):
				square[i][j] = cur
	cur += 1
	if square[x1+c-step_x][y2-step_y] == 0:
		for i in range(x1, x1+k, step_x):
			for j in range(y1+z, y1+z+c, step_y):
				square[i][j] = cur
	cur += 1
	if square[x2-step_x][y1+c-step_y] == 0:
		for i in range(x1+z, x1+z+l, step_x):
			for j in range(y1, y1+l, step_y):
				square[i][j] = cur
	cur += 1
	return cur
	

def find_corners(square):
	x1, x2, y1, y2 = (-1, -1, -1, -1)
	for i in range(0, len(square)):
		for j in range(0, len(square)):
			if square[i][j] == 0:
				break
		if square[i][j] == 0:
			x1 = i
			y1 = j
			break
	if x1 == -1:
		return None
	for i in range(len(square)-1, -1, -1):
		for j in range(len(square)-1, -1, -1):
			if square[i][j] == 0:
				break
		if square[i][j] == 0:
			x2 = i
			y2 = j
			break
	return (x1, y1, x2, y2)
	
def search_empty(n, square):
	ans = None
	for i in range(0, n):
		for j in range(0, n):
			if square[i][j] == 0:
				ans = [i, j]
				break
		if not ans is None:
			break
	#print(ans)
	if not ans is None:
		for j in range(ans[1], n):
			if square[ans[0]][j] != 0:
				j -= 1
				break
		ans.append(min(n-ans[0], j-ans[1]+1))
		return ans

def quadration(n):
	square = [[0 for i in range(0, n)] for j in range(0, n)]
	z, c = find_z_c(n)
	print(z, c)
	cur = fill_corner(square, n-1, n-1, -1, -1, -z, -c, 1)
	for i in square:
		print(*i)
	best = [0 for i in range(0, n*n+1)]
	ans = [[0, 0, z], [0, z, c], [z, 0, c]]
	cur = 4
	while cur != 3:
		new = search_empty(n, square)
		if new is None:
			if len(best) > len(ans):
				best = [ans[i].copy() for i in range(0, len(ans))]
				print(new, best)
				for i in range(0, n):
					print(*square[i])
		#print(new, best)
		#for i in range(0, n):
		#	print(*square[i])
		while new is None:
			if len(ans) == 3:
				return best
			if ans[-1][2] == 1:
				square[ans[-1][0]][ans[-1][1]] = 0
				ans.pop(-1)
				continue
			for i in range(ans[-1][0], ans[-1][0]+ans[-1][2]):
				square[i][ans[-1][1]+ans[-1][2]-1] = 0
			for j in range(ans[-1][1], ans[-1][1]+ans[-1][2]-1):
				square[ans[-1][0]+ans[-1][2]-1][j] = 0
			ans[-1][2] -= 1
			cur = len(ans) + 1
			break
		if new is None:
			continue
		for i in range(new[0], new[0]+new[2]):
			for j in range(new[1], new[1]+new[2]):
				square[i][j] = cur
		ans.append(new)
		cur += 1
	return best
			
		
def main():
	n = int(input())
	print(quadration(n))

if __name__ == '__main__':
	main()
