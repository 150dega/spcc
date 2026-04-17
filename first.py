# -------------------------------
# Compute FIRST
# -------------------------------

# ε represented as 'ε'
grammar = {
    "S": [["A", "B"]],
    "A": [["a"], ["ε"]],
    "B": [["b"]]
}

first = {}

# Initialize FIRST sets
for nt in grammar:
    first[nt] = set()

# Function to compute FIRST
def compute_first(symbol):
    # If terminal
    if symbol not in grammar:
        return {symbol}

    result = set()

    for production in grammar[symbol]:
        for sym in production:
            sym_first = compute_first(sym)
            result.update(sym_first - {"ε"})

            if "ε" not in sym_first:
                break
        else:
            result.add("ε")

    return result

# Compute FIRST for all non-terminals
for nt in grammar:
    first[nt] = compute_first(nt)

# Print results
print("Grammar:")
for nt in grammar:
    print(f"{nt} -> {grammar[nt]}")

print("\nFIRST sets:")
for nt in first:
    print(f"FIRST({nt}) = {first[nt]}")
#Save:
#first.py
#Run:
#cd Desktop
#python3 first.py
