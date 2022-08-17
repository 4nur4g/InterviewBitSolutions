# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
# Example 1:
# Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].
A = [ (1, 2), (3, 6) ]
B = (10, 8)

def insert(intervals, new_interval):
    finalintervals = []
    if new_interval[0] > new_interval[1]:
        corr_new_interval = [new_interval[1],new_interval[0]]

    for i in range(len(intervals)):
        if corr_new_interval[1] < intervals[i][0]:
            finalintervals.append(tuple(corr_new_interval))
            return finalintervals + intervals[i:]
        elif corr_new_interval[0] > intervals[i][1]:
            finalintervals.append(intervals[i])
        else: 
            corr_new_interval = [min(intervals[i][0],corr_new_interval[0]),max(intervals[i][1],corr_new_interval[1])]
    
    finalintervals.append(tuple(corr_new_interval))
    return finalintervals

print(insert(A,B))

            
        
        
        
            

