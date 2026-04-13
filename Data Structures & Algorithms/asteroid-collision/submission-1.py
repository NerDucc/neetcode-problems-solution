class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] == -a:
                    stack.pop()
                elif stack[-1] < -a:
                    stack.pop()
                    continue
                break
            else:
                stack.append(a)
        return stack
                
                    
