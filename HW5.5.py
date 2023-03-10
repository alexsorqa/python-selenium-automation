"""Create a function that will take a string as an input and return the 1st unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?
"""

def unique(word):
    word = word.lower()
    count = 0
    letters = []
    for letter in word:
        if not letter.isalpha():
            continue
        else:
            count += word.count(letter)
            if letter not in letters:
                letters.append(letter)
            if count > 1:
                count = 0
            else:
                return letter
    if len(letters) <= 2:
        return '""'

print(unique("Google"))
print(unique("Amazon"))
print(unique("xoxoxo"))