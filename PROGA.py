from flask import Flask, request, render_template, redirect
from threading import Thread
import time
import random
app = Flask(__name__)
a = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOlQcqjYsNVMEN2sFumLWsP_oRhFYZzdML4ppi2h7RQ2ml1NEW"]
level = 1
yt = 2
number = 2
ret = 'ОШИБКА! ПОПРОБУЙ ЕЩЕ РАЗ!'
helpp = 0
reggi = 300
big = 0
ss = 0
ik = 0
peppa=["https://www.youtube.com/watch?v=i1HyxG1y7rk", "https://www.youtube.com/watch?v=e3gqIi8LER4", "https://www.youtube.com/watch?v=JQasq3MExHU", "https://www.youtube.com/watch?v=SWq8ccfYxtk", "https://www.youtube.com/watch?v=vQOb2zfqUII", "https://www.youtube.com/watch?v=_Dp3ghRgQ_o"]
sas = 9
der = 7
file = open('hugme.txt', 'r', encoding='utf-8')
hugme = int(file.read())
file.close()
helpi = reggi
file = open('new.txt', 'r', encoding='utf-8')
tyui = file.read()
file.close()
money = int(tyui)
print(money)
@app.route('/info')
def info():
    return"""
    <html>
        <head>
        <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">        
        <title>info</title>
        </head>
        <body>
        <img src="https://i.pinimg.com/originals/96/77/af/9677aff012816f817f72f1ef5c8160a0.jpg">
        <a class="btn btn-light btn-lg" style="width: 700px;height: 250px;margin-top: 15px;" role="button"><h1><p>Привет, я ОБЕЗЬЯНКА!</p>Я люблю есть яблоки!<br>Дай мне как можно больше яблок за пять минут!</h1></a>
        <p></p>
        <a class="btn btn-primary btn-lg" style="width: 250px;height: 70px;margin-top: 15px;" href="http://127.0.0.1:8088/" role="button"><h1>ВЕРНУТЬСЯ</h1></a>
        </body>
    </html>
    """
@app.route('/lose')
def lose():
    return"""
    <html>
        <head>
        <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <meta charset="UTF-8">
        <Title>lose</Title>
        </head>
        <body>
        <h1><input class="btn btn-secondary" style="width: 300px;height: 300px;" type="submit" value="К СОЖАЛЕНИЮ, ТЫ ПРОИГРАЛ!"></h1>
        <br><a class="btn btn-primary btn-lg" style="width: 250px;height: 70px;margin-top: 15px;" href="http://127.0.0.1:8088/" role="button"><h1>ВЕРНУТЬСЯ</h1></a>
        <img src="https://cdn.pixabay.com/photo/2017/01/31/16/38/face-2025364_1280.png" width = 10% heigh = 10%>
        </body>
    </html>"""
@app.route('/pencil')
def pencil():
    global money
    pagee = render_template('penc.html')
    a = request.args.get("password", "0")
    if a == "1200":
        file = open('new.txt', 'r', encoding='utf-8')
        tyui = file.read()
        file.close()
        tyui = int(tyui)
        tyui-=60
        money = tyui
        tyui = str(tyui)
        file = open('new.txt', 'w', encoding='utf-8')
        file.write(tyui)
        file.close()
        return redirect('/shop')
    return pagee
@app.route('/sweet')
def sweet():
    global money
    pagee = render_template('sweet.html')
    a = request.args.get("password", "0")
    if a == "1200":
        file = open('new.txt', 'r', encoding='utf-8')
        tyui = file.read()
        file.close()
        tyui = int(tyui)
        tyui-=30
        money = tyui
        tyui = str(tyui)
        file = open('new.txt', 'w', encoding='utf-8')
        file.write(tyui)
        file.close()
        return redirect('/shop')
    return pagee
@app.route('/multi')
def multi():
    global money, peppa
    pagee = render_template('multik.html')
    a = request.args.get("password", "0")
    if a == "1200":
        file = open('new.txt', 'r', encoding='utf-8')
        tyui = file.read()
        file.close()
        tyui = int(tyui)
        tyui-=100
        money = tyui
        tyui = str(tyui)
        file = open('new.txt', 'w', encoding='utf-8')
        file.write(tyui)
        file.close()
        return redirect(random.choice(peppa))
    elif a =="-1200":
        return redirect('/shop')
    return pagee
