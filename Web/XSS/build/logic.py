from flask import current_app, request, render_template, render_template_string
from random import randint
from re import findall
from jobs import admin
from urllib.parse import urlparse

def validator(link):
    result = urlparse(link)
    print(result)
    if not result.netloc:
        return "not url"
    if result.netloc != current_app.config.get('CURRENT_URL'):
        return "not valid"

def admin():
    if "is_admin" in request.cookies:
        if request.cookies.get('is_admin') == '6e55c909e31e8f09efa5b4c684634612':
            return render_template_string("yetiCTF{very_bad_admin}")
        return render_template_string("А не хакерок ли ты часом?")
    return render_template_string("Ты точно не админ!")

def index():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            return render_template('index.html', 
                                        message = "Пустое поле.")
        if "document" in text:
            return render_template('index.html', 
                                        message = "А не хакерок ли ты часом?")
        length = len(text)
        longest = len(max(findall(r'\S+',text), key = len))
        message = f"Ваш текст: {text}; Длина: {length}; Самое длинное слово {longest}"
        filename = randint(100000,10000000)
        open(f"files/{filename}.txt", 'w').write(message)
        file_link = f"http://{current_app.config.get('CURRENT_URL')}/files/{filename}.txt"
        return render_template('index.html', 
                                        message = message, link=file_link)
    return render_template('index.html')

def download(filename):
    return render_template_string(open(f"files/{filename}").read())

def report():
    if request.method == "POST":
        link = request.form.get("link")
        if validator(link) == "not url":
            return render_template("report.html", message="Пожалуйста, отправьте ссылку на проблемный файл")
        if validator(link) == "not valid":
            return render_template("report.html", message="А не хакерок ли ты часом? Найдена ссылка ведущая на другой ресурс")
        admin.queue(link)
        return render_template("report.html", message="Админ уже бежит проверять твой файл...")
    return render_template("report.html")