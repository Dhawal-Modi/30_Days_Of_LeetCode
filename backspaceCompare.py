def backspaceCompare(self, S: str, T: str) -> bool:
    def build(S):
        ans = []
        for x in S:
            if x != '#':
                ans.append(x)
            elif ans:
                ans.pop()
        return "".join(ans)
    return build(S) == build(T)
    
"""if __name__ == "__main__":
    S = str(input())
    T = str(input())
    backspaceCompare(S,T)"""
