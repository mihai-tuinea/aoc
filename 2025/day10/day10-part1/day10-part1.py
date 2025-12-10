result = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split()
        diagram = parts[0][1:-1]
        buttons = parts[1:-1]
        joltage = parts[-1]

        diagram_val = 0
        for index, char in enumerate(diagram):
            if char == "#":
                diagram_val += 2**index

        buttons_vals = []
        for button in buttons:
            nums = [int(x) for x in button[1:-1].split(",")]
            button_val = 0
            for n in nums:
                button_val += 2**n
            buttons_vals.append(button_val)

        num_buttons = len(buttons_vals)
        fewest_presses = float("inf")
        total_combinations = 2**num_buttons

        for combination in range(0, total_combinations):
            current_state = 0
            press_count = 0

            for button_index in range(0, num_buttons):
                is_pressed = (combination >> button_index) & 1

                if is_pressed:
                    press_count += 1
                    current_state = current_state ^ buttons_vals[button_index]

            if current_state == diagram_val:
                if press_count < fewest_presses:
                    fewest_presses = press_count

        result += fewest_presses

print(result)
