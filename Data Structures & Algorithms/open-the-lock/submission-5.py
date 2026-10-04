from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        for each position we can turn clockwise or counter clockwise

        if a position is blocked then we have to try turning the other way

        """

        #edge case

        if "0000" in deadends:
            return -1



        #BFS solution
        def bfs(start):
            q = deque()
            visited = set()
            q.append([start, 0])
            visited.add(start)

            while q:
                lockState, step = q.popleft()
   
                if lockState == target:    
                    return step

                for i in range(len(lockState)): #try all next positions
                    currWheelState = lockState[i]
                    if currWheelState == '9':
                        upWheelState = '0'
                    else:
                        upWheelState = str(int(currWheelState) + 1)
                    if currWheelState == '0':
                        downWheelState = '9'
                    else:
                        downWheelState = str(int(currWheelState) - 1)
                    
                    
                    upLockState = lockState[:i] + upWheelState + lockState[i + 1:]
                    downLockState = lockState[:i] + downWheelState + lockState[i + 1:]


                    if upLockState not in visited and upLockState not in deadends:
                        visited.add(upLockState)
                        q.append([upLockState, step + 1])
                    
                    if downLockState not in visited and downLockState not in deadends:
                        visited.add(downLockState)
                        q.append([downLockState, step + 1])
            return -1
                        
        return bfs("0000")
        