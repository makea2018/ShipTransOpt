from PySide6.QtWidgets import (QMainWindow, QSizePolicy)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # =====================================================================#
        #                               Фронт                                  #
        # =====================================================================#
        # Название приложения
        self.setWindowTitle("ShipTransOpt")

        # Menubar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Файл")
        open_action = file_menu.addAction("Открыть")
        quit_action = file_menu.addAction("Закрыть")
        save_action = menu_bar.addAction("Сохранить")
        load_action = menu_bar.addAction("Загрузить")
        help_menu = menu_bar.addMenu("Помощь")


        # =====================================================================#
        #                               Коннекты                               #
        # =====================================================================#


        # =====================================================================#
        #                               Размеры                                #
        # =====================================================================#
        # MainWindow
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # MenuBar
        menu_bar.setMinimumHeight(50)
        menu_bar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # =====================================================================#
        #                               Стили                                  #
        # =====================================================================#
        self.setStyleSheet(
            """
                background-color: rgb(184, 212, 255);
            """
        )
        menu_bar.setStyleSheet(
            """
               background-color: rgb(94, 139, 255); 
            """
        )


    # =====================================================================#
    #                               Функции                                #
    # =====================================================================#