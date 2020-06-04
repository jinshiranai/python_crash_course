#PCC TIY 3-10,11
#Use every function learned this chapter

languages = ['english', 'spanish', 'german', 'french', 'japanese']
lang_number = len(languages)
print(f"I have formally studied {lang_number} languages in school. They are:")
print(languages)

print("\nHere they are again in temporary abc order:")
print(sorted(languages))

print("\nHere they are again in temporary reverse abc order:")
print(sorted(languages, reverse=True))

print("\nLet's reverse that original list:")
languages.reverse()
print(languages)

print("\nActually, let's put it back:")
languages.reverse()
print(languages)

print("\nMaybe we should permanently sort this out:")
languages.sort()
print(languages)

print("\nOkay, but how about in permanently in reverse alphabetical order:")
languages.sort(reverse=True)
print(languages)

print("\nOh wait, I did study that little bit of Korean, should we add that?:")
languages.insert(0, 'korean')
print(languages)
print("Actually you know what that wasn't formal study that was just a study group so let's just get rid of it.")
languages.remove('korean')

print("\nThings are all mixed up now. What's the 3rd item on the list?")
print(f"If you guessed {languages[2].title()} you're absolutely right!")
print(languages)

print("\nHere's another question. How many foreign languages did I study in high school?")
languages.remove('japanese')
print(f"I started formal study of Japanese at Clemson, so we can get rid of it.")
print("And English isn't a foreign language for me so it goes bye bye too.")
languages.remove('english')
print("Which leaves us with how many languages?")

lang_number = len(languages)
print(f"That's right! {lang_number}!")

print("\nOkay, last question, I promise. What is currently the last language in the list?")
last = languages.pop()
print(f"If you guessed {last.title()}, that's technically wrong because I popped it for this print.")
print(f"Which means the real answer is {languages[-1].title()}! See:")
print(languages)

print("\nNow to empty the list because I still have to use del:")
del languages[0]
del languages[0]
print(f"See? All gone! {languages}")

#3-11
#print(languages[-1]) returns a list index error because the list is currently empty so there is no last item to reference