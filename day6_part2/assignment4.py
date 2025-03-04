text = 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming. '

text = text.lower()
text = text.replace(" ", "")
text = text.replace(",", "")
text = text.replace("-", "")
text = text.replace(".", "")

print(text)

dict_of_letterandcount = {}

for char in text :

    if dict_of_letterandcount.get(char) == None :
        dict_of_letterandcount[char] = 1
    else :
         dict_of_letterandcount[char] = dict_of_letterandcount.get(char) +1

print(f"the modified dict is {dict_of_letterandcount}")