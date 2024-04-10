from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QComboBox, QLineEdit,
                               QVBoxLayout, QWidget,
                               QSizePolicy)

class Left_Panel(QWidget):
    def __init__(self):
        super().__init__()
        # =====================================================================#
        #                               Фронт                                  #
        # =====================================================================#
        # Параметры модели
        # Название судна
        vessel_title = QLineEdit()
        vessel_title.setPlaceholderText("Название судна")
        # Тип судна
        vessel_type = QComboBox()
        vessel_type.setPlaceholderText("Тип судна")
        vessel_type.addItem("сухогруз")
        vessel_type.addItem("танкер")
        # Длина судна
        L = QLineEdit()
        L.setPlaceholderText("Длина судна, м")
        # Ширина судна
        B = QLineEdit()
        B.setPlaceholderText("Ширина судна, м")
        # Осадка судна
        d = QLineEdit()
        d.setPlaceholderText("Осадка судна, м")
        # Дедвейт
        DW = QLineEdit()
        DW.setPlaceholderText("Дедвейт, т")
        # Скорость судна
        speed = QLineEdit()
        speed.setPlaceholderText("Скорость судна, узел")
        # Количество перевозимого груза
        cargo_amount = QLineEdit()
        cargo_amount.setPlaceholderText("Количество перевозимого груза, т")
        # Цена 1т груза за 1 милю
        cost_per_mile = QLineEdit()
        cost_per_mile.setPlaceholderText("Цена 1т груза за 1 милю")
        # Спрос на товар
        cargo_demand = QComboBox()
        cargo_demand.setPlaceholderText("Спрос на товар")
        cargo_demand.addItem("маленький")
        cargo_demand.addItem("большой")
        # Ценность груза
        cargo_value = QComboBox()
        cargo_value.setPlaceholderText("Ценность груза")
        cargo_value.addItem("обычный")
        cargo_value.addItem("ценный")
        cargo_value.addItem("очень ценный")
        # Хрупкость груза
        cargo_fragility = QComboBox()
        cargo_fragility.setPlaceholderText("Хрупкость груза")
        cargo_fragility.addItem("не хрупкий")
        cargo_fragility.addItem("хрупкий")
        # Класс опасности груза
        cargo_danger = QComboBox()
        cargo_danger.setPlaceholderText("Класс опасности груза")
        cargo_danger.addItem("не опасный")
        cargo_danger.addItem("опасный")
        # Протяженность морского пути
        sea_route = QLineEdit()
        sea_route.setPlaceholderText("Протяженность морского пути, миль")
        # Сила ветра
        wind_strength = QLineEdit()
        wind_strength.setPlaceholderText("Сила ветра, балл")
        # Сила волнения
        sea_state = QLineEdit()
        sea_state.setPlaceholderText("Сила волнения, балл")

        # Слои
        verticalLayout = QVBoxLayout()
        # Добавляем элементы параметров в вертикальный слой
        verticalLayout.addWidget(vessel_title)
        verticalLayout.addWidget(vessel_type)
        verticalLayout.addWidget(L)
        verticalLayout.addWidget(B)
        verticalLayout.addWidget(d)
        verticalLayout.addWidget(DW)
        verticalLayout.addWidget(speed)
        verticalLayout.addWidget(cargo_amount)
        verticalLayout.addWidget(cost_per_mile)
        verticalLayout.addWidget(cargo_demand)
        verticalLayout.addWidget(cargo_value)
        verticalLayout.addWidget(cargo_fragility)
        verticalLayout.addWidget(cargo_danger)
        verticalLayout.addWidget(sea_route)
        verticalLayout.addWidget(wind_strength)
        verticalLayout.addWidget(sea_state)

        # Отображаем слой на виджете
        self.setLayout(verticalLayout)

        # Шрифт
        font = QFont("Arial", 16)
        # Применяем шрифт к объектам
        vessel_title.setFont(font)
        vessel_type.setFont(font)
        L.setFont(font)
        B.setFont(font)
        d.setFont(font)
        DW.setFont(font)
        speed.setFont(font)
        cargo_amount.setFont(font)
        cost_per_mile.setFont(font)
        cargo_demand.setFont(font)
        cargo_value.setFont(font)
        cargo_fragility.setFont(font)
        cargo_danger.setFont(font)
        sea_route.setFont(font)
        wind_strength.setFont(font)
        sea_state.setFont(font)


        # =====================================================================#
        #                               Коннекты                               #
        # =====================================================================#


        # =====================================================================#
        #                               Размеры                                #
        # =====================================================================#
        # Размеры виджета
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setMaximumWidth(400)
        vessel_title.setMaximumSize(QSize(400, 40))
        vessel_type.setMaximumSize(QSize(400, 40))
        L.setMaximumSize(QSize(400, 40))
        B.setMaximumSize(QSize(400, 40))
        d.setMaximumSize(QSize(400, 40))
        DW.setMaximumSize(QSize(400, 40))
        speed.setMaximumSize(QSize(400, 40))
        cargo_amount.setMaximumSize(QSize(400, 40))
        cost_per_mile.setMaximumSize(QSize(400, 40))
        cargo_demand.setMaximumSize(QSize(400, 40))
        cargo_value.setMaximumSize(QSize(400, 40))
        cargo_fragility.setMaximumSize(QSize(400, 40))
        cargo_danger.setMaximumSize(QSize(400, 40))
        sea_route.setMaximumSize(QSize(400, 40))
        wind_strength.setMaximumSize(QSize(400, 40))
        sea_state.setMaximumSize(QSize(400, 40))


        # =====================================================================#
        #                               Стили                                  #
        # =====================================================================#
        # QLineEdit
        self.setStyleSheet(
            """
                QLineEdit {
                    background-color: rgb(94, 139, 255);
                    border: 2px solid white;
                    border-radius: 15px;
                    color: white;
                }
                
                QComboBox {
                    background-color: rgb(94, 139, 255);
                    border: 2px solid white;
                    border-radius: 15px;
                    color: white;
                }

                QComboBox::down-arrow {
                    image: url(UI/Icons/arrow-down.svg);
                    width: 15px;
                    height: 15px;
                    margin-right: 15px;
                }

                QComboBox::drop-down {
                    border-width: 0px;
                }
            """
        )


    # =====================================================================#
    #                               Функции                                #
    # =====================================================================#