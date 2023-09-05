import app

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



# -------------------------------------------------------------------------------
