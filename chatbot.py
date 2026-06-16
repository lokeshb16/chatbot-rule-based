import re
import random
import datetime

# patterns for each topic - tried to keep it simple
# each intent has keywords and some replies

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening", "namaste", "hii", "helo"],
        "responses": [
            "Hey! How can I help you today?",
            "Hello there! Ask me anything :)",
            "Hi! I can help with college info, jokes, weather topics, and more."
        ]
    },

    "fees": {
        "patterns": ["fee", "fees", "tuition", "payment", "scholarship", "money", "cost", "charges", "pay"],
        "responses": [
            "College fees depend on your branch. CSE/IT is usually around 1.2L per year.",
            "You can check the fee structure on the college website. Scholarships are available for merit students.",
            "For fee payment, visit the accounts section or pay online via the college portal."
        ]
    },

    "exams": {
        "patterns": ["exam", "exams", "test", "schedule", "timetable", "result", "marks", "paper", "backlog", "date sheet"],
        "responses": [
            "Exam schedule is usually uploaded 3 weeks before on the university portal.",
            "Results come out around 45 days after the exam ends.",
            "For backlog exams, apply through the exam section before the deadline."
        ]
    },

    "hostel": {
        "patterns": ["hostel", "room", "accommodation", "mess", "pg", "stay", "warden", "dormitory"],
        "responses": [
            "The college has separate hostels for boys and girls. Fees are around 70k/year with mess.",
            "For hostel allotment, you need to apply in June. Contact the warden for details.",
            "Mess timings: Breakfast 7-9am, Lunch 12-2pm, Dinner 7-9pm."
        ]
    },

    "placement": {
        "patterns": ["placement", "job", "company", "package", "campus", "recruit", "salary", "ctc", "lpa", "hire", "interview"],
        "responses": [
            "Placement cell got 85%+ placements last year. Average package was around 4.2 LPA.",
            "Top companies that visit: TCS, Infosys, Wipro, Cognizant, L&T Infotech.",
            "Register on the placement portal before August 1st to be eligible for campus drives."
        ]
    },

    "joke": {
        "patterns": ["joke", "funny", "laugh", "jokes", "humor", "haha", "make me laugh"],
        "responses": [
            "Why don't scientists trust atoms? Because they make up everything! :D",
            "I told my computer I needed a break... now it won't stop sending me Kit-Kat ads.",
            "Why did the student eat his homework? Because the teacher told him it was a piece of cake!",
            "Debugging is like being the detective in a crime movie where you are also the murderer."
        ]
    },

    "time": {
        "patterns": ["time", "what time", "current time", "time now", "kitna baj"],
        "responses": ["__TIME__"]  # special case, handled below
    },

    "weather": {
        "patterns": ["weather", "rain", "temperature", "hot", "cold", "climate", "forecast", "sunny"],
        "responses": [
            "I can't fetch live weather, but you can check weather.com or Google for your city!",
            "For Nagpur weather, just Google 'Nagpur weather today' - updates in real time.",
            "Monsoon in Nagpur usually hits around June-July. Stay prepared!"
        ]
    },

    "bye": {
        "patterns": ["bye", "goodbye", "exit", "quit", "see you", "later", "thanks", "thank you", "ok bye"],
        "responses": [
            "Goodbye! Good luck with your studies :)",
            "See you later! Take care.",
            "Bye! Feel free to come back anytime."
        ]
    }
}

# fallback replies when nothing matches
fallback_replies = [
    "Hmm, I didn't quite get that. Try asking about fees, exams, hostel, placement, jokes, or weather.",
    "Not sure what you mean. I can help with college info or just chat a bit!",
    "I don't have an answer for that. Try rephrasing or ask something else?"
]


def match_intent(user_input):
    text = user_input.lower().strip()

    for intent_name, data in intents.items():
        for pattern in data["patterns"]:
            # checking if keyword exists in user message
            if re.search(r'\b' + re.escape(pattern) + r'\b', text):
                return intent_name

    return "fallback"


def get_response(intent_name):
    if intent_name == "fallback":
        return random.choice(fallback_replies)

    response = random.choice(intents[intent_name]["responses"])

    # special handling for time intent
    if response == "__TIME__":
        now = datetime.datetime.now()
        return f"Current time is: {now.strftime('%I:%M %p')} (your system time)"

    return response


def show_intro():
    print("=" * 45)
    print("       Welcome to SmartBot!")
    print("  Topics: College Info | Jokes | Weather")
    print("  Type 'bye' or 'exit' to quit")
    print("=" * 45)


def main():
    show_intro()

    # track session stats
    total = 0
    matched = 0

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except KeyboardInterrupt:
            print("\nBot: Session ended. Bye!")
            break

        if not user_input:
            print("Bot: Say something!")
            continue

        total += 1
        intent = match_intent(user_input)

        if intent != "fallback":
            matched += 1

        reply = get_response(intent)
        print(f"Bot: {reply}")

        # show accuracy after every 5 messages
        if total % 5 == 0:
            acc = (matched / total) * 100
            print(f"  [Stats] {total} messages | Recognition rate: {acc:.0f}%")

        # exit condition
        if intent == "bye":
            print(f"\n  -- Session ended | Total: {total} | Recognized: {matched} --")
            break


if __name__ == "__main__":
    main()
