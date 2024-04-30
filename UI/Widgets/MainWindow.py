from PySide6.QtWidgets import (QMainWindow, QSizePolicy, QHBoxLayout,
                               QToolBar, QLabel, QPushButton,
                               QSpacerItem, QWidget)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import QSize

class UserPanel(QWidget):
    def __init__(self):
        super().__init__()
        # =====================================================================#
        #                               Фронт                                  #
        # =====================================================================#
        # Элементы виджета
        # Название приложения
        app_title_label = QLabel()
        app_title_label.setText("ShipTransOpt")
        # Иконка пользователя
        user_icon = QIcon("UI/Icons/Person _Icon.svg")
        user_photo = QLabel()
        user_photo.setPixmap(user_icon.pixmap(QSize(30, 30)))
        # Никнейм пользователя
        user_name = QLabel("Ugine")
        # Бургер меню профиля
        user_menu_button = QPushButton()
        user_menu_button.setIcon(QIcon("UI/Icons/Burger_menu_Icon.svg"))
        # Spacers
        horizontalSpacer_1 = QSpacerItem(510, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        horizontalSpacer_2 = QSpacerItem(710, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        # Слой
        horizontalLayout = QHBoxLayout()
        # Добавляю элементы на горизонтальный слой
        horizontalLayout.addItem(horizontalSpacer_1)
        horizontalLayout.addWidget(app_title_label)
        horizontalLayout.addItem(horizontalSpacer_2)
        horizontalLayout.addWidget(user_photo)
        horizontalLayout.addItem(horizontalSpacer_3)
        horizontalLayout.addWidget(user_name)
        horizontalLayout.addItem(horizontalSpacer_3)
        horizontalLayout.addWidget(user_menu_button)
        horizontalLayout.addItem(horizontalSpacer_3)

        # Отображаем слой на виджете
        self.setLayout(horizontalLayout)


        # =====================================================================#
        #                               Коннекты                               #
        # =====================================================================#


        # =====================================================================#
        #                               Размеры                                #
        # =====================================================================#


        # =====================================================================#
        #                               Стили                                  #
        # =====================================================================#
        user_menu_button.setStyleSheet(
                """
                    QPushButton {
                        border: none;
                    }

                    QPushButton:pressed {
                        border: 2px dashed white;
                    }
                """
        )

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        # =====================================================================#
        #                               Фронт                                  #
        # =====================================================================#
        # Объект приложения
        self.app = app
        # Название приложения
        self.setWindowTitle("ShipTransOpt")
        
        # Menubar
        # Элементы верхнего меню
        # Основные кнопки на верхнем меню
        menu_bar = QToolBar()
        menu_bar.setMovable(False)
        self.addToolBar(menu_bar)
        save_action = menu_bar.addAction("Сохранить")
        load_action = menu_bar.addAction("Загрузить")
        help_action = menu_bar.addAction("Помощь")
        quit_action = menu_bar.addAction("Закрыть")

        # Виджет с данными пользователя
        user_widget = UserPanel()
        # Добавляем элементы в MenuBar
        menu_bar.addWidget(user_widget)
        
        # Шрифт
        font = QFont("Arial", 14)
        self.setFont(font)
        # =====================================================================#
        #                               Коннекты                               #
        # =====================================================================#
        quit_action.triggered.connect(self.quit_app)

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
                color: white;
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
    def quit_app(self):
        self.app.quit()