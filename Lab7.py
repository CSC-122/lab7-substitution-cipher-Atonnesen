# CSC 122
# Substitution Cipher
# By <Ashley Tonnesen>

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
# prompt user to enter short message to be encrypted with sub cypher
# python functions ordinal value = ord
# python functions character = chr
# prompt user to enter encrypted message to be decrypted

def main():
    # cipher is your empty list
    cipher = []
    message = input("Enter the message to be encrypted: ")
    for letter in message:
        # convert it to ordinal value and add 3 then apend to cypher list
        cipher.append(chr(ord(letter) + 3))
    # combine everything into one list
    print(f"Encrypted message = {''.join(cipher)}\n")

    # plaintext is empty list
    plaintext = []
    message = input("Enter the cipher to be decrypted: ")
    for letter in message:
        # convert it to ordinal value and subtract 3 then apend to plaintext list
        plaintext.append(chr(ord(letter) - 3))
    # combine everything into one list
    print(f"Decrypted message = {''.join(plaintext)}\n")


if __name__ == '__main__':
    main()
