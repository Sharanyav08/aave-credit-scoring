
import json
from collections import defaultdict

# Load transaction data
with open("user_transactions.json", "r") as f:
    transactions = json.load(f)

# Initialize wallet scores
wallet_scores = defaultdict(lambda: 500)

# Define scoring rules
scoring_rules = {
    "deposit": 10,
    "repay": 5,
    "borrow": -5,
    "redeemunderlying": -5,
    "liquidationcall": -20
}

# Process each transaction
for tx in transactions:
    wallet = tx["userWallet"]
    action = tx["action"].lower()

    # Update score if action is in our rules
    if action in scoring_rules:
        wallet_scores[wallet] += scoring_rules[action]

# Clamp scores between 0 and 1000
for wallet in wallet_scores:
    wallet_scores[wallet] = max(0, min(1000, wallet_scores[wallet]))

# Save to JSON
with open("wallet_scores.json", "w") as f:
    json.dump(wallet_scores, f, indent=2)

print("✅ Wallet scores saved to wallet_scores.json")
