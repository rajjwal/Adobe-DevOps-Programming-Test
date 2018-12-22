def ReadNetworkTxt(file_path):

	lines = open(file_path, 'r')
	trueValue = lambda item : 0 if item == '-' else int(item)
	matrix = [[trueValue(item) for item in line.rstrip('\n').split(',')] for line in lines]

	total_weight = 0
	for i in range(0, len(matrix)):
		for j in range(i, len(matrix[0])):
			total_weight += matrix[i][j]

	return (matrix, total_weight)

def Prims(matrix):
  V = len(matrix)

  # arbitrarily choose initial vertex from graph
  vertex = 0
  
  # initialize empty edges array and empty MST
  MST = []
  edges = []
  visited = set()
  minEdge = [None,None,float('inf')]
  
  # run prims algorithm until we create an MST
  # that contains every vertex from the graph
  while len(MST) != V-1:
  	# mark this vertex as visited
    visited.add(vertex)
    
    # add each edge to list of potential edges
    for r in range(0, V):
      if matrix[vertex][r] != 0:
        edges.append([vertex,r,matrix[vertex][r]])
        
    # find edge with the smallest weight to a vertex
    # that has not yet been visited
    for e in range(0, len(edges)):
      if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
        minEdge = edges[e]
        
    # remove min weight edge from list of edges
    edges.remove(minEdge)

    # push min edge to MST
    MST.append(minEdge)
      
    # start at new vertex and reset min edge
    vertex = minEdge[1]
    minEdge = [None,None,float('inf')]

  sum = 0
  for item in MST:
  	sum += item[-1]
    
  return (sum)

def main():
	network_matrix, total_network_weight = ReadNetworkTxt('./network.txt')

	minimal_network_weight = Prims(network_matrix)

	print (total_network_weight)
	print (minimal_network_weight)

if __name__ == '__main__':
	main()
