class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = { i : [] for i in range(N)} # i -> [[distance, node]]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1,N):
                x2, y2 = points[j]
                dist = abs(x1- x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        print(adj)

        res = 0
        visit = set()
        minHeap = [[0,0]] #cost, point
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:    
                continue
            res += cost
            visit.add(i)
            for neigCost, neig in adj[i]:
                if neig not in visit:
                    heapq.heappush(minHeap, [neigCost, neig])
        
        return res

        # ans = 0
        # for i in range(len(distances)):
        #     distance_list = distances[i]
        #     min_dist = None
        #     min_index = None
        #     for j in range(len(distance_list)):
        #         distance_to_point = distance_list[j]
        #         if distance_to_point != -1:
        #             if min_dist == None or distance_to_point < 

            