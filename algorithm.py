#algorithm.py

def write_file(flag,node,cl):
	Dir_list = ['walkTrap','infoMap','fastGreedy','leadingEigen','labelPropa',\
	'multilevel','optimalModularity','spinGlass','edgeBetweenness']
	with open(Dir_list[flag]+'/'+node+'.circles','w') as f:
		for i in cl:
			f.write('circle:')
			for j in i:
				f.write(str(j)+' ')
			f.write('\n')
def extract_clusters(clusters, reverseIdMap):
    new_clusters = []
    for i in range(len(clusters)):
        next_cluster = [reverseIdMap[j] for j in clusters[i]]
        new_clusters.append(next_cluster)
    return new_clusters
def real_data(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	#print g
	#quit()
	dendogram = g.community_walktrap(steps=4)
	#print '~~~',dendogram.graph()
	#quit()
	cl = dendogram.as_clustering()
	#print cl._formatted_cluster_iterator
	quit()
	walktrapmap_clusters = extract_clusters(cl, reverseIdMap)
	filename =  t.split('/')[1].split('.')[0]
	return cl

def walk_trap(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_walktrap(steps=4)
	cl = dendogram.as_clustering()
	walktrapmap_clusters = extract_clusters(cl, reverseIdMap)
	filename =  t.split('/')[1].split('.')[0]
	write_file(0,filename,list(walktrapmap_clusters))
	return cl	
	#quit()

def infomap(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_infomap(trials=10)
	infomap_clusters = extract_clusters(dendogram, reverseIdMap)
	#print infomap_clusters
	filename =  t.split('/')[1].split('.')[0]
	write_file(1,filename,list(infomap_clusters))
	#quit()

def fast_greedy(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_fastgreedy()
	cl = dendogram.as_clustering()
	fastgreedy_clusters = extract_clusters(cl, reverseIdMap)
	#print fastgreedy_clusters
	filename =  t.split('/')[1].split('.')[0]
	write_file(2,filename,list(fastgreedy_clusters))
	return cl
	
	#quit()

def leading_eigenvector(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_leading_eigenvector()
	leading_eigenvector_clusters = extract_clusters(dendogram, reverseIdMap)
	#print leading_eigenvector_clusters
	filename =  t.split('/')[1].split('.')[0]
	#write_file(3,filename,list(leading_eigenvector_clusters))
	#quit()
def label_propagation(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_label_propagation()
	label_propagation_clusters = extract_clusters(dendogram, reverseIdMap)
	#print label_propagation_clusters
	filename =  t.split('/')[1].split('.')[0]
	write_file(4,filename,list(label_propagation_clusters))

def multilevel(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_multilevel()
	multilevel_clusters = extract_clusters(dendogram, reverseIdMap)
	#print multilevel_clusters
	filename =  t.split('/')[1].split('.')[0]
	write_file(5,filename,list(multilevel_clusters))
	return dendogram

def optimal_modularity(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_optimal_modularity()
	optimal_modularity_clusters = extract_clusters(dendogram, reverseIdMap)
	#write_file(6,t,list(optimal_modularity_clusters))

def spinglass(g,t):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_spinglass()
	#print dendogram
	#quit()
	spinglass_clusters = extract_clusters(dendogram, reverseIdMap)
	#print multilevel_clusters
	filename =  t.split('/')[1].split('.')[0]
	write_file(7,filename,list(spinglass_clusters))
def edge_betweenness(g,t,flag):
	reverseIdMap = {}
	idMap = {}
	currentId = 0
	for friend in g.vs['name']:
		idMap[friend] = currentId
		reverseIdMap[currentId] = friend
		currentId += 1	
	dendogram = g.community_edge_betweenness(directed=flag)
	cl = dendogram.as_clustering()
	edge_betweenness_clusters = extract_clusters(cl, reverseIdMap)
	#print edge_betweenness_clusters
	filename =  t.split('/')[1].split('.')[0]
	write_file(8,filename,list(edge_betweenness_clusters))