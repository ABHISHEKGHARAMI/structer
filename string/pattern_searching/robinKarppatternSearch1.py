# "Robin Karp" algorithm for pattern searching.
'''
algorithm for  -
Initially calculate the hash value of the pattern.

Start iterating from the starting of the string:
    Calculate the hash value of the current substring having length m.
    If the hash value of the current substring and the pattern are same check if the substring is same
    as the pattern.
    
    If they are same, store the starting index as a valid answer.
    
    Otherwise, continue for the next substrings.
    
    Return the starting indices as the required answer.
    
    
'''

def robinKarpSearching(text,pattern):
    n = len(text)
    m = len(pattern)
    # define the modulous value
    d = 256
    # define the value probably
    q = 101
    # define the hash value to 1
    h = 1
    # define for the hash value of text
    t = 0
    # define the the hash value of the pattern
    p = 0
    # now done with the intialization then go for the hash value . 
    for i in range(m - 1):
        h = ( h * d ) % q 
        
    # after find the hash value go for the first window of the text and pattern
    for i in range(m):
        t = ( d * t + ord(text[i])) % q
        p = ( d * p + ord(pattern[i])) % q
        
    # after doing that go fo the comparison for the first window if not match then go for the next window
    for i in range(n - m + 1):
        match = True
        if t == p:
            j = 0
            while j < m :
                if text[i + j] != pattern[j]:
                    match = False
                    break
                j += 1
                if j == m:
                    print(f"The pattern found at the position of : {i}")
                    
        # if t != m then go for the next slide
        if i < n - m :
            t = ( d * (t - ord(text[i])* h) + ord(text[i + m])) % q
            if t < 0:
                t += q
                
                
                
                
# testing the main function
text = "AABAACAADAABAAABAA"
pattern = "AABA"

robinKarpSearching(text,pattern)