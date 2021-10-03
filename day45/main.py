from bs4 import BeautifulSoup

# with open("day45/website.html", encoding="utf8", mode="r") as website:
#     soup = BeautifulSoup(website.read(), 'html.parser')
#
# # ------------------ finding h1 -------------------
# print(soup.h1)
#
# # ------------ finding actual content of h1 -----------------
# print(soup.h1.string)
#
# # ---------------- finding all list items -----------------
# all_list_items = soup.find_all(name="li")
# print(all_list_items)
#
# # --------------- finding actual content in list item -----------------
# for item in all_list_items:
#     print(item.get_text())
#
# # ---------------- getting the content in href -------------
# print(soup.a.get("href"))  # give only for first a tag
#
# all_a_tags = soup.find_all(name="a")
# for item in all_a_tags:
#     print(item.get("href"))
#
# # -------------- finding element by id and tag ----------------
# header = soup.find(name="h1", id="name")
# print(header)
#
# # ------------finding element by class and tag ---------------
# section_class = soup.find(name="h3", class_="heading")
# print(section_class)
#
# # --------------- select one ----------------------
# name = soup.select_one(selector="#name")
# print(name)
#
# # -------------- select all ------------------
# heading = soup.select(".heading")
# print(heading)


# ------------------------- parsing a live website ------------------
import requests

# require = requests.get(url="https://news.ycombinator.com/")
# soup = BeautifulSoup(require.text, "html.parser")
# # print(soup)
#
# all_items = soup.select("td")
# full_list = []
# for item in all_items:
#     a = item.select(".score")
#     if len(a) > 1:
#         full_list = a
#
# my_dict = {}
# for item in full_list:
#     dict_id = item.attrs['id'].split("_")[1]
#     dict_score = int(item.string.split(" ")[0])
#     my_dict[dict_id] = dict_score
#
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# # print(sorted_dict)
#
# rank = 0
# for item in sorted_dict:
#     rank+=1
#     # print(item[0])
#     tr_item = soup.find(name="tr", id=item[0])
#     text = tr_item.find_all(name="td")[2]
#     print(f"score: {item[1]}, Rank:{rank}, Movie:{text.find(name='a').string}")


# ---------------- top 100 movies of all time ------------------------
response = requests.get(url="https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

listicle_item = soup.find_all("h3", {"class": "lister-item-header"})
rank = 0
full_string = ""
for item in listicle_item:
    rank += 1
    a = item.find("a").getText()
    full_string += f"{rank}. {str(a)}\n"

print(full_string)
with open("day45/Top_50_movies.txt", mode="w",encoding="UTF-16") as file:
    file.write(full_string)
