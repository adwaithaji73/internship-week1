#cli token counter for week 1 and 2
import tiktoken
import sys
prices = {
    "gpt-4o": 2.50,
    "gpt-4-turbo": 10.00,
    "gpt-3.5-turbo": 0.50
}

file = input("enter filename:")

try:
    with open(file,"r") as f:
        text = f.read()
except FileNotFoundError:
    print("file doesnt exist")
    sys.exit(1)



enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode(text)
count = len(tokens)



print("\nAvailable Models:")
for model in prices:
    print(model)
model = input("\nChoose model: ").strip()
if model not in prices:
    print("Unknown model")
    sys.exit(1)
 
cost = (count / 1000000) * prices[model]




print("\n===== RESULT =====")

print("File       :", file)
print("Characters :", len(text))
print("Tokens     :", count)
print("Model      :", model)
print("Cost       : $", round(cost, 6))