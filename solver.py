import networkx as nx

def gengraph(width, height, holes):
	g = nx.Graph();
	for x in range(width):
		for y in range(height):
			if x+1 < width:
				g.add_edge((x,y), (x+1,y))
			if y+1 < height:
				g.add_edge((x,y), (x,y+1))
	for hole in holes:
		g.remove_node(hole)
	return g

def solve(g, start, total):
	counter = 0
	### Prune the search space ###
	# If the solution splits the puzzleboard into two areas, it is not solvable
	#if nx.number_connected_components(g) > 1:
	#	return {'sol':[start],'counter':counter}
	# If the puzzle leaves more than 1 dead end, it is not solvable
	#if len([node for node in g.nodes() if g.degree(node)==1 and node != start]) > 1:
	#	return {'sol':[start],'counter':counter}
	### end pruning ###
	nextsol = []
	nextg = nx.Graph(g)
	nextg.remove_node(start)
	for neigh in g[start]:
		counter += 1
		sol = solve(nextg, neigh, total-1)
		nextsol = [start] + sol['sol']
		counter += sol['counter']
		if len(nextsol) == total:
			return {'sol':nextsol,'counter':counter}
	return {'sol':[start],'counter':counter}

def ppsol(sol):
	for i in range(1,len(sol)):
		p2 = sol[i]
		p1 = sol[i-1]
		diff = (p2[0]-p1[0], p2[1]-p1[1])
		if diff == (-1, 0):
			print("l ", end="")
		if diff == (1, 0):
			print("R ", end="")
		if diff == (0, -1):
			print("u ", end="")
		if diff == (0, 1):
			print("D ", end="")
	print()


#####################################################################

if __name__ == "__main__":
	# Level 33
	# Width, height, [position of black squares]
	g = gengraph(6, 8,[
		(4,0),
		(3,1),
		(1,2),
		(5,2),
		(5,3),
		(0,7),
		(5,7),
	])
	# (starting square)
	sol = solve(g, (3,0), len(g.nodes()))
	ppsol(sol['sol'])
	print(sol['counter'])
	print(len(sol['sol']))