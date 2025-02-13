def dfs(G, s, v):
	if s not in v:
		print(s, end=' ')
		v.append(s)
		for n in G[s]:
			dfs(G, n, v)
