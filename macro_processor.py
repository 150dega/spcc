program = [
    "MACRO",
    "INCR &A",
    "ADD &A, =1",
    "MEND",
    "START 100",
    "INCR X",
    "END"
]

MNT = {}   # Macro Name Table
MDT = []   # Macro Definition Table
output = []

i = 0
while i < len(program):
    line = program[i].strip()

    if line == "MACRO":
        i += 1
        macro_name = program[i].split()[0]
        MNT[macro_name] = len(MDT)

        while program[i].strip() != "MEND":
            MDT.append(program[i])
            i += 1

        MDT.append("MEND")  # include MEND

    elif line.split()[0] in MNT:
        output.append(f"{line} is a macro call")

    else:
        output.append(line)

    i += 1

print("Macro Name Table (MNT):")
for name, index in MNT.items():
    print(f"{name}: {index}")

print("\nMacro Definition Table (MDT):")
for i, definition in enumerate(MDT):
    print(f"{i}: {definition}")
#macro_processor.py
#Run
#cd Desktop
#python3 macro_processor.py