@app.route('/mulcomic')
def mulcomic():
    global money
    pagee = render_template('mulcomputer.html')
    a = request.args.get("password", "0")
    if a == "1200":
        file = open('new.txt', 'r', encoding='utf-8')
        tyui = file.read()
        file.close()
        tyui = int(tyui)
        tyui-=190
        money = tyui
        tyui = str(tyui)
        file = open('new.txt', 'w', encoding='utf-8')
        file.write(tyui)
        file.close()
        return redirect('/shop')
    return pagee
@app.route('/comic')
def comic():
    global money
    pagee = render_template('computer.html')
    a = request.args.get("password", "0")
    if a == "1200":
        file = open('new.txt', 'r', encoding='utf-8')
        tyui = file.read()
        file.close()
        tyui = int(tyui)
        tyui-=100
        money = tyui
        tyui = str(tyui)
        file = open('new.txt', 'w', encoding='utf-8')
        file.write(tyui)
        file.close()
        return redirect('/shop')
    return pagee
@app.route('/pnt')
def pnt():
    global money
    pagee = render_template('print.html')
    a = request.args.get("password", "0")
    if a == "1200":
        file = open('new.txt', 'r', encoding='utf-8')
        tyui = file.read()
        file.close()
        tyui = int(tyui)
        tyui-=50
        money = tyui
        tyui = str(tyui)
        file = open('new.txt', 'w', encoding='utf-8')
        file.write(tyui)
        file.close()
        return redirect('/shop')
    return pagee
@app.route('/mag')
def mag():
    page = render_template('mag.html')
    return page
