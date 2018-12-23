Solution of the Adobe DevOps Programming Test (Problem Description in `Programming Test.pdf`)

## Requirements
- Linux based system
- Download and install [docker]. Create an account if you don't already have one.

## Steps to deploy the script in docker
- Login to docker registery (`docker login` in terminal)
- Go to source file,  and run following commands:

    - `docker build -t min_net_container .`
    (This command will create the container with name 'min_net_container')

    - `docker run min_net_container`

- The report will be printed as follows:
<img src = "./report.png">


### Runtime Analysis
- We are representing the graph as an adjacency matrix, the runtime time is O(|V|<sup>2</sup>) where V is the number of vertices the graph contains. If we want to optimize it even more to get runtime of O(ELogV) where E is the number of edges and V is the number of vertices the graph containts, we can implement the solution [using adjaceny list].

### Time Spent: 5-6 hrs

### References:
- https://coderbyte.com/algorithm/find-minimum-spanning-tree-using-prims-algorithm


[docker]: https://www.docker.com/get-started
[using adjaceny list]: https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/

