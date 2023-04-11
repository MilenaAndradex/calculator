import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from display import Display



if __name__ == '__main__':
    app = QApplication (sys.argv)
    window = MainWindow()

    #ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    #display
    display = Display()
    window.addToVlao(display)

    #executa
    window.adjustFixedSize()
    window.show()
    app.exec()