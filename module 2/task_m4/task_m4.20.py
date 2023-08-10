my_list = [1, 1, 45, 57, 568, None, 235, 213, -346, -10, None,  -45, 0, 100, 57]
print(my_list)
res = None
try:
    # res = my_list.index(None)
    for _ in range(len(my_list)):
        if None not in my_list:
            break
        # res = my_list.index(None)
        my_list.pop(my_list.index(None))
except ValueError:
    print("No value in list")
finally:
    print(my_list)