def count_vowels(s):
    count = 0
    vowels = []
    
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
            vowels.append(ch)
    
    return count, vowels

print(count_vowels("hello"))