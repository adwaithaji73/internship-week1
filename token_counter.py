#cli token counter for week 1 and 2
import tiktoken
import sys

PRICES = {
    "gpt-4o":        2.50,
    "gpt-3.5-turbo": 0.50,
    "claude-sonnet": 3.00,
    "claude-haiku":  0.25,
}

def count_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    return len(tokens)

def estimate_cost(token_count, model):
    price_per_million = PRICES[model]
    return (token_count / 1_000_000) * price_per_million

def main():
    print("=" * 40)
    print("   TOKEN COUNTER — Week 1-2 Project")
    print("=" * 40)

    file_name = input("\nEnter file name: ").strip()

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"\n❌ File '{file_name}' not found.")
        sys.exit(1)

    print("\nAvailable models:")
    for model in PRICES:
        print(f"  - {model}")

    model = input("\nEnter model name: ").strip()

    if model not in PRICES:
        print("❌ Unknown model.")
        sys.exit(1)

    token_count = count_tokens(content)
    cost = estimate_cost(token_count, model)

    print("\n" + "=" * 40)
    print(f"  File:               {file_name}")
    print(f"  Model:              {model}")
    print(f"  Characters:         {len(content):,}")
    print(f"  Tokens:             {token_count:,}")
    print(f"  Cost (1 call):      ${cost:.6f}")
    print(f"  Cost (1k calls):    ${cost * 1_000:.4f}")
    print(f"  Cost (100k calls):  ${cost * 100_000:.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
