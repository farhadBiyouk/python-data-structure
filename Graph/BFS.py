def bfs(G, s, v):
	q = []
	v.append(s)
	q.append(s)
	while q:
		m = q.pop(0)
		print(m, end=' ')
		for n in G[m]:
			if n not in v:
				v.append(n)
				q.append(n)
