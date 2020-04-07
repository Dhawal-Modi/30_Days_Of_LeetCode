from collections import defaultdict
def groupAnagrams(n):
    groupedWords = defaultdict(list)
    for i in n:
        groupedWords["".join(sorted(i))].append(i)
        return (list(groupedWords.values()))
        


if __name__ == "__main__":
    n=list(map(str,input().split()))
    groupAnagrams(n)
