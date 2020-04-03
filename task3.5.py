def s_sum():
    ex = False
    sum_res = 0

    while ex == False:
        nums = input('Ввести числа или нажать E для выхода').split()
        res = 0
        for elem in range(len(nums)):
            if nums[elem] == 'e' or nums[elem] == 'E':
                ex = True
                break
            else:
                res = res + int(nums[elem])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')

    print(f'Сумма всех чисел: {sum_res}')

s_sum()