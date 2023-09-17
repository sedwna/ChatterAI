import app
import training
import chatbot

json_name = app.open_file()
choice = 0
while choice != '-1' and json_name != '-1':
    choice = app.menu()
    if choice == '1':
        app.show_tag(json_name)
    elif choice == '2':
        app.add_new_tag(json_name)
    elif choice == '3':
        app.add_response(json_name)
    elif choice == '4':
        app.add_pattern(json_name)
    elif choice == '5':
        app.show_pattern(json_name)
    elif choice == '6':
        app.show_response(json_name)
    # elif choice == '7':
    #     app.add_new_json_file(json_name)
    elif choice == '8':
        app.add_data_from_csv(json_name)
    elif choice == '9':
        ch = input("1 -> bag of word\n"
                   "2 -> weight\n"
                   "----> ")
        if ch == '1':
            training.trainer_bag_of_word(json_name)
        elif ch == '2':
            training.trainer_weight(json_name)

    elif choice == '10':
        ch = input("1 -> bag of word\n"
                   "2 -> weight\n"
                   "----> ")
        if ch == '1':
            chatbot.bag_chatbot_model(json_name)
        elif ch == '2':
            chatbot.weight_chatbot_model(json_name)

print("have a nice time...")

# -------------------------------------------------------------------------------
