import string

# Positive and Negative word lists
positive = [
    "good", "happy", "excellent", "great", "awesome", "love",
    "amazing", "fantastic", "nice", "wonderful", "best",
    "positive", "enjoy", "cool", "brilliant", "super",
    "perfect", "pleased", "delight", "satisfied"
]

negative = [
    "bad", "sad", "poor", "worst", "hate", "angry",
    "terrible", "awful", "horrible", "disappointing",
    "negative", "pain", "ugly", "annoying", "fail",
    "boring", "problem", "issue", "frustrating", "depressed"
]

# Input text
text = input("Enter text: ").lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Convert to words
words = text.split()

pos = 0
neg = 0

# Count sentiment words
for word in words:
    if word in positive:
        pos += 1
    elif word in negative:
        neg += 1

# Output scores
print("\nPositive score:", pos)
print("Negative score:", neg)
print("Total words analyzed:", len(words))

# Final sentiment result
if pos > neg:
    print("Sentiment: Positive 😊")
elif neg > pos:
    print("Sentiment: Negative 😡")
else:
    print("Sentiment: Neutral 😐")
