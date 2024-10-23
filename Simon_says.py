def simon_instructions(command_list):
    total_operations = 0
    for cmd in command_list:
        if "Simon says" in cmd:
            action = cmd.replace("Simon says ", "")
            parts = action.split()
            operation = parts[0]

            if operation == "add":
                total_operations += int(parts[1])
            elif operation == "subtract":
                total_operations -= int(parts[1])
            elif operation == "multiply" and parts[1] == "by":
                total_operations *= int(parts[2])
    
    return total_operations

print(simon_instructions([
    "Simon says add 4",
    "Simon says add 6",
    "Then add 5"
]))

print(simon_instructions([
    "Susan says add 10",
    "Simon says add 3",
    "Simon says multiply by 8"
]))

print(simon_instructions([
    "Firstly, add 4",
    "Simeon says subtract 100"
]))
