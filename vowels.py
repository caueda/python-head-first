def search_for_vowels(word):
    """Display any vowels found in a supplied word."""
    vowels = ('a',',','e','i','o','u')
    found = { }

    for letter in word:
        if letter in vowels:
            found.setdefault(letter, 0)
            found[letter] += 1

    for k, v in sorted(found.items()):
        print(f"{k} was found {v} times")