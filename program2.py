class Solution(object):
   def TestRomanToInt(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    n = len(s)
    for i in range(n):
        if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    return total

# Test cases
print("III")    # Output: 3
print(("LVIII"))   # Output: 58
print("MCMXCIV") # Output: 1994




