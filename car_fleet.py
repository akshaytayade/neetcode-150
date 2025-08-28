class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p,s) for zip in (position, speed)]
        pair.sorted(reverse=True)

        for p,s in pair:
            time_taken = ((target - p) / s)
            stack.append(time_taken)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)