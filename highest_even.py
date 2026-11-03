# def highest_even(li):
#
#     value = 0
#     even = []
#
#     for number in li:
#         if number % 2 == 0:
#             even.append(number)
#     print(even)
#
#     for number in even:
#         if number > value:
#             value = number
#
#     print(value)
#
#
# highest_even([10,2,3,4,8,46,11, 200, 760])


def highest_even(li):
    evens = []

    for number in li:
        if number % 2 == 0:
            evens.append(number)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 46, 11, 200, 760]))
