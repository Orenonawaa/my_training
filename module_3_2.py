def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" not in recipient or not ((recipient.endswith(".com") and sender.endswith(".com")) or (recipient.endswith(".ru") and sender.endswith(".ru")) or (recipient.endswith(".net") and sender.endswith(".net"))):
        print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender:
        print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
