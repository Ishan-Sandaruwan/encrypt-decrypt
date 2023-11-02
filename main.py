import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text, shift, directionn):
    plain_text = ""
    if directionn == "decode":
        shift *= -1
    for char in text:
        if not char in alphabet:
            plain_text += char
            continue
        old_index = alphabet.index(char)
        new_index = old_index + shift
        if new_index > 25:
            new_index -= 26
        plain_text += alphabet[new_index]
    print(f"\n{directionn}d code = {plain_text}\n")

while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>25:
        shift = shift%25
    caesar(text=text,shift=shift,directionn=direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no' :")
    if again != "yes":
        print("\nGood Bye !!! \n")
        break

print("\n@copyright by Ishan Sandaruwan")