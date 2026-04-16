import string

text1 = input("Enter first text: ").lower()
text2 = input("Enter second text: ").lower()

# Remove punctuation
text1 = text1.translate(str.maketrans('', '', string.punctuation))
text2 = text2.translate(str.maketrans('', '', string.punctuation))

words1 = set(text1.split())
words2 = set(text2.split())

common = words1.intersection(words2)

if len(words1) == 0:
    similarity = 0
else:
    similarity = (len(common) / len(words1)) * 100

print("\nCommon words:", common)
print("Similarity Score:", round(similarity, 2), "%")
