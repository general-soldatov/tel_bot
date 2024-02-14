def turn_surprize(number, sep=5):
    """функция для переворота числа до определённого значения
    """
    raz = len(number)
    chis = int(number)
    result = 0
    for i in range(1, sep+1):
        result += chis % 10 * 10**(sep-i)
        chis //= 10
    result += chis * 100000
    return result

print(turn_surprize(input('Enter number: ')))