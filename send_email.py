import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # "EMAIL" は環境変数です。送信に使いたいメールアドレスを入力してください。
    username = "EMAIL"

    # "PASSWORD" は環境変数です。アプリパスワードを作成して入力してください。
    password = "PASSWORD"

    # "EMAIL" は環境変数です。受信に使いたいメールアドレスを入力してください。
    receiver = "EMAIL"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

