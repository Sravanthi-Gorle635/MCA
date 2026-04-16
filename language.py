english = [
    "the", "is", "and", "hello", "hi", "how", "are", "you",
    "this", "that", "what", "where", "when", "why", "who",
    "good", "morning", "night", "please", "thanks", "thank",
    "yes", "no", "okay", "welcome", "friend", "love"
]

spanish = [
    "hola", "gracias", "amigo", "como", "estas", "bien",
    "mal", "por", "favor", "buenos", "dias", "noches",
    "si", "no", "que", "donde", "cuando", "porque",
    "quien", "amor", "feliz", "triste", "comida"
]

french = [
    "bonjour", "merci", "salut", "comment", "ca", "va",
    "bien", "mal", "oui", "non", "plait",
    "bon", "jour", "nuit", "amour", "ami", "heureux",
    "triste", "quoi", "ou", "quand", "pourquoi"
]

# Input
text = input("Enter text: ").lower().split()

eng = sum(word in english for word in text)
spa = sum(word in spanish for word in text)
fre = sum(word in french for word in text)

# Output
if eng > spa and eng > fre:
    print("Language: English 🇬🇧")
elif spa > eng and spa > fre:
    print("Language: Spanish 🇪🇸")
elif fre > eng and fre > spa:
    print("Language: French 🇫🇷")
else:
    print("Language: Unknown 🌐")
