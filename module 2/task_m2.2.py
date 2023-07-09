is_active = bool(input("Is the user active?: "))
is_admin = bool(input("Is the user administrator?: "))
is_permission = bool(input("Does the user have access?: "))

access = True
if is_active == False and is_permission == False:
    access = True
elif is_admin and is_active == False and is_permission:
    access = True
else:
    access = False