def group_anagrams(strings):
    
    string_map = {}
    
    for string in strings:
        char_map = [0]*26
        for ch in string:
            char_map[ord(ch) - ord('a')] += 1
        char_map = tuple(char_map)
        if char_map not in string_map:
            string_map[char_map] = []
        string_map[char_map].append(string)
    
    return string_map.values()

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
