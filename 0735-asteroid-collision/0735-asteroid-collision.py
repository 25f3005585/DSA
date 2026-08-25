class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for i in range(n-1, -1 , -1):
            elem = asteroids[i]

            if elem > 0:
                while stack:
                    top = stack[-1]
                    if top > 0:
                        stack.append(elem)
                        break
                    else:
                        new_top = stack.pop()
                        top = abs(new_top)

                        if top > elem:
                            stack.append(new_top)
                            break

                        elif elem > top:
                            continue

                        else:
                            break
                else:
                    stack.append(elem)
            else:
                stack.append(elem)
        
        stack.reverse()
        return stack