a =  """tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""




b = a.lower()
c = b.replace("iz", "is")
d = c.split(".")
d = [s.strip() for s in d]

last_words = []
for s in d:
    if s:  # чтобы пропустить пустые строки
        words = s.split()
        last_words.append(words[-1])

new_sentence = " ".join(last_words) + "."
result = c + " " + new_sentence
count = sum(1 for ch in result if ch.isspace())
print(count)

print(result)
