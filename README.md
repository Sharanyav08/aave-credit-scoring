
# DeFi Wallet Credit Scoring - Aave V2 Protocol

This project assigns a credit score (from 0 to 1000) to wallets based on their behavior on the Aave V2 DeFi protocol.

## Rules Used for Scoring:

- +10 for every `deposit`
- +5 for every `repay`
- -20 for every `liquidationcall`
- Base score: 500
- Final score limited between 0 and 1000

## How to Use:

1. Place your `user_transactions.json` file in the same folder
2. Run `score_generator.py` (or the Colab notebook)
3. Output will be saved to `wallet_scores.json`
