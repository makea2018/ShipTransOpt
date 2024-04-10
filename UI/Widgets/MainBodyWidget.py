from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QSpacerItem, QHBoxLayout,
                               QWidget, QSizePolicy)
from Widgets.LeftPanelWidget import Left_Panel
from Widgets.RightPanelWidget import Right_Panel

class MainBody(QWidget):
    def __init__(self):
        super().__init__()
        # =====================================================================#
        #                               Фронт                                  #
        # =====================================================================#
        # Виджеты левая и правая части
        leftPanelWidget = Left_Panel()
        rightPanelWidget = Right_Panel()
        
        # Spacer
        horizontalSpacer = QSpacerItem(120, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        # Слои
        horizontalLayout = QHBoxLayout()
        # Добавляем элементы на горизонтальный слой
        horizontalLayout.addWidget(leftPanelWidget)
        horizontalLayout.addItem(horizontalSpacer)
        horizontalLayout.addWidget(rightPanelWidget)

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



    # =====================================================================#
    #                               Функции                                #
    # =====================================================================#