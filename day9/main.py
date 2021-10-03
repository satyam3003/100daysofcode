# # -------------- creating a dictionary -----------
# my_dictionary = {
#     "name": "satyam",
#     "age": "20",
#     "Education": "Undergraduate",
#     "College": "WCE, Sangli"
# }
#
# # printing the dictionary
# print(my_dictionary)
#
# # retrieving from dictionary
# print(my_dictionary["name"])
#
# # adding to dictionary
# my_dictionary['Interest'] = "Coding"
#
# # accessing all keys from loop
# for key in my_dictionary:
#     print(key)
#
# # accessing the value of key
# for key in my_dictionary:
#     print(my_dictionary[key])


# -------------converting scores to grades --------------
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
#
# for key in student_scores:
#     score = student_scores[key]
#     if score > 90:
#         grade = "Outstanding"
#     elif score > 80:
#         grade = "Exceeds Expectations"
#     elif score > 70:
#         grade = "Acceptable"
#     else:
#         grade = "Fail"
#
#     student_grades[key] = grade
#
# print(student_grades)


# ---------travel_log creater -------------
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
#
# def add_new_country(country, visits, cities):
#     log = {
#         "country": country,
#         "visits": visits,
#         "cities": cities,
#     }
#     travel_log.append(log)
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# -----------secret auction --------------
import ascii_art

print(ascii_art.logo)
secret_bid_dictionary = {}


def secret_bid_dict(secret_name, secret_bid):
    secret_bid_dictionary[secret_name] = secret_bid

def clear():
    print("\n"*100)

last = False
while not last:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    more_bidders = input("Are there more bidders? y or n: ")
    if more_bidders == 'n':
        last = True
    secret_bid_dict(name, bid)
    clear()

i = 0
highest_bidder = ''
for key in secret_bid_dictionary:
    bid_val = secret_bid_dictionary[key]
    if bid_val > i:
        i = bid_val
        highest_bidder = key

print(f"Highest bidder is {highest_bidder} with price {i}")
