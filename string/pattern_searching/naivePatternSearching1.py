# naive pattern searching algorithm 
def naivePatternSearching(Str1,Str2):
    n = len(Str1)
    m = len(Str2)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if Str1[i+j] != Str2[j]:
                break
            j += 1
        if j == m:
            print(f"The Pattern exist in the position of : {i}")
            
            
str1 = "AABAACAADAABAAABAA"
pattern = "AABA"

# print the result
naivePatternSearching(str1,pattern)