print('привет это простой чат с двумя ползователями БЕЗ БОТОВ')
print('Есть 2 ползователя 1 и 2 или чтобы выйти exit')
user1 = 'user1'
user2 = 'uer2'

history = []
while True:
    choice = input('Выберите ползователя:\t')
    if choice == 'exit':
        break
    if choice == '1':
        author = user1
        print('Вы выбрали ползователя 1')
    elif choice == '2':
        author = user2
        print('Вы выбрали ползователя 2')
    else:
        print('Не понимаю. Введите: 1 или 2 ')
        continue

    text = input('Введите текст:\t')
    messages = f'[{author}]: {text}'
    history.append(messages)

    print('\n --- ЧАТ ---')
    for msg in history:
        print(msg)
    print('-----------\n')