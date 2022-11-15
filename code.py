def maximumWealth( accounts: List[List[int]]) -> int:
        return max([sum(lst) for lst in accounts])
