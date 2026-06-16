# SmartBot - Rule-Based Chatbot

A professional, lightweight, and highly efficient **Rule-Based Chatbot** built using Python. This project was developed as part of the **Week 1 Internship Task**. It utilizes Regular Expressions (`re`) for flexible keyword matching and incorporates dynamic features like live system time retrieval and real-time session tracking.

---

## Key Features

* **Smart Intent Recognition:** Powered by Python's `re` (Regular Expressions) module with word boundary checks (`\b`) to prevent false positives (e.g., matching "exam" but ignoring "example").
* **Dynamic Time Integration:** Automatically fetches and formats the user's current system time using the `datetime` module.
* **Live Session Statistics:** Tracks the total number of queries and dynamically displays the **Bot's Recognition Rate (%)** after every 5 messages.
* **Robust Crash Prevention:** Built-in exception handling (`try-except`) for `KeyboardInterrupt` to ensure the program terminates gracefully without throwing ugly terminal crashes.
* **Randomized Conversational Replies:** Uses the `random` library so the bot gives varying natural responses for the same intent.

---

## 🛠️ Architecture & Core Components

The chatbot is structured into 4 clean, modular parts:
1. **Intents Data Dictionary:** Stores the pre-defined keywords (patterns) and multiple response variants for topics like College Fees, Placement, Hostels, Exams, Weather, and Jokes.
2. **Intent Matcher (`match_intent`):** Normalizes user input (lowercasing/stripping) and scans for pattern matches using regular expressions.
3. **Response Generator (`get_response`):** Handles regular responses and executes custom business logic for special cases (like retrieving the system time).
4. **Main Execution Loop:** Keeps the bot alive in an interactive CLI environment until the user types an exit command (`bye`, `exit`).

---

## 💻 Tech Stack Used

* **Language:** Python 
* **Core Libraries:** `re` (Regex), `random`, `datetime`

---

## 🏃‍♂️ How to Run the Project Locally

### Prerequisites
Make sure you have Python installed on your machine. You can check by running:
```bash
python --version