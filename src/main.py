import app
import training
import chatbot
import os

json_name = app.open_file()
choice = 0
while choice != '-1' and json_name != '-1':
    os.system("cls")
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
        training.trainer(json_name)
    elif choice == '10':
        chatbot.chatbot_model(json_name)

print("have a nice time...")

# -------------------------------------------------------------------------------
