import sys
from PySide6.QtWidgets import QApplication
from Widgets.MainWindow import MainWindow
from Widgets.MainBodyWidget import MainBody

# Создание приложения
app = QApplication(sys.argv)

# Главное окно приложения
window = MainWindow()
# Виджет основного тела приложения
mainBody = MainBody()
# Помещаем виджеты на экран
window.setCentralWidget(mainBody)
window.show()

# Запуск приложения
app.exec()