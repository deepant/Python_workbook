def max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number>max_number:
            max_number=number
    return max_number
def lb_to_kg(weight):
    return weight *0.45
def kg_to_pond(weight):
    return weight /0.45