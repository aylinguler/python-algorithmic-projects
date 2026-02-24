# Arithmetic Arranger: A tool to format and solve arithmetic problems 
# vertically for easy reading, built for the freeCodeCamp certification.

def arithmetic_arranger(problems, show_answers=False):
    # 1. Error Handling: Too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_row = []
    second_row = []
    dash_row = []
    solution_row = []

    for operations in problems:
        op_lst = operations.split()
        first_num = op_lst[0]
        operator = op_lst[1]
        second_num = op_lst[2]

        # 2. Error Handling: Operator check
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # 3. Error Handling: Digits only
        if not first_num.isdigit() or not second_num.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        # 4. Error Handling: Max length
        if len(first_num) > 4 or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Logic for calculation and formatting
        length = max(len(first_num), len(second_num)) + 2
        top = first_num.rjust(length)
        bottom = operator + second_num.rjust(length - 1)
        line = "-" * length
        
        # Calculate result
        if operator == "+":
            res = str(int(first_num) + int(second_num))
        else:
            res = str(int(first_num) - int(second_num))
        
        display_res = res.rjust(length)

        first_row.append(top)
        second_row.append(bottom)
        dash_row.append(line)
        solution_row.append(display_res)

    # Joining the rows with 4 spaces between each problem
    arranged_problems = "    ".join(first_row) + "\n" + \
                        "    ".join(second_row) + "\n" + \
                        "    ".join(dash_row)

    if show_answers:
        arranged_problems += "\n" + "    ".join(solution_row)

    return arranged_problems

if __name__ == "__main__":
    
    test_cases = [
        (["3801 - 2", "123 + 49"], False),
        (["1 + 2", "1 - 9380"], False),
        (["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], False),
        (["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], False),
        (["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], False),
        (["3 / 855", "3801 - 2", "45 + 43", "123 + 49"], False),
        (["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], False),
        (["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"], False),
        (["3 + 855", "988 + 40"], True),
        (["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
    ]
    for i, (problems, show) in enumerate(test_cases, 1):
        print(f"--- Test Case {i} ---")
        print(arithmetic_arranger(problems, show))
        print("\n")
