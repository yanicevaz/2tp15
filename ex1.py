from PySide2.QtWidgets import *

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600, 400)
        layout = QVBoxLayout()

        buttonspanel = ButtonsPanel()
        notificationPanel = QTextEdit()

        resultTable = QTableWidget(5, 3)
        resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(buttonspanel)
        layout.addWidget(notificationPanel)
        layout.addWidget(resultTable)

        self.setLayout(layout)

class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()

        button1 = QPushButton("Configure")
        button2 = QPushButton("Connect")
        button3 = QPushButton("Disconnect")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        self.setLayout(layout)
