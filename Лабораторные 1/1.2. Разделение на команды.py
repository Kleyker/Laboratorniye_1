list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

amount = len(list_players)# TODO Разделите участников на две команды
mid = amount // 2
first_team = list_players[:mid]
second_team = list_players[mid:]

print(first_team)
print(second_team)