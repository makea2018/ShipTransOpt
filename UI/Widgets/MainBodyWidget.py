from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QSpacerItem, QHBoxLayout,
                               QWidget, QSizePolicy, QLabel)
from Widgets.LeftPanelWidget import Left_Panel
from Widgets.RightPanelWidget import Right_Panel
import numpy as np

class NotValidLabel(QWidget):
    def __init__(self, text):
        super().__init__()
        # =====================================================================#
        #                               Фронт                                  #
        # =====================================================================#
        NotValidLabel = QLabel(text)
        # Шрифт
        font = QFont("Arial", 20)
        
        NotValidLabel.setFont(font)

        # Горизонтальный слой
        h_layout = QHBoxLayout()
        h_layout.addWidget(NotValidLabel)
        # Отступы контента внутри виджета
        h_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(h_layout)

        # =====================================================================#
        #                               Размеры                                #
        # =====================================================================#
        self.setMaximumSize(QSize(1250, 106))
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)


        # =====================================================================#
        #                               Стили                                  #
        # =====================================================================#
        NotValidLabel.setStyleSheet(
            """
                background-color: rgb(94, 139, 255);
                border: 2px solid white;
                color: #FA8072;
            """
        )
        

class MainBody(QWidget):
    def __init__(self):
        super().__init__()
        # =====================================================================#
        #                               Фронт                                  #
        # =====================================================================#
        # Виджеты левая и правая части
        self.leftPanelWidget = Left_Panel()
        self.rightPanelWidget = Right_Panel()

        # Значения предикторов
        self.predictors_values = {}
        
        # Spacer
        horizontalSpacer = QSpacerItem(120, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        # Слои
        horizontalLayout = QHBoxLayout()
        # Добавляем элементы на горизонтальный слой
        horizontalLayout.addWidget(self.leftPanelWidget)
        horizontalLayout.addItem(horizontalSpacer)
        horizontalLayout.addWidget(self.rightPanelWidget)

        # Отображаем слой на виджете
        self.setLayout(horizontalLayout)

        # =====================================================================#
        #                               Коннекты                               #
        # =====================================================================#
        # Валидация ввода значений предикторов
        self.leftPanelWidget.L.textChanged.connect(self.validate_L)
        self.leftPanelWidget.B.textChanged.connect(self.validate_B)
        self.leftPanelWidget.d.textChanged.connect(self.validate_d)
        self.leftPanelWidget.DW.textChanged.connect(self.validate_DW)
        self.leftPanelWidget.speed.textChanged.connect(self.validate_speed)
        self.leftPanelWidget.cargo_amount.textChanged.connect(self.validate_cargo_amount)
        self.leftPanelWidget.cost_per_mile.textChanged.connect(self.validate_cost_per_mile)
        self.leftPanelWidget.sea_route.textChanged.connect(self.validate_sea_route)
        self.leftPanelWidget.wind_strength.textChanged.connect(self.validate_wind_strength)
        self.leftPanelWidget.sea_state.textChanged.connect(self.validate_sea_state)
        # Предсказание стоимости транспортировки груза (Кнопка 'Определить')
        self.rightPanelWidget.predict_button.clicked.connect(self.predict_cost)

        # =====================================================================#
        #                               Размеры                                #
        # =====================================================================#



        # =====================================================================#
        #                               Стили                                  #
        # =====================================================================#



    # =====================================================================#
    #                               Функции                                #
    # =====================================================================#
    
    #=====================================================================#
    #            Валидация ввода значений предикторов                     #
    #=====================================================================#
    def validate_L(self):
        if self.leftPanelWidget.L.hasAcceptableInput():
            self.leftPanelWidget.L.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.L.setStyleSheet("border: 2px solid red;")
    def validate_B(self):
        if self.leftPanelWidget.B.hasAcceptableInput():
            self.leftPanelWidget.B.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.B.setStyleSheet("border: 2px solid red;")
    def validate_d(self):
        if self.leftPanelWidget.d.hasAcceptableInput():
            self.leftPanelWidget.d.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.d.setStyleSheet("border: 2px solid red;")
    def validate_DW(self):
        if self.leftPanelWidget.DW.hasAcceptableInput():
            self.leftPanelWidget.DW.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.DW.setStyleSheet("border: 2px solid red;")
    def validate_speed(self):
        if self.leftPanelWidget.speed.hasAcceptableInput():
            self.leftPanelWidget.speed.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.speed.setStyleSheet("border: 2px solid red;")
    def validate_cargo_amount(self):
        if self.leftPanelWidget.cargo_amount.hasAcceptableInput():
            self.leftPanelWidget.cargo_amount.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.cargo_amount.setStyleSheet("border: 2px solid red;")
    def validate_cost_per_mile(self):
        if self.leftPanelWidget.cost_per_mile.hasAcceptableInput():
            self.leftPanelWidget.cost_per_mile.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.cost_per_mile.setStyleSheet("border: 2px solid red;")
    def validate_sea_route(self):
        if self.leftPanelWidget.sea_route.hasAcceptableInput():
            self.leftPanelWidget.sea_route.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.sea_route.setStyleSheet("border: 2px solid red;")
    def validate_wind_strength(self):
        if self.leftPanelWidget.wind_strength.hasAcceptableInput():
            self.leftPanelWidget.wind_strength.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.wind_strength.setStyleSheet("border: 2px solid red;")
    def validate_sea_state(self):
        if self.leftPanelWidget.sea_state.hasAcceptableInput():
            self.leftPanelWidget.sea_state.setStyleSheet("border: 2px solid white;")
        else:
            self.leftPanelWidget.sea_state.setStyleSheet("border: 2px solid red;")
    
    # Функция отключения кнопки 'Определить'
    def validate_invalid_input(self):
        inputs = [self.leftPanelWidget.L.hasAcceptableInput(),
                  self.leftPanelWidget.B.hasAcceptableInput(),
                  self.leftPanelWidget.d.hasAcceptableInput(),
                  self.leftPanelWidget.DW.hasAcceptableInput(),
                  self.leftPanelWidget.speed.hasAcceptableInput(),
                  self.leftPanelWidget.cargo_amount.hasAcceptableInput(),
                  self.leftPanelWidget.cost_per_mile.hasAcceptableInput(),
                  self.leftPanelWidget.sea_route.hasAcceptableInput(),
                  self.leftPanelWidget.wind_strength.hasAcceptableInput(),
                  self.leftPanelWidget.sea_state.hasAcceptableInput()
                  ]
        
        return all(inputs)
    
    #=====================================================================#
    #            Взаимодействие с кнопкой 'Определить'                    #
    #=====================================================================#
    def write_predictors_values(self):
        # Записываем все значения предикторов в словарь предикторов
        self.predictors_values["vessel_title"] = self.leftPanelWidget.vessel_title.text()
        self.predictors_values["vessel_type"] = self.leftPanelWidget.vessel_type.currentText()
        self.predictors_values["L"] = self.leftPanelWidget.L.text()
        self.predictors_values["B"] = self.leftPanelWidget.B.text()
        self.predictors_values["d"] = self.leftPanelWidget.d.text()
        self.predictors_values["DW"] = self.leftPanelWidget.DW.text()
        self.predictors_values["speed"] = self.leftPanelWidget.speed.text()
        self.predictors_values["cargo_amount"] = self.leftPanelWidget.cargo_amount.text()
        self.predictors_values["cost_per_mile"] = self.leftPanelWidget.cost_per_mile.text()
        self.predictors_values["cargo_demand"] = self.leftPanelWidget.cargo_demand.currentText()
        self.predictors_values["cargo_value"] = self.leftPanelWidget.cargo_value.currentText()
        self.predictors_values["cargo_fragility"] = self.leftPanelWidget.cargo_fragility.currentText()
        self.predictors_values["cargo_danger"] = self.leftPanelWidget.cargo_danger.currentText()
        self.predictors_values["sea_route"] = self.leftPanelWidget.sea_route.text()
        self.predictors_values["wind_strength"] = self.leftPanelWidget.wind_strength.text()
        self.predictors_values["sea_state"] = self.leftPanelWidget.sea_state.text()
        return self.predictors_values

    def validate_na_in_predictors_values(self):
        predictors_values = self.write_predictors_values()
        # Условие что в виджете меньше 3 сообщений (Кнопка + Сообщение со стоимостью + Предупреждение валидации)
        cond = self.rightPanelWidget.verticalLayout.count() < 4
        # Проверяем, что все значения для предикторов заполнены
        if any(x == "" for x in list(predictors_values.values())) and cond:
            # Добавляем виджет о том, что данные не валидированы
            Warning_Label = NotValidLabel("Не все значения предикторов были заполнены!")
            self.rightPanelWidget.verticalLayout.addWidget(Warning_Label)
            return False
        elif all(x != "" for x in list(predictors_values.values())) and not cond:
            widget = self.rightPanelWidget.verticalLayout.takeAt(3)
            self.rightPanelWidget.verticalLayout.removeWidget(widget.widget().deleteLater())
            return True
        
        return True

    def predict_cost(self):
        na_validation_result = self.validate_na_in_predictors_values()
        invalid_input_validation_result = self.validate_invalid_input()
        # Добавляем надпись если хотя бы одно значение невалидное (горит красным)
        if not invalid_input_validation_result and self.rightPanelWidget.verticalLayout.count() < 5:
            warning = NotValidLabel("Один или несколько предикторов имеют неверный ввод!")
            self.rightPanelWidget.verticalLayout.addWidget(warning)
            return 0
        # Удаляем надпись если все значения валидные
        elif invalid_input_validation_result:
            if self.rightPanelWidget.verticalLayout.count() == 4:
                widget = self.rightPanelWidget.verticalLayout.takeAt(3)
                self.rightPanelWidget.verticalLayout.removeWidget(widget.widget().deleteLater())
            elif self.rightPanelWidget.verticalLayout.count() == 5:
                widget = self.rightPanelWidget.verticalLayout.takeAt(4)
                self.rightPanelWidget.verticalLayout.removeWidget(widget.widget().deleteLater())

            if na_validation_result:
                # Обработка результатов числовых предикторов
                self.predictors_values["L"] = float(self.predictors_values["L"])
                self.predictors_values["B"] = float(self.predictors_values["B"])
                self.predictors_values["d"] = float(self.predictors_values["d"])
                self.predictors_values["DW"] = float(self.predictors_values["DW"])
                self.predictors_values["speed"] = float(self.predictors_values["speed"])
                self.predictors_values["cargo_amount"] = int(self.predictors_values["cargo_amount"])
                self.predictors_values["cost_per_mile"] = float(self.predictors_values["cost_per_mile"])
                self.predictors_values["sea_route"] = int(self.predictors_values["sea_route"])
                self.predictors_values["wind_strength"] = int(self.predictors_values["wind_strength"])
                self.predictors_values["sea_state"] = int(self.predictors_values["sea_state"])

                # Обработка результатов категориальных предикторов
                self.predictors_values["vessel_type"]
                self.predictors_values["cargo_demand"]
                self.predictors_values["cargo_value"]
                self.predictors_values["cargo_fragility"]
                self.predictors_values["cargo_danger"]
        
                print(self.predictors_values)
            
            return 1

        # init_text = self.rightPanelWidget.result_text_label.text()
        # if init_text.endswith("- "):
        #     # Вычисление стоимости транспортировки груза
        #     cost = 1000
        #     # Запись стоимости в QLabel
        #     self.rightPanelWidget.result_text_label.setText(init_text + str(cost))
        # print(self.predictors_values)