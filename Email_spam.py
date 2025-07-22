import smtplib
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path("env.env"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

head = """From: %sender%
To: %recipient%
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
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

sender = EMAIL_USER
recipient = "avc@bk.ru"
friend_name = "Владимир"
my_name = "Devman"
url = "https://dvmn.org/referrals/O4w62S83RdL7taQOLhpAbfnnOJtFhQndmLAxHndr/"

def head_replace(sender, recipient):
    head_replaced = head
    head_replaced = head_replaced.replace("%sender%", str(sender))
    head_replaced = head_replaced.replace("%recipient%", str(recipient))
    return head_replaced

def email_text_replace(friend_name, my_name, url):
    text_replaced = email_text
    text_replaced = text_replaced.replace("%friend_name%", friend_name)
    text_replaced = text_replaced.replace("%my_name%", my_name)
    text_replaced = text_replaced.replace("%website%", url)
    return text_replaced

message = f"{head_replace(sender, recipient)}\n{email_text_replace(friend_name, my_name, url)}"

login = EMAIL_USER
password = EMAIL_PASS

email_from = sender
email_to = recipient

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(login, password)
server.sendmail(email_from, email_to, message.encode('utf-8'))
server.quit()
