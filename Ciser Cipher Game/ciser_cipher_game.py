"""Caesar Cipher Encryption & Decryption CLI Application.

Encodes and decodes secret messages by shifting alphabetic characters along the alphabet
array, preserving spaces, numbers, and special symbols intact.
"""

from typing import List

LOGO = r"""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

ALPHABET: List[str] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(original_text: str, shift_amount: int, encode_or_decode: str) -> str:
    """Encode or decode text by shifting alphabetic characters.

    Args:
        original_text: The message string to transform.
        shift_amount: Number of positions to shift.
        encode_or_decode: Directional mode ('encode' or 'decode').

    Returns:
        The resulting transformed string.
    """
    output_text = ""
    effective_shift = shift_amount % len(ALPHABET)
    if encode_or_decode.lower() == "decode":
        effective_shift *= -1

    for letter in original_text:
        lower_char = letter.lower()
        if lower_char in ALPHABET:
            shifted_position = (ALPHABET.index(lower_char) + effective_shift) % len(ALPHABET)
            new_char = ALPHABET[shifted_position]
            output_text += new_char.upper() if letter.isupper() else new_char
        else:
            output_text += letter

    return output_text


def main() -> None:
    """Execute Caesar Cipher interactive loop."""
    print(LOGO)
    should_continue = True

    while should_continue:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
        if direction not in ['encode', 'decode']:
            print("Invalid direction specified! Please enter 'encode' or 'decode'.")
            continue

        text = input("Type your message:\n")

        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Shift amount must be an integer.")
            continue

        result = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        print(f"\nHere is the {direction}d result: {result}")

        play_again = input("\nDo you want to run another cipher? Type 'yes' or 'no': ").strip().lower()
        if play_again == "no":
            should_continue = False
            print("Goodbye!")


if __name__ == "__main__":
    main()
