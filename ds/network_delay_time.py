
class UniqueEmails:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def remove_dot(local_name):
            a=local_name.split('.')
            a="".join(a)
            return a
        def remove_plus(local_name):
            a=local_name.split('+')
            return a[0]
        
        seen=set()
        
        for x in emails:
            local_name,domain=x.split("@", maxsplit=1)
            local_name=remove_dot(local_name)
            local_name=remove_plus(local_name)
            
            seen.add(local_name+"@"+domain)
            
        
        #set length is answer
        return len(seen)
class NetworkLatency:

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        Approach:
        put the given node in a queue
        mark its cost vector to zero
        mark it visited?
        repeat following:
            item= pop item from queue
            if queue empty:
                break
            #following for each unvisited wont work
            #for example, s->1 and s->3->4->1 are two path, second cost wont be taken
            #into account.
            //for each unvisited neighbor of item: #1 will have no neighbor, 3 will have
            for each neighbor of item:
                if not_visited
                    #when 2 is popped of [1,3] are being processed [-1,1,0,1,-1]
                    #when 3 is popped [-1,1,0, 1, -1]: cost[src,4]=cost(3,4)+cost(src,3)
                    update cost_vector frm src (ie if prev_cost[s,4] < cost(3,4+cost(src,3)
                    mark neighbor visited
                    put neighbor in queue #queue=[4], [-1,1,0,1,2]
                elif already visited:#we have another path for this node.
                    update cost_vector frm src  
                
            #end for
        
        if visited vector is True for all nodes:
            return max from cost vector
            
        """
        #Note better approach is to use adjacency matrix
        #rather than adjacency list as edges are 6000 and
        #nodes are just 100 , total possible edges(if its not sparse)
        #though will be 2**100 which is way too much
        #Assumption: there is only one direct path from node i to j[if there are multiple
        #it can be take care while populating neighbors, by picking the smallest associated cost]
        from queue import Queue
        q=Queue(N)           
        visited= [False for x in range(0,N+1)]
        cost= [-1 for x in range(0, N+1)]   
        neighbors= [[] for x in range(0, N+1)]
        #find all neighbors and their cost
        for x in times:
            if neighbors[x[0]]==None:
                neighbors[x[0]]=[(x[1],x[2])]
            else:
                neighbors[x[0]].append((x[1],x[2]))
        print(neighbors)
        #check if source has no neighbors, just return here
        q.put(K)
        cost[K]=0 #K is src
        visited[K]=True
        pass1=False
        while True:
            if q.empty():
                break
            
            tmps=[]
            while not q.empty():
                tmps.append(q.get())
            print(tmps)
            for tj in tmps:
                q.put(tj)
            
            k=q.get()
            
            for (x,c) in neighbors[k]:
                if visited[x]==True:
                    #update possible new cost k->x even if it was visited.
                     
                    tc=cost[k]+c
                    if tc < cost[x]:
                        if pass1:
                            print("cost-vector", cost)
                            print("Pass2:visited,newcost(",tc,")=currentSrc",k,"Cost(",cost[k],")+kToxCost(",c,") is less for neighbor", x,"\'s oldcost",cost[x])       
                        #this might result in cost decrease for other neighbors of x. update
                        #their cost matrix, if so
                        cost[x]= tc
                        
                        #simple example is
                        #[[3,1,4],[3,2,1],[1,2,2],[2,1,2],[3,4,1],[2,4,1], [1,5,1]]
                        #5
                        #3
                        for i,j in neighbors[x]:#This is needed, if for example
                            #there is loop and nodes in the queue[n1,n2] at this level are
                            #reachable by each other
                            tc=cost[x]+j #find_cost(k,x), cost[k] is gauranteed to be valid
                            if cost[i]==-1 or tc < cost[i]:
                                cost[i]=tc
                            #visited[i]=True
                        
                        
                    else:
                        
                        cost[x]=cost[x]#no op
                    continue
                else:
                    tc=cost[k]+c #find_cost(k,x), cost[k] is gauranteed to be valid
                    if cost[x]==-1 or tc < cost[x]:
                        cost[x]=tc
                    visited[x]=True
                    q.put(x)
                print("q-size",q.qsize())
                print("cost:", cost, "processed neighbors of k=", k, neighbors[k], "visited:",x,"visitflag",visited )
            pass1=True
        
        if all(visited[1:N+1]):
            delay=max(cost)
            return -1 if delay==0 else delay
        else:
            return -1
			
class UniqueOccurance:
	'returns unique occurance'
	def singleNumber(self, nums: List[int]) -> int: