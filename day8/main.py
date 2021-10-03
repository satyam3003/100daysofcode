# -----------------------passing parameters through functions --------------------

# --------------no parameter function -----------
# def greet():
#     print("Hello!")
#
# greet()


# ----------- one parameter function -------------
# def greet(name):
#     print(f"Hello {name}!")
#
#
# greet("Satyam")


# ------------ two parameter function -----------
# def greet(name,location):
#     print(f"Hello {name} from {location}")
#
#
# greet("Satyam","Pune")
# greet(location='Pune',name='Satyam')


# -------------- No of paint can solution ---------------
# import math
# def paint_calc(height,width,cover):
#     area = height * width
#     total_cans = area / coverage
#     print(f"You will need {math.ceil(total_cans)} cans of paint")
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# ---------------- Prime no -------------
# def prime_checker(number):
#     if number == 1:
#         print("Its neither prime nor composite")
#     else:
#         prime = True
#         for num in range(2, number):
#             if number % num == 0:
#                 prime = False
#
#         if prime:
#             print("It is a prime no")
#         else:
#             print("Its is a composite no")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)


# -------------------caesar-cipher------------------
import math
import ascii_art as aa

print(aa.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text_given, shift_given, encode_decode):
    if encode_decode == 'decode':
        shift_given = -shift_given
    encode = ''
    for n in text_given:
        if alphabet.count(n) == 0:
            encode += n
        else:
            for alphabets in alphabet:
                i = alphabet.index(alphabets)
                if n == alphabets:
                    if i+shift_given < len(alphabet):
                        circulation = i + shift_given
                    else:
                        multip = math.floor(shift // len(alphabet))
                        circulation = i + shift_given - len(alphabet) * multip

                    encode += alphabet[circulation]
    print(f"{encode_decode} result is : {encode} \n")


continue_status = True
while continue_status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift, direction)

    a = input("Would you like to continue: Y or N:\n")
    if a == 'N':
        continue_status = False
        print("Bye Bye..")

