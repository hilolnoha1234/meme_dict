meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ROFL":"joke",
            "AFK":"away from keyboard",
            "WYD":"What are you doing",
            "TEAMATE":"someone on your team"
            }
while True:
    command = input("enter your command (dict, add, remove)")
    if command == "dict":
        word = input("Введите непонятное слово (большими буквами!): ")
        if word in meme_dict.keys():
            # Что делать, если слово нашлось?
            print (meme_dict[word])
        else:
            print('This word does not exist')
            # Что делать, если слово не нашлось?
    elif command == "add":
        k = input()
        v = input()
        meme_dict[k]=v
    elif command == 'remove':
        k = input()
        del meme_dict[k]
    else:
        print("invalid syntaxix")
