from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QLabel, QSizePolicy,
                               QVBoxLayout, QWidget,
                               QPushButton, QSpacerItem)

class Right_Panel(QWidget):
    def __init__(self):
        super().__init__()
        # =====================================================================#
        #                               Фронт                                  #
        # =====================================================================#
        # Кнопка 'Определить'
        predict_button = QPushButton()
        predict_button.setText("Определить")
        # Spacer
        verticalSpacer = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Maximum)
        # Строка с выводом результата предсказания нейросети
        self.result_text_label = QLabel()
        self.result_text_label.setText("Оптимальная стоимость транспортировки груза - ")
        self.result_text_label.setAlignment(Qt.AlignCenter)

        # Вертикальный слой
        verticalLayout = QVBoxLayout()
        # Добавляем элементы параметров в вертикальный слой
        verticalLayout.addWidget(predict_button)
        verticalLayout.addItem(verticalSpacer)
        verticalLayout.addWidget(self.result_text_label)

        # Отображаем слой на виджете
        self.setLayout(verticalLayout)

        # Шрифт
        font1 = QFont("Arial", 16)
        font2 = QFont("Arial", 24)
        # Применяем шрифт к объектам
        predict_button.setFont(font1)
        self.result_text_label.setFont(font2)

        # =====================================================================#
        #                               Коннекты                               #
        # =====================================================================#
        predict_button.clicked.connect(self.predict_cost)

        # =====================================================================#
        #                               Размеры                                #
        # =====================================================================#
        # Размер виджета
        self.setMaximumSize(QSize(1250, 222))
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # Размер кнопки
        predict_button.setMaximumSize(QSize(200, 70))
        predict_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # Размер сообщения результата
        self.result_text_label.setMaximumSize(QSize(1250, 106))
        self.result_text_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # =====================================================================#
        #                               Стили                                  #
        # =====================================================================#
        self.setStyleSheet(
            """
                QPushButton {
                    background-color: rgb(94, 139, 255);
                    border: 2px solid white;
                    border-radius: 30px;
                    border-color: white;
                    color: white;
                }

                QPushButton:pressed {
                    border: 2px solid red;
                }

                QLabel {
                    background-color: rgb(94, 139, 255);
                    border: 2px solid white;
                    color: white;
                }
            """
        )


    # =====================================================================#
    #                               Функции                                #
    # =====================================================================#
    def predict_cost(self):
        init_text = self.result_text_label.text()
        if init_text.endswith("- "):
            # Вычисление стоимости транспортировки груза
            cost = 1000
            # Запись стоимости в QLabel
            self.result_text_label.setText(init_text + str(cost))