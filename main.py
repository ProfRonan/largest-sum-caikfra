def largest_sum(numbers: list[int]) -> tuple[int, int]:
    numbers.sort()
    if len(numbers) <= 1:
        return None
    else:
       print(numbers)
       primeiro = numbers[-2]
       segundo = numbers[-1]
       return primeiro, segundo    