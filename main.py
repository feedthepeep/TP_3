import PySimpleGUI as sg
import And
import Max
import TPK
def main():
    layout = [
        [sg.Button('Данные о разводах', key='Andrey', font='Arial 18')],
        [sg.Button('Данные о мигрантах', key='Makc', font='Arial 18')],
        [sg.Button('Данные о ценах жилья', key='Saif', font='Arial 18')]
    ]
    window = sg.Window('Главное меню', layout, size=(600, 250), finalize=True)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Andrey':
            window.hide()
            And.run()
            window.un_hide()
        elif event == 'Makc':
            window.hide()
            Max.run()
            window.un_hide()
        elif event == 'Saif':
            window.hide()
            TPK.run()
            window.un_hide()
    window.close()

if __name__ == '__main__':
    main()
