from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0

        student_queue = deque()
        sandwiches_queue = deque()

        sandwiches.reverse()

        while sandwiches:
            sandwiches_queue.append(sandwiches.pop())
        
        while students:
            student_queue.append(students.pop())

        
        while student_queue and count < len(student_queue):
            if student_queue[0] == sandwiches_queue[0]:
                student_queue.popleft()
                sandwiches_queue.popleft()
                count = 0
            else:
                count += 1
                student_queue.append(student_queue.popleft())
        
        return count