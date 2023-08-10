message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    print(ord(ch))
    if 65 <= ord(ch) and ord(ch) <= 90:
        pos = ord(ch) - ord('A')
        pos = (pos + offset) % 26
        encoded_message += chr(pos + ord("A"))
    elif 97 <= ord(ch) and ord(ch) <= 127:
        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26
        encoded_message += chr(pos + ord("a"))
    elif ch == ' ':
        encoded_message += ' '
    else:
        encoded_message += ch

print(encoded_message, ch, sep='')