from PySide6.QtWidgets import QApplication ,QMainWindow , QPushButton , QLabel, QVBoxLayout , QWidget
from PySide6.QtGui import QIcon 
import sys 
from random import choice

jokes = [
    "Why did the scarecrow win an award? He was outstanding in his field",
"What do you call a fish with no eyes? Fsh!",
"What did the buffalo say when his son left for college? Bison.",
"What do you call a bear with no teeth? A gummy bear!",
"Why did the bicycle fall over? Because it was two tired.",
"What did the ocean say to the beach? Nothing, it just waved.",
"What do you call a fish with no eyes? Fsh!",
"What do you call a lazy kangaroo? A pouch potato.",
"What do you call a bear with no teeth? A gummy bear!",
"Why did the cookie go to the doctor? Because it was feeling crummy."
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.count = 10
        self.setWindowTitle("Joke Tailor")
        self.setWindowIcon(QIcon("icons8-funny-48.png"))

        layout = QVBoxLayout()


        self.mainLine = QLabel(self)
        self.mainLine.setText("WlCOME TO ME>>! 😁")
        layout.addWidget(self.mainLine)

        self.btn = QPushButton("press me.!",self)
        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.selectJoke)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def selectJoke(self):
        if self.count > 0:
            self.mainLine.setText(choice(jokes) +"  😂🔥")
            print(self.count)
            self.count -= 1
        else:
            self.mainLine.setText("GOOD BYE!.." + " 🙋🏻‍♂️👋🏻")
            self.btn.setEnabled(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())