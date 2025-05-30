def greet():
    print("😒 Welcome. I’m CryptoLily — your dead-inside crypto sidekick. Want advice? Fine. Let’s get this over with.")


crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 7/10
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Dogecoin": {
        "price_trend": "rising",
        "market_cap": "low",
        "energy_use": "high",
        "sustainability_score": 2/10
    }
}

#logic
def get_advice(user_query):
    user_query = user_query.lower()

    #greetings
    if user_query in ["hi", "hello", "hey", "yo", "hiya", "sup","oya","sasa","good morning","good afternoon","good evening"]:
        return "CryptoLily: Oh... it’s you again. What do you want this time?"

    if "trending up" in user_query or "rising" in user_query or "growing" in user_query:
        rising_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if rising_coins:
            return f"🙄 Fine. These coins are actually going up: {', '.join(rising_coins)}."
        else:
            return "Wow, nothing's rising. What a time to be alive."

    elif "most sustainable" in user_query or "eco" in user_query or "green" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        score = crypto_db[recommend]["sustainability_score"]
        return f"{recommend}. Sustainability score: {score*10}/10. Not bad, I guess. 🌱"

    elif "long-term growth" in user_query or "should i buy" in user_query:
        candidates = []
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]:
                candidates.append((coin, data["sustainability_score"]))

        if candidates:
            candidates.sort(key=lambda x: x[1], reverse=True)
            best = candidates[0][0]
            score = candidates[0][1]
            return f"{best} looks promising. Trending up with a sustainability score of {score*10}/10. Happy now?"
        else:
            return "Nothing fits your oh-so-specific long-term growth criteria. Try again later."

    else:
        return "Ugh. I didn’t get that. Try saying something useful like 'trending up', 'most sustainable', or 'long-term growth'."

#run the bot
def run_chatbot():
    greet()
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("CryptoLily: Leaving already? Typical. Whatever — remember crypto is risky. Don’t blame me later. 🙃")
            break
        response = get_advice(user_input)
        print(response)

if __name__ == "__main__":
    run_chatbot()

    


