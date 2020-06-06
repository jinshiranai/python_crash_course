#PCC Try It Yourself 6-3. Glossary

glossary = {
    'none': 'A special value indicating the absence of a value',
    'dictionary': 'A collection of key-value pairs',
    'key-value pair': 'A set of values associated with each other',
    'conditional test': 'An expression that can be evaluated as either True or False',
    'boolean value': 'Either true or false. Often used to keep track of certain conditions',
    }

print(f"None:\n\t{glossary.get('none')}.\n")
print(f"Dictionary:\n\t{glossary['dictionary']}.\n")
print(f"Key-Value Pair:\n\t{glossary['key-value pair']}.\n")
print(f"Conditional Test:\n\t{glossary['conditional test']}.\n")
print(f"Boolean Value:\n\t{glossary.get('boolean value')}.\n")
print(f"Common Sense:\n\t{glossary.get('common sense')}.\n")