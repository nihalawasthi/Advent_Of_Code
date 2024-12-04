import re
with open('day_3.txt', 'r') as file:
    data = file.read()

pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
matches = re.findall(pattern, data)
result1 = sum(int(x) * int(y) for x, y in matches)

print("Sum of all results 1:", result1)


mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
control_pattern = r"\b(do|don't)\(\)"
mul_matches = re.finditer(mul_pattern, data)
control_matches = re.finditer(control_pattern, data)

control_instructions = {match.start(): match.group() for match in control_matches}
enabled = True

result = 0
for match in mul_matches:
    position = match.start()
    relevant_controls = {pos: instr for pos, instr in control_instructions.items() if pos < position}
    if relevant_controls:
        latest_control = relevant_controls[max(relevant_controls.keys())]
        enabled = (latest_control == "do()")
    if enabled:
        x, y = map(int, match.groups())
        result += x * y

print("Sum of enabled results 2:", result)
