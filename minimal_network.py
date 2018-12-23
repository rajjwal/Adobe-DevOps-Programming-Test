import timeit

# Read 'network.txt' file and return the adjacency matrix and total weight of the network
def ReadNetworkTxt(file_path):
	lines = open(file_path, 'r')
	trueValue = lambda item : 0 if item == '-' else int(item)
	matrix = [[trueValue(item) for item in line.rstrip('\n').split(',')] for line in lines]

	total_weight = 0
	for i in range(0, len(matrix)):
		for j in range(i, len(matrix[0])):
			total_weight += matrix[i][j]

	return (matrix, total_weight)


# optimized version of implementation of Prim's Algorithm here derived from source here:
# https://coderbyte.com/algorithm/find-minimum-spanning-tree-using-prims-algorithm
# returns: weight and list of minimum edges in the adjacency matrix
def PrimsAlgorithm(matrix):
  V = len(matrix)

  # arbitrarily choose initial vertex from graph
  vertex = 0
  
 
  weight = 0 # to store and compute weight of minimal network
  MST = [] # to store all the vertices (nodes) along with the value of edges (weight)
  edges = []
  visited = set() # to store all the visited vertices
  minEdge = [None,None,float('inf')] # initial minimum edge
  
  # run prims algorithm until we create an MST
  # that contains every vertex from the graph
  while len(MST) != V-1:
  	# mark this vertex as visited
    visited.add(vertex)
    
    # add each edge to list of potential edges
    for r in xrange(0, V):
      if matrix[vertex][r] != 0:
        edges.append([vertex,r,matrix[vertex][r]])
        
    # find edge with the smallest weight to a vertex
    # that has not yet been visited
    for e in xrange(0, len(edges)):
      if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
        minEdge = edges[e]
        
    # remove min weight edge from list of edges
    edges.remove(minEdge)

    # push min edge to MST
    MST.append(minEdge)

    weight += minEdge[2]
      
    # start at new vertex and reset min edge
    vertex = minEdge[1]
    minEdge = [None,None,float('inf')]
    
  return (weight, MST)

# driver function of the script
def main():

	start = timeit.default_timer()

	network_matrix, total_network_weight = ReadNetworkTxt('./network.txt')
	minimal_network_weight, mst_v_and_e = PrimsAlgorithm(network_matrix)

	stop = timeit.default_timer()

	print ('************** REPORT *************')

	print ('Original Network Weight: ' + str(total_network_weight))
	

	# print ('Vertex and Edges of Minimal Network \n')
	# print (mst_v_and_e)

	print ('Minimal Network Weight: ' + str(minimal_network_weight))
	print ('Maximum Saving: ' + str(total_network_weight - minimal_network_weight))

	print ('Total Runtime: ' + str (stop - start))

	print ('***********************************')



if __name__ == '__main__':
	main()
