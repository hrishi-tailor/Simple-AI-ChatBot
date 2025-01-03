import json
import random
from rapidfuzz import process, fuzz

# Load intents from file
def load_intents(filename="intents.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"intents": []}

# Save intents to file
def save_intents(intents, filename="intents.json"):
    with open(filename, "w") as file:
        json.dump(intents, file, indent=4)

# Initialize intents
intents = load_intents()

# Add a new intent
def add_new_intent(user_input, response):
    intents["intents"].append({
        "patterns": [user_input],
        "responses": [response]
    })
    save_intents(intents)

# Find the best matching intent
def find_best_match(user_input):
    matches = []
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            score = fuzz.partial_ratio(user_input.lower(), pattern.lower())
            if score >= 80:  # Match threshold
                matches.append((intent, score))
    return matches

# Combine responses from multiple intents
def combine_responses(matches):
    responses = []
    for match, _ in matches:
        responses.extend(match["responses"])
    return " ".join(random.sample(responses, len(responses)))

# Get chatbot response
def get_response(user_input):
    # Create a list of all patterns and their associated intents
    patterns = [(pattern, intent) for intent in intents["intents"] for pattern in intent["patterns"]]
    # Map patterns to their corresponding intents
    patterns_dict = {pattern: intent for pattern, intent in patterns}

    # Use process.extractOne to find the best match for the user input
    result = process.extractOne(user_input, patterns_dict.keys(), scorer=fuzz.partial_ratio)

    if result is None:
        print("Chatbot: I don't understand that yet. How should I respond?")
        new_response = input("You: ")
        add_new_intent(user_input, new_response)
        return "Got it! I'll remember that."

    # Extract best match and score
    best_match = result[0]  # The matched pattern
    score = result[1]       # The score of the match

    matched_intent = patterns_dict[best_match]
    responses = matched_intent.get("responses", [])

    # Define a stricter threshold for matching
    threshold = 80  # Adjust threshold for better matching
    if score >= threshold:
        return random.choice(responses)  # Choose one random response

    # Handle ambiguous intent
    print(f"Chatbot: Did you mean: '{best_match}'? (yes/no)")
    confirmation = input("You: ").strip().lower()
    if confirmation == "yes":
        return random.choice(responses)
    else:
        print("Chatbot: I don't understand that yet. How should I respond?")
        new_response = input("You: ")
        add_new_intent(user_input, new_response)
        return "Got it! I'll remember that."



# Chatbot interaction
print("Chatbot is running! Type 'quit' to exit.")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {get_response(user_input)}")
