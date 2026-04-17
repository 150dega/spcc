# -------------------------------
# PASS 1 (IMPROVED - LIST ONLY)
# -------------------------------

program = [
    "START 100",
    "MOVER AREG, X",
    "ADD BREG, X",
    "X DS 1",
    "END"
]

# Opcode table (list)
optab = ["START", "END", "MOVER", "ADD", "DS"]

LC = 0

# Symbol Table → [symbol, address]
symtab = []

# Intermediate Code
IC = []

for line in program:
    parts = line.replace(",", "").split()

    # START
    if parts[0] == "START":
        LC = int(parts[1])
        IC.append(["START", LC])
        continue

    # END
    if parts[0] == "END":
        IC.append(["END"])
        break

    # CHECK LABEL
    if parts[0] not in optab:
        label = parts[0]
        symtab.append([label, LC])
        parts = parts[1:]

    opcode = parts[0]

    # DS (Declarative)
    if opcode == "DS":
        size = int(parts[1])
        IC.append(["DS", size])
        LC += size

    # Instruction
    else:
        operands = parts[1:]
        IC.append([opcode] + operands)
        LC += 1


# -------------------------------
# OUTPUT
# -------------------------------

print("SYMTAB:")
for s in symtab:
    print(s)

print("\nIC:")
for i in IC:
    print(i)
#pass1.py
#RUn:
#cd Desktop
#python3 pass1.py
