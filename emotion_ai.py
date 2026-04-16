import string

happy = [
    "happy", "joy", "excited", "great", "good", "amazing", "awesome",
    "fantastic", "wonderful", "delighted", "pleased", "smile",
    "cheerful", "content", "satisfied", "brilliant", "love",
    "enjoy", "glad", "positive", "blessed", "thrilled"
]

sad = [
    "sad", "depressed", "cry", "unhappy", "down", "upset",
    "heartbroken", "miserable", "lonely", "tired", "bad",
    "hurt", "disappointed", "gloomy", "negative", "pain",
    "sorrow", "grief", "regret", "hopeless"
]

angry = [
    "angry", "mad", "furious", "annoyed", "irritated",
    "frustrated", "rage", "hate", "aggressive", "offended",
    "disgusted", "outraged", "yelling", "shouting",
    "argument", "fight", "temper", "hostile"
]

# Input
text = input("Enter text: ").lower()

# Clean text
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()

h = 0
s = 0
a = 0

# Count emotions
for word in words:
    if word in happy:
        h += 1
    elif word in sad:
        s += 1
    elif word in angry:
        a += 1

print("\nHappy score:", h)
print("Sad score:", s)
print("Angry score:", a)

# Result
if h > s and h > a:
    print("Emotion: Happy 😄")
elif s > h and s > a:
    print("Emotion: Sad 😢")
elif a > h and a > s:
    print("Emotion: Angry 😡")
else:
    print("Emotion: Neutral 😐")
