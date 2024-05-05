from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QIntValidator, QDoubleValidator, QRegularExpressionValidator
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
        self.vessel_title = QLineEdit()
        self.vessel_title.setPlaceholderText("Название судна")
        # Тип судна
        self.vessel_type = QComboBox()
        self.vessel_type.setPlaceholderText("Тип судна")
        self.vessel_type.addItem("сухогруз")
        self.vessel_type.addItem("танкер")
        # Длина судна
        self.L = QLineEdit()
        self.L.setPlaceholderText("Длина судна, м (не более 600)")
        # Ширина судна
        self.B = QLineEdit()
        self.B.setPlaceholderText("Ширина судна, м (не более 70)")
        # Осадка судна
        self.d = QLineEdit()
        self.d.setPlaceholderText("Осадка судна, м (не более 30)")
        # Дедвейт
        self.DW = QLineEdit()
        self.DW.setPlaceholderText("Дедвейт, т (не более 550000)")
        # Скорость судна
        self.speed = QLineEdit()
        self.speed.setPlaceholderText("Скорость судна, узел (не более 40)")
        # Количество перевозимого груза
        self.cargo_amount = QLineEdit()
        self.cargo_amount.setPlaceholderText("Количество перевозимого груза, т (не более 550000)")
        # Цена 1т груза за 1 милю
        self.cost_per_mile = QLineEdit()
        self.cost_per_mile.setPlaceholderText("Цена 1т груза за 1 милю (не более 50000)")
        # Спрос на товар
        self.cargo_demand = QComboBox()
        self.cargo_demand.setPlaceholderText("Спрос на товар")
        self.cargo_demand.addItem("маленький")
        self.cargo_demand.addItem("большой")
        # Ценность груза
        self.cargo_value = QComboBox()
        self.cargo_value.setPlaceholderText("Ценность груза")
        self.cargo_value.addItem("обычный")
        self.cargo_value.addItem("ценный")
        self.cargo_value.addItem("очень ценный")
        # Хрупкость груза
        self.cargo_fragility = QComboBox()
        self.cargo_fragility.setPlaceholderText("Хрупкость груза")
        self.cargo_fragility.addItem("не хрупкий")
        self.cargo_fragility.addItem("хрупкий")
        # Класс опасности груза
        self.cargo_danger = QComboBox()
        self.cargo_danger.setPlaceholderText("Класс опасности груза")
        self.cargo_danger.addItem("не опасный")
        self.cargo_danger.addItem("опасный")
        # Протяженность морского пути
        self.sea_route = QLineEdit()
        self.sea_route.setPlaceholderText("Протяженность морского пути, миль (не более 20000)")
        # Сила ветра
        self.wind_strength = QLineEdit()
        self.wind_strength.setPlaceholderText("Сила ветра, балл (не более 9)")
        # Сила волнения
        self.sea_state = QLineEdit()
        self.sea_state.setPlaceholderText("Сила волнения, балл (не более 7)")

        # Слои
        verticalLayout = QVBoxLayout()
        # Добавляем элементы параметров в вертикальный слой
        verticalLayout.addWidget(self.vessel_title)
        verticalLayout.addWidget(self.vessel_type)
        verticalLayout.addWidget(self.L)
        verticalLayout.addWidget(self.B)
        verticalLayout.addWidget(self.d)
        verticalLayout.addWidget(self.DW)
        verticalLayout.addWidget(self.speed)
        verticalLayout.addWidget(self.cargo_amount)
        verticalLayout.addWidget(self.cost_per_mile)
        verticalLayout.addWidget(self.cargo_demand)
        verticalLayout.addWidget(self.cargo_value)
        verticalLayout.addWidget(self.cargo_fragility)
        verticalLayout.addWidget(self.cargo_danger)
        verticalLayout.addWidget(self.sea_route)
        verticalLayout.addWidget(self.wind_strength)
        verticalLayout.addWidget(self.sea_state)

        # Отображаем слой на виджете
        self.setLayout(verticalLayout)

        # Шрифт
        font = QFont("Arial", 16)
        # Применяем шрифт к объектам
        self.vessel_title.setFont(font)
        self.vessel_type.setFont(font)
        self.L.setFont(font)
        self.B.setFont(font)
        self.d.setFont(font)
        self.DW.setFont(font)
        self.speed.setFont(font)
        self.cargo_amount.setFont(font)
        self.cost_per_mile.setFont(font)
        self.cargo_demand.setFont(font)
        self.cargo_value.setFont(font)
        self.cargo_fragility.setFont(font)
        self.cargo_danger.setFont(font)
        self.sea_route.setFont(font)
        self.wind_strength.setFont(font)
        self.sea_state.setFont(font)


        # Валидация значений указанных в предикторах
        self.vessel_title.setValidator(QRegularExpressionValidator(r"[A-Za-zА-Яа-я]+\s{1}\d{1,4}"))
        self.L.setValidator(QDoubleValidator(1, 600, 2))
        self.B.setValidator(QDoubleValidator(1, 70, 2))
        self.d.setValidator(QDoubleValidator(1, 30, 2))
        self.DW.setValidator(QDoubleValidator(1, 550000, 2))
        self.speed.setValidator(QDoubleValidator(1, 40, 2))
        self.cargo_amount.setValidator(QIntValidator(1, 550000))
        self.cost_per_mile.setValidator(QDoubleValidator(1, 70, 2))
        self.sea_route.setValidator(QIntValidator(1, 15000))
        self.wind_strength.setValidator(QIntValidator(0, 9))
        self.sea_state.setValidator(QIntValidator(0, 7))

        # =====================================================================#
        #                               Коннекты                               #
        # =====================================================================#
        self.L.textChanged.connect(self.validate_L)
        self.B.textChanged.connect(self.validate_B)
        self.d.textChanged.connect(self.validate_d)
        self.DW.textChanged.connect(self.validate_DW)
        self.speed.textChanged.connect(self.validate_speed)
        self.cargo_amount.textChanged.connect(self.validate_cargo_amount)
        self.cost_per_mile.textChanged.connect(self.validate_cost_per_mile)
        self.sea_route.textChanged.connect(self.validate_sea_route)
        self.wind_strength.textChanged.connect(self.validate_wind_strength)
        self.sea_state.textChanged.connect(self.validate_sea_state)
       

        # =====================================================================#
        #                               Размеры                                #
        # =====================================================================#
        # Размеры виджета
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setMaximumWidth(560)
        self.vessel_title.setMaximumSize(QSize(560, 45))
        self.vessel_type.setMaximumSize(QSize(560, 45))
        self.L.setMaximumSize(QSize(560, 45))
        self.B.setMaximumSize(QSize(560, 45))
        self.d.setMaximumSize(QSize(560, 45))
        self.DW.setMaximumSize(QSize(560, 45))
        self.speed.setMaximumSize(QSize(560, 45))
        self.cargo_amount.setMaximumSize(QSize(560, 45))
        self.cost_per_mile.setMaximumSize(QSize(560, 45))
        self.cargo_demand.setMaximumSize(QSize(560, 45))
        self.cargo_value.setMaximumSize(QSize(560, 45))
        self.cargo_fragility.setMaximumSize(QSize(560, 45))
        self.cargo_danger.setMaximumSize(QSize(560, 45))
        self.sea_route.setMaximumSize(QSize(560, 45))
        self.wind_strength.setMaximumSize(QSize(560, 45))
        self.sea_state.setMaximumSize(QSize(560, 45))


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
    def validate_vessel_title(self):
        if self.vessel_title.hasAcceptableInput():
            self.vessel_title.setStyleSheet("border: 2px solid white;")
        else:
            self.vessel_title.setStyleSheet("border: 2px solid red;")
    def validate_L(self):
        if self.L.hasAcceptableInput():
            self.L.setStyleSheet("border: 2px solid white;")
        else:
            self.L.setStyleSheet("border: 2px solid red;")
    def validate_B(self):
        if self.B.hasAcceptableInput():
            self.B.setStyleSheet("border: 2px solid white;")
        else:
            self.B.setStyleSheet("border: 2px solid red;")
    def validate_d(self):
        if self.d.hasAcceptableInput():
            self.d.setStyleSheet("border: 2px solid white;")
        else:
            self.d.setStyleSheet("border: 2px solid red;")
    def validate_DW(self):
        if self.DW.hasAcceptableInput():
            self.DW.setStyleSheet("border: 2px solid white;")
        else:
            self.DW.setStyleSheet("border: 2px solid red;")
    def validate_speed(self):
        if self.speed.hasAcceptableInput():
            self.speed.setStyleSheet("border: 2px solid white;")
        else:
            self.speed.setStyleSheet("border: 2px solid red;")
    def validate_cargo_amount(self):
        if self.cargo_amount.hasAcceptableInput():
            self.cargo_amount.setStyleSheet("border: 2px solid white;")
        else:
            self.cargo_amount.setStyleSheet("border: 2px solid red;")
    def validate_cost_per_mile(self):
        if self.cost_per_mile.hasAcceptableInput():
            self.cost_per_mile.setStyleSheet("border: 2px solid white;")
        else:
            self.cost_per_mile.setStyleSheet("border: 2px solid red;")
    def validate_sea_route(self):
        if self.sea_route.hasAcceptableInput():
            self.sea_route.setStyleSheet("border: 2px solid white;")
        else:
            self.sea_route.setStyleSheet("border: 2px solid red;")
    def validate_wind_strength(self):
        if self.wind_strength.hasAcceptableInput():
            self.wind_strength.setStyleSheet("border: 2px solid white;")
        else:
            self.wind_strength.setStyleSheet("border: 2px solid red;")
    def validate_sea_state(self):
        if self.sea_state.hasAcceptableInput():
            self.sea_state.setStyleSheet("border: 2px solid white;")
        else:
            self.sea_state.setStyleSheet("border: 2px solid red;")