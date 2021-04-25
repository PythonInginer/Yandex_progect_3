def show_sort_1():
    bd = sqlite3.connect('BDGK.db')
    cur = bd.cursor()
    res = cur.execute("""SELECT кабинет, ФИО FROM базаКТ_сентябрь_2020
                        WHERE АРМучителя = 1""").fetchall()
    table_sort_ms = []
    with open("templates/sort_1.html", 'r', encoding='utf-8') as f_html:
        ms_html = f_html.read()
        print(ms_html)
        with open("static/sort_style.css", 'r', encoding='utf-8') as f_css:
            ms_css = f_css.read()
            ms_html = ms_html.replace('{{ table_style }}', ms_css)
    for lines in range(len(res)):
        line = ''.join([f'<td>{i}</td>' for i in res[lines]])
        table_sort_ms.append(f'<tr>{line}</tr>')
    ms_html = ms_html.replace(' {{ sorted_table }} ', ''.join(table_sort_ms))
    ms_html = ms_html.replace(' {{ title }} ', 'АРМ Учителя')
    return ms_html