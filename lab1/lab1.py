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
	for i in range(0, (n+1)//2):
		for j in range(0, (n+1)//2):
			square[i][j] = 1
	for i in range(0, n//2):
		for j in range((n+1)//2, n):
			square[i][j] = 2
	for i in range((n+1)//2, n):
		for j in range(0, n//2):
			square[i][j] = 3
	best = [0 for i in range(0, n*n+1)]
	ans = [[0, 0, (n+1)//2], [0, (n+1)//2, n//2], [(n+1)//2, 0, n//2]]
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
