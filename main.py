number_first_team = 20
number_second_team = 15
print("В команде \"Мастера кода\" всего %d участников."%number_first_team,
      "В команде \"Волшебники данных\" всего %d участников."%number_second_team,
      "Итого сегодня в схватке сойдутся %d человек!\n"%(number_first_team+number_second_team),
      sep="\n")

score_1 = 30
score_2 = 34
time_1 = 30
time_2 = 20
print("Первая команда решила {} задач, а вторая - {};".format(score_1, score_2))

print(f"Первая команда управилась за {time_1} минут, а вторая за {time_2};\n")
if score_1==score_2:
    print(f"Победила дружба! Обеими командами было решено по {score_1} задач!\n"
          f"Скорость первой команды: {score_1/time_1}\n"
          f"Скорость второй команды: {score_2/time_2}\n")
elif score_1>score_2:
    print(f"Победили \"Мастера кода\"!\n"
          f"Они решили {score_1} задач за {time_1}, таким образом их скорость : {score_1/time_1}")
else:
    print(f"Победили \"Волшебники данных\"!\n"
          f"Они решили {score_2} задач за {time_2}, таким образом их скорость : {score_2 / time_2}")