@app.route('/game')
def game():
    global a, level, number, ret, helpp, reggi, big, ss, helpi, sas, ik, yt, der, money, fiv
    hello = ["БРАВО!","ТАК ДЕРЖАТЬ!","МОЛОДЕЦ!", "ОТЛИЧНО!"]
    bad = ["НЕПРАВИЛЬНО! В СЛЕДУЮЩИЙ РАЗ ПОВЕЗЕТ!", "НЕПРАВИЛЬНО! МЫ УЧИМСЯ НА ОШИБКАХ!", "НЕПРАВИЛЬНО! НИЧЕГО СТРАШНОГО!"]
    if "answer" in request.args:
        try:
            if int(request.args["answer"]) == number * helpp:
                a.append(
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOlQcqjYsNVMEN2sFumLWsP_oRhFYZzdML4ppi2h7RQ2ml1NEW")
                print(1)
                ret = random.choice(hello)
            else:
                a.pop(0)
                ret = random.choice(bad)
        except:
            ret = 'ОШИБКА! ПОПРОБУЙ ЕЩЕ РАЗ!'
        helpp = random.randint(2, 9)
    ik = 0
    fge = 0
    for ik in range(yt, sas+1):
        fge+=1
    ss = 0
    level = 1
    number = yt
    for ik in range(1, fge+1):
        if len(a) > ik*der:
            level+=1
            number += 1
    while helpi >= 60:
        helpi-=60
        ss+=1
    page = render_template('lukas.html', imp=a, tim=helpi, hor=ss)
    if helpi <= 0 and ss <= 0:
        return redirect('/lose')
    elif len(a) > fge*der:
        file = open('new.txt', 'r', encoding='utf-8')  # открываем файл new.txt для записи (w)
        tyui = file.read()  # записываем строку в файл
        file.close()
        tyui = int(tyui)
        tyui+=fiv
        money = tyui
        tyui = str(tyui)
        file = open('new.txt', 'w', encoding='utf-8')  # открываем файл new.txt для записи (w)
        file.write(tyui)  # записываем строку в файл
        file.close()
        return redirect('/win')
    else:
        return page.format(level, helpp, number, ret)
@app.route('/shop')
def shop():
    global money
    print(123456789)
    if money >= 60:
        penci = ""
    else:
        penci = "disabled "
    if money >= 30:
        swee = ""
    else:
        swee = "disabled "
    if money >= 50:
        pin = ""
    else:
        pin = "disabled "
    if money >= 100:
        com = ""
    else:
        com = "disabled "
    if money >= 100:
        we = ""
    else:
        we = "disabled "
    if money >= 190:
        mulcom = ""
    else:
        mulcom = "disabled "
    print(money)
    page = render_template('shop.html', pencil=penci, sweet=swee, pint=pin, comp=com, wer=we, mulcomp=mulcom)
    return page.format(money)
@app.route('/cht')
def cht():
    global yt, sas, der, reggi, fiv
    yt = 2
    sas = 9
    yt = int(request.args.get('qz', 2))
    if yt < 1:
        yt = 2
    sas = int(request.args.get('zq', 9))
    if sas < 1:
        sas = 9
    der = int(request.args.get('colvo', 7))
    if der < 1:
        der = 7
    reggi = int(request.args.get('time', 300))
    if reggi < 1:
        reggi = 300
    fiv = int(request.args.get('fir', 4))
    if fiv < 1:
        fiv = 4
    secsec = reggi
    horhor = 0
    while secsec >= 60:
        secsec-=60
        horhor+=1
    return"""
    <html>
        <head>
        <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <meta charset="UTF-8">
        <Title>cht</Title>
        </head>
        <body>
        <form action='/cht' method='GET'>
        <h1>От: <input type="text" value="{}" name="qz" /></h1>
        <h1>До: <input type="text" value="{}" name="zq" /></h1>
        <h1>Кол-во необходимых ответов: <input type="text" value="{}" name="colvo" /></h1>
        <h1>Кол-во монет за победу: <input type="text" value="{}" name="fir" /></h1>
        <h1>Кол-во секунд: <input type="text" value="{}" name="time" /> (Минут: {} Секунд: {})</h1>
        <h1><input class="btn btn-success" style="width: 120px;height: 70px;" type="submit" value="СОХРАНИТЬ"></h1></form>
        <br><a class="btn btn-primary btn-lg" style="width: 200px;height: 70px;margin-top: 15px;" href="http://127.0.0.1:8088/game" role="button"><h1>ИГРАТЬ</h1></a>
        </body>
    </html>
    """.format(yt, sas, der, fiv, reggi, horhor, secsec)
@app.route('/table')
def tabe():
    page = render_template('table.html')
    return page
@app.route('/shaxta')
def shaxta():
    page = render_template('shaxta.html')
    return page
@app.route('/')
def index():
    global a, level, number, ret, ss, reggi, helpi, ik, yt, sas, der
    der = 7
    yt = 1
    sas = 9
    ret = 'ОШИБКА! ПОПРОБУЙ ЕЩЕ РАЗ!'
    level = 1
    a = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOlQcqjYsNVMEN2sFumLWsP_oRhFYZzdML4ppi2h7RQ2ml1NEW"]
    number = 2
    ss = 0
    ik = 0
    reggi = 300
    helpi = reggi
    return"""
    <html>
        <head>
        <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <title>main</title>
        </head>
        <body>
        <div class="btn-group-lg" role="button" aria-label="Basic example">
        <a class="btn btn-success" type="submit" href="http://127.0.0.1:8088/"><h1>ИГРА</h1></a>
        <a class="btn btn-success" type="submit" href="http://127.0.0.1:8088/shop"><h1>МАГАЗИН</h1></a>
        <a class="btn btn-success" type="submit" href="http://127.0.0.1:8088/table"><h1>ПОМОЩЬ</h1></a>
        <a class="btn btn-success" type="submit" href="http://127.0.0.1:8088/shaxta"><h1>ШАХТА</h1></a>
        <a class="btn btn-success" type="submit" href="http://127.0.0.1:8088/mag"><h1>УРОВНИ</h1></a>
        </div>
        <p></p>
        <div class="card" style="width: 500;height: 430">
        <img src="http://purmix.ru/images/uroki/karand/priroda/kak_narisovat_dzhungli_na_bumage_karandashom.jpg" class="card-img-top">
        <div class="card-body">
        <h2 class="card-title">Это джунгли Амазонки!</h2>
        <p class="card-text"><h2>Здесь живет множество обезьянок!</h2>
        <a class="btn btn-primary btn-lg" style="width: 200px;height: 70px;margin-top: 15px;" href="http://127.0.0.1:8088/cht" role="button"><h1>ИГРАТЬ</h1></a>
        <a class="btn btn-danger btn-lg" style="margin-top: 15px;" href="http://127.0.0.1:8088/info" role="button">СПРАВКА</a>
        </div>
        </div>
        </body>
    </html>
    """
@app.route('/win')
def win(method = 'GET'):
    page = render_template('win.html')
    return page
def tme():
    global reggi, helpi
    while True:
        time.sleep(1)
        reggi-=1
        helpi = reggi
thread = Thread(target=tme)
thread.start()
app.run(debug=True, port=8088)