import pandas as pd
import json
import os


# -------------------------------------------------------------------------------
def open_file():
    json_name = input("enter json file name you want to work with it (enter -1 to exit)  --> ")

    while json_name != "-1":
        try:
            json_file = open(f"../json_file/{json_name}.json", 'r',
                             encoding="utf8")
            json_file.close()
            break
        except:
            print("we cant find and open this file")
            flag = input(f"do you want to craete a {json_name}.json file ?(y/n) ---> ")

        if flag == "y":
            json_name = add_new_file(json_name)
        else:
            json_name = input("enter json file name you want to work with it (enter -1 to exit)  --> ")
    return json_name


# -------------------------------------------------------------------------------
def menu():
    print("hi, welcome to AI conversation creator\n"
          "to exit enter -1\n"
          "to show your tag enter 1\n"
          "to add a new tag enter 2\n"
          "add a response for tag enter 3\n"
          "add a patterns for tag enter 4\n"
          "show pattern of tag enter 5\n"
          "show response of tag enter 6\n"
          "add a new json file enter 7\n"
          )
    choice = input("enter your choice ----> ")
    return choice


# -------------------------------------------------------------------------------
def add_new_file(json_name):
    intents = {"intents": []}
    json_file = open(f"../json_file/{json_name}.json", 'w',
                     encoding="utf8")
    with open(f"../json_file/{json_name}.json", "w",
              encoding="utf8") as outfile:
        json.dump(intents, outfile)
    json_file.close()

    input(f"add {json_name}.json file was successful, to continue press enter...")
    return json_name


def show_tag(json_name):
    json_file = open(f"../json_file/{json_name}.json", 'r',
                     encoding="utf8")
    intents = json.load(json_file)
    for intent in intents['intents']:
        print(intent["tag"])
    input("to continue press enter...")
    json_file.close()
    os.system('cls')


# -------------------------------------------------------------------------------
def add_new_tag(json_name):
    json_file = open(f"../json_file/{json_name}.json", 'r',
                     encoding="utf8")
    intents = json.load(json_file)
    json_file.close()

    tag_name = input("enter the new tag name (-1 to exit) ---> ")
    if tag_name == "-1":
        return
    intents["intents"].append({"tag": f"{tag_name}", "patterns": [], "responses": []})
    with open(f"../json_file/{json_name}.json", "w",
              encoding="utf8") as outfile:
        json.dump(intents, outfile)
    json_file.close()
    input(f"add tag {tag_name} was successful, to continue press enter...")
    os.system("cls")


# -------------------------------------------------------------------------------

def add_response(json_name):
    json_file = open(f"../json_file/{json_name}.json", 'r',
                     encoding="utf8")
    intents = json.load(json_file)
    json_file.close()

    tag_name = input("enter the tag name you want to add a new response ---> ")
    new_response = 0
    while True:
        new_response = input("enter the response you want to add (-1 to exit) ---> ")
        if new_response == "-1":
            break
        for intent in intents["intents"]:
            if intent["tag"] == f"{tag_name}":
                intent["responses"].append(f"{new_response}")
        input(f"add response to tag {tag_name} was successful, to continue press enter...")
    with open(f"../json_file/{json_name}.json", "w",
              encoding="utf8") as outfile:
        json.dump(intents, outfile)
    json_file.close()

    os.system("cls")


# -------------------------------------------------------------------------------

def add_pattern(json_name):
    json_file = open(f"../json_file/{json_name}.json", 'r',
                     encoding="utf8")
    intents = json.load(json_file)
    json_file.close()
    tag_name = input("enter the tag name you want to add a new pattern ---> ")
    new_pattern = 0
    while True:
        new_pattern = input("enter the pattern you want to add (-1 to exit) ---> ")
        if new_pattern == "-1":
            break
        for intent in intents["intents"]:
            if intent["tag"] == f"{tag_name}":
                intent["patterns"].append(f"{new_pattern}")
        input(f"add pattern to tag {tag_name} was successful, to continue press enter...")

    with open(f"../json_file/{json_name}.json", "w",
              encoding="utf8") as outfile:
        json.dump(intents, outfile)
    json_file.close()

    os.system("cls")


# -------------------------------------------------------------------------------
def show_pattern(json_name):
    json_file = open(f"../json_file/{json_name}.json", 'r',
                     encoding="utf8")
    intents = json.load(json_file)
    json_file.close()
    tag_name = input("enter the tag name you want to show pattern ---> ")
    for intent in intents["intents"]:
        if intent["tag"] == tag_name:
            print(intent["patterns"])
    input("to continue press enter...")
    os.system('cls')


# -------------------------------------------------------------------------------
def show_response(json_name):
    json_file = open(f"../json_file/{json_name}.json", 'r',
                     encoding="utf8")
    intents = json.load(json_file)
    json_file.close()
    tag_name = input("enter the tag name you want to show response ---> ")
    for intent in intents["intents"]:
        if intent["tag"] == tag_name:
            print(intent["responses"])
    input("to continue press enter...")
    os.system('cls')

# -------------------------------------main--------------------------------------


# df = pd.read_csv("data.csv")
# df.head()
# json_file = open("info.json", 'r', encoding="utf8")
# intents = json.load(json_file)
# txt_file = open("counter.txt", "r")
# counter = txt_file.read()
# counter = int(counter)
# print(counter)
#
# label = 0
#
# while label != "-1":
#     print('user: ', df["user"][counter])
#     print('operator: ', df["operator"][counter])
#     for intent in intents['intents']:
#         print(intent["tag"])
#     print("اسپم")
#     label = input("enter -1 to exit, tag?")
#
#     if label == "اسپم":
#         counter += 1
#         continue
#     for intent in intents['intents']:
#         if intent["tag"] == label:
#             intent["patterns"].append(df["user"][counter])
#
#     if label != "-1":
#         counter += 1
#
# txt_file.close()
# json_file.close()
#
# txt_file = open("counter.txt", "w")
# txt_file.write(str(counter))
#
# with open("info.json", "w", encoding="utf8") as outfile:
#     json.dump(intents, outfile)
#
# print(intents)
