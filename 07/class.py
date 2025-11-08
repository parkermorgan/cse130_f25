# def search(array, search):
#     i_begin = 0
#     i_end = len(array) - 1
#     while i_begin <= i_end:
#         i_middle = (i_begin + i_end) // 2

#         if array[i_middle] == search:
#             return True
        
#         if search > array[i_middle]:
#             i_begin = i_middle + 1
#         else:
#             i_end = i_middle - 1
#     return False

# if __name__ == "__main__":
#     print(search([2, 4, 6], 2))
#     print(search([2, 4, 6], 3))
#     print(search([2, 4, 6, 8, 10, 12, 14], 10))
#     print(search([2, 4, 6, 8, 10, 12, 14], 5))


