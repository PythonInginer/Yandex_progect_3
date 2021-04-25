import sqlite3

from flask import Flask, render_template, url_for
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    with open("static/style.css", 'r', encoding='utf-8') as f_css:
        ms_css = f_css.read()
        with open("templates/index.html", 'r', encoding='utf-8') as f_html:
            ms_html = f_html.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    with open("GV_bd.csv", 'r', encoding='utf8') as f_csv:
        ms_csv = [i for _, i in enumerate(csv.reader(f_csv, delimiter=';'))]
    ms_html = ms_html.replace('{{ headers }}', ''.join([f'<th>{i}</th>' for i in ms_csv[0]]))
    table_ms = []
    for lines in range(1, len(ms_csv)):
        line = ''.join([f'<td>{i}</td>' for i in ms_csv[lines]])
        table_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ table_osn }}', ''.join(table_ms))
    return ms_html


@app.route('/sort_1.html')
def show_sort_1():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, АРМучителя FROM базаКТ_сентябрь_2020
                        WHERE АРМучителя > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_1.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}', f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'АРМ Учителя')
    return ms_html


@app.route('/sort_2.html')
def show_sort_2():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, образование FROM базаКТ_сентябрь_2020
                            WHERE образование > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_2.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'Образование')
    return ms_html


@app.route('/sort_3.html')
def show_sort_3():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, АРМадмин FROM базаКТ_сентябрь_2020
                            WHERE АРМадмин > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_3.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'АРМ Админ')
    return ms_html


@app.route('/sort_4.html')
def show_sort_4():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, админ FROM базаКТ_сентябрь_2020
                            WHERE админ > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_4.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'Админ')
    return ms_html


@app.route('/sort_5.html')
def show_sort_5():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, до2013 FROM базаКТ_сентябрь_2020
                            WHERE до2013 > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_5.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'До 2013')
    return ms_html


@app.route('/sort_6.html')
def show_sort_6():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, tab20132017 FROM базаКТ_сентябрь_2020
                            WHERE tab20132017 > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_6.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', '20132017')
    return ms_html


@app.route('/sort_7.html')
def show_sort_7():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, tab20172018 FROM базаКТ_сентябрь_2020
                            WHERE tab20172018 > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_7.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', '20172018уч.год')
    return ms_html


@app.route('/sort_8.html')
def show_sort_8():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, tab20182019 FROM базаКТ_сентябрь_2020
                            WHERE tab20182019 > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_8.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', '20182019')
    return ms_html


@app.route('/sort_9.html')
def show_sort_9():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, tab20192020 FROM базаКТ_сентябрь_2020
                            WHERE tab20192020 > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_9.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', '20192020')
    return ms_html


@app.route('/sort_10.html')
def show_sort_10():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, tab2020 FROM базаКТ_сентябрь_2020
                            WHERE tab2020 > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_10.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', '2020')
    return ms_html


@app.route('/sort_11.html')
def show_sort_11():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, ПК FROM базаКТ_сентябрь_2020
                            WHERE ПК > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_11.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'ПК')
    return ms_html


@app.route('/sort_12.html')
def show_sort_12():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, сеть FROM базаКТ_сентябрь_2020
                            WHERE сеть > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_12.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'сеть')
    return ms_html


@app.route('/sort_13.html')
def show_sort_13():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, Ноутбук FROM базаКТ_сентябрь_2020
                            WHERE Ноутбук > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_13.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'Ноутбук')
    return ms_html


@app.route('/sort_14.html')
def show_sort_14():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, скамерой FROM базаКТ_сентябрь_2020
                            WHERE скамерой > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_14.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'скамерой')
    return ms_html


@app.route('/sort_15.html')
def show_sort_15():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, ИнтерДоска FROM базаКТ_сентябрь_2020
                            WHERE ИнтерДоска > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_15.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'Интер.доска')
    return ms_html


@app.route('/sort_16.html')
def show_sort_16():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, Мультимедиапроектор FROM базаКТ_сентябрь_2020
                            WHERE Мультимедиапроектор > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_16.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'Мультимедиапроектор')
    return ms_html


@app.route('/sort_17.html')
def show_sort_17():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, ДоскаПроекто FROM базаКТ_сентябрь_2020
                            WHERE ДоскаПроекто > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_17.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'Доска + проектор')
    return ms_html


@app.route('/sort_18.html')
def show_sort_18():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, принтер FROM базаКТ_сентябрь_2020
                            WHERE принтер > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_18.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'Принтер')
    return ms_html


@app.route('/sort_19.html')
def show_sort_19():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, Сканер FROM базаКТ_сентябрь_2020
                            WHERE Сканер > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_19.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'Сканер')
    return ms_html


@app.route('/sort_20.html')
def show_sort_20():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО, МФУ FROM базаКТ_сентябрь_2020
                            WHERE МФУ > 0""").fetchall()
    table_sort_ms = []
    with open("templates/sort_20.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace('{{ header }}',
                              f'<th>Всего</th><th>{sum([int(res[i][2]) for i in range(len(res))])}</th>')
    ms_html = ms_html.replace('{{ sorted_table }}', ''.join(table_sort_ms))
    ms_html = ms_html.replace('{{ title }}', 'МФУ')
    return ms_html


if __name__ == '__main__':
    app.run()
