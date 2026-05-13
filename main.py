import PySimpleGUI as sg
import And
import Max
import TPK
def main():
    layout = [
        [sg.Button('Данные о разводах (Кэт)', key='-KAT-', font='Helvetica 16')],
        [sg.Button('Данные о численности населения (Поля)', key='-POLYA-', font='Helvetica 16')],
        [sg.Button('Данные о заболеваниях (Вика)', key='-VIKA-', font='Helvetica 16')]
    ]
    window = sg.Window('Главное меню', layout, size=(500, 300), finalize=True)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Andrey':
            window.hide()
            And.run()      # <-- вызываем функцию из модуля Кэт
            window.un_hide()
        elif event == 'Makc':
            sg.popup('Модуль Поли в разработке')
        elif event == 'Saif':
            sg.popup('Модуль Вики в разработке')
    window.close()

if __name__ == '__main__':
    main()