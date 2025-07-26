import numpy as np

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_arr = np.array(sorted(seats))  # 12 12 14 19 19
        students_arr = np.array(sorted(students)) # 2 7 17 19 20

        return int((abs(seats_arr - students_arr)).sum())