class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        processorTime.sort()
        tasks.sort(reverse = True)
        maxTime = 0   
        
        taskIndex = 0
        for time in processorTime:
            if maxTime < time + tasks[taskIndex]:
                maxTime = time + tasks[taskIndex]
            
            taskIndex += 4
        
        return maxTime
