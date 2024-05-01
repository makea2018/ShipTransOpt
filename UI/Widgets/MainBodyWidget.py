from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QSpacerItem, QHBoxLayout,
                               QWidget, QSizePolicy, QLabel)
from Widgets.LeftPanelWidget import Left_Panel
from Widgets.RightPanelWidget import Right_Panel

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
        self.rightPanelWidget.predict_button.clicked.connect(self.validate_na_in_predictors_values)
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
    def predict_cost(self):
        init_text = self.rightPanelWidget.result_text_label.text()
        if init_text.endswith("- "):
            # Вычисление стоимости транспортировки груза
            cost = 1000
            # Запись стоимости в QLabel
            self.rightPanelWidget.result_text_label.setText(init_text + str(cost))
        print(self.predictors_values)

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
        elif all(x != "" for x in list(predictors_values.values())) and not cond:
            widget = self.rightPanelWidget.verticalLayout.takeAt(3)
            self.rightPanelWidget.verticalLayout.removeWidget(widget.widget().deleteLater())