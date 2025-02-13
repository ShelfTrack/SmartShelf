import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ShelfTrack - Library Management System")
        self.setGeometry(100, 100, 600, 400)
        self.label = QLabel("Welcome to ShelfTrack!", self)
        self.label.setGeometry(200, 150, 200, 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec())
