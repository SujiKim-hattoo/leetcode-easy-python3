class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # bit calculation
        start_bin = bin(start)[2:]  # c.f. bin() -> 0bxxxx..
        goal_bin = bin(goal)[2:]  

        # length manipulation - .zfill()
        max_bin = max(len(start_bin), len(goal_bin))
        start_bin =  start_bin.zfill(max_bin)
        goal_bin = goal_bin.zfill(max_bin)

        count = 0  # conversiosn number
        # bit flips ver1. 
        # for a, b in zip(start_bin, goal_bin):
        #     if a != b:
        #         count += 1

        # bit flips ver2. - using XOR
        for a, b in zip(start_bin, goal_bin):
            count += int(a) ^ int(b)  # c.f. different -> return 1

        return count 
        