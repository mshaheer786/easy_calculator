def words_to_num(words):
    units = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19
    }

    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }

    scales = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1_000_000
    }

    words = words.lower().replace("-", " ").split()
    current = 0
    total = 0

    for word in words:
        if word in units:
            current += units[word]
        elif word in tens:
            current += tens[word]
        elif word in scales:
            current *= scales[word]
            total += current
            current = 0
        elif word == "and":  # ignore "and" in numbers
            continue
        else:
            raise ValueError(f"Unknown number word: {word}")

    return total + current

def get_number(prompt):
    value = input(prompt)
    try:
        return int(value)  # Try normal integer
    except ValueError:
        return words_to_num(value)  # Convert from words


num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operator = input("Enter the operator (+,-,*,/,%,**): ")
operator= operator.strip().lower()

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
elif operator == "/":
    if num2 == 0:
        result = "Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operator"
    
print(f"The result is: {result}")
