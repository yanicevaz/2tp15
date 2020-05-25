from ex1 import *
from ex2 import *

if __name__ == "__main__":
    app = QApplication([])
    win1 = SQLClientWindow()
    win2 = ConfigurationDialog()
    win1.show()
    win2.show()
    app.exec_()
