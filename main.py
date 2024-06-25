import math
from js import document

def get_input_value(input_id):
    element = document.getElementById(input_id)
    if element and element.value:
        try:
            return int(element.value)
        except ValueError:
            return None
    return None

def generate_number(input_value, max_range, input_letter):
    if input_value is None or max_range is None:
        return None
    golden_ratio = (1 + math.sqrt(5)) / 2
    result = round(((input_value + 1) * golden_ratio) % max_range)
    return f"{input_letter}: {result}"

def generate_numbers(*args):
    max_range1 = get_input_value('maxRange1')
    max_range2 = get_input_value('maxRange2')
    inputs = ['A', 'B', 'C', 'D', 'E', 'F']
    results = []

    for input_letter in inputs:
        input_value = get_input_value(f'input{input_letter}')
        
        if input_value is not None:
            if input_letter != 'F':
                if max_range1 is not None:
                    result = generate_number(input_value, max_range1, input_letter)
                    if result:
                        results.append(result)
            else:
                if max_range2 is not None:
                    result = generate_number(input_value, max_range2, input_letter)
                    if result:
                        results.append(result)

    result_element = document.getElementById('result')
    if results:
        result_element.innerHTML = "<br>".join(results)
    else:
        result_element.innerHTML = "No valid inputs provided." 
