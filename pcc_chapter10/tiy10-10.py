# Try It Yourself 10-10. Common Words.

filenames = ['alice.txt', 'the_iliad.txt', 'little_women.txt']

for filename in filenames:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()

    word_count = contents.lower().count('the ')

    print(f"The word 'the' appears in {filename} approximately {word_count} times.")