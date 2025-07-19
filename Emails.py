import smtplib

head = """
From: %sender%
To: %recipient%
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8;"
"""

email_text = r"""Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!
 
%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 
 
Как будет проходить ваше обучение на %website%? 
 
→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 
 
Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

login = ""
password = ""

sender = ""
recipient = ""
friend_name = "Ilya"
my_name = "Devman"
url = "https://dvmn.org/referrals/O4w62S83RdL7taQOLhpAbfnnOJtFhQndmLAxHndr/"

def head_replace(sender, recipient):
    result = head
    result = result.replace("%sender%", sender)
    result = result.replace("%recipient%", recipient)
    return result

def email_text_replace(friend_name, my_name, url):
    result = email_text
    result = result.replace("%friend_name%", friend_name)
    result = result.replace("%my_name%", my_name)
    result = result.replace("%website%", url)
    return result

message = f"{head_replace(sender, recipient)}\n{email_text_replace(friend_name, my_name, url)}"

email_from = sender
email_to = recipient

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()




