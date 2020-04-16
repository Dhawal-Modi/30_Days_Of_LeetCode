class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move_l = 0
        length = len(s)
        for direction,amount in shift:
            if direction == 0:
                move_l = move_l + amount
            else:
                move_l = move_l - amount
        move_l = move_l % length
        return s[move_l:] + s[:move_l]
