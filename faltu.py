import random

responses = [
    "poogal ho ap",
    "KAMTAM",
    "Maluga meh",
    "yeh raaatay yeh mausam",
    "Kya hai",
    "tang mat kara",
    "insaan bana",
    "demag ke keeray",
    "kuch toh",
    "teri meh",
    "yahi kuch toh",
    "gian hai ap",
    
]

print("Welcome to the Magic 8 Ball!")

while True:
    question = input("Ask a question (or type 'quit' to exit): ")
    if question.lower() == "quit":
        break
    print("Shaking the 8 Ball...")
    print(random.choice(responses))
