import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from display import Display
from info import Info
from style import setupTheme
from buttons import ButtonsGrid



if __name__ == '__main__':
     
    app = QApplication (sys.argv)
    setupTheme()
    window = MainWindow()

    #ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    #info
    info = Info('sua conta')
    window.addWidgetToVLayout(info)

    #display
    display = Display()
    window.addWidgetToVLayout(display)

    #gride
    buttonsGride = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGride)
    
   

    #executa
    window.adjustFixedSize()
    window.show()
    app.exec()