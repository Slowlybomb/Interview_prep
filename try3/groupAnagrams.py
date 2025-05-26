MAX_CHAR = 26

def getHash(s):
    """Generate hash of word by counting appearance of every word."""
    hashList = []
    freq = [0] * MAX_CHAR
    
    # Count frequency of each character
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    
    # Append the frequency to construct the hash
    for i in range(MAX_CHAR):
        hashList.append(str(freq[i]))
        hashList.append("$")
    
    return ''.join(hashList)

def groupAnagrams(arr):
    """Get hash of key and compare with """
    res = []
    mp = {}
    
    for i in range(len(arr)):
        key = getHash(arr[i])
        
        # If key is not present in the hash map, add
        # an empty group (list) in the result and
        # store the index of the group in hash map
        if key not in mp:
            mp[key] = len(res)
            res.append([])
        
        # Insert the string in its correct group
        res[mp[key]].append(arr[i])
    
    return res

if __name__ == "__main__":
    arr = ["act", "god", "cat", "dog", "tac"]
    
    res = groupAnagrams(arr)
    for group in res:
        for word in group:
            print(word, end=" ")
        print()