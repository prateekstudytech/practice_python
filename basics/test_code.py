def first_non_repeating_char(string):
    ch_counts = {}
    
    for ch in string:
        ch_counts[ch] = 1 + ch_counts.get(ch, 0)
        if ch_counts[ch] > 1:
            return ch
    return None


print( first_non_repeating_char('leetcode') )
