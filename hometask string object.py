import re

# исходный текст
text = """ tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# 1. нормализация регистра
text = text.lower()

# первая буква каждого предложения заглавная
sentences = re.split(r'([.!?])', text)
normalized = ""

for i in range(0, len(sentences) - 1, 2):
    sentence = sentences[i].strip()
    mark = sentences[i + 1]

    if sentence:
        sentence = sentence[0].upper() + sentence[1:]
        normalized += sentence + mark + " "

text = normalized.strip()

# 2. исправление "iz" -> "is" только как отдельного слова
text = re.sub(r'\biz\b', 'is', text, flags=re.IGNORECASE)

# 3. собрать последние слова каждого предложения
parts = re.findall(r'([^.!?]+)[.!?]', text)

last_words = []
for part in parts:
    words = re.findall(r"[A-Za-z0-9]+", part)
    if words:
        last_words.append(words[-1])

new_sentence = " ".join(last_words).capitalize() + "."

text += " " + new_sentence

# 4. подсчёт всех whitespace символов
spaces_count = sum(1 for ch in text if ch.isspace())

# вывод
print(text)
print("Количество whitespace символов:", spaces_count)