
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QIcon

def closeApp():
    window.close()

def submitInfo():
    name = "Jhon"
    password = "123"

    boxSubmit = QMessageBox()
    boxSubmit.setWindowTitle("Login Message")

    if txtUsername.text() == name and txtPassword.text() == password:
        boxSubmit.setText("You are successfully logged in!")
        btnSubmit = boxSubmit.exec()
    else:
        boxSubmit.setText("Your username or password might be incorrect, please try again.")
        btnSubmit = boxSubmit.exec()

app = QApplication()
window = QWidget()
window.setFixedSize(400, 200)
window.setWindowTitle("Login App")
window.setWindowIcon(QIcon("E:\Coding\Python\Python PySide6\Completed Projects\Basic_Ui_(178).png"))

# labels
lblUsername = QLabel("Username", parent=window)
lblUsername.move(60, 30)
lblPassword = QLabel("Password", parent=window)
lblPassword.move(60, 65)

# text box
txtUsername = QLineEdit(parent=window)
txtUsername.setFixedWidth(190)
txtUsername.setPlaceholderText("Enter your username...")
txtUsername.move(130, 30)

txtPassword = QLineEdit(parent=window)
txtPassword.setFixedWidth(190)
txtPassword.setPlaceholderText("Enter your password...")
txtPassword.setEchoMode(QLineEdit.Password)
txtPassword.move(130, 65)

# buttons
btnClose = QPushButton("Close", parent=window)
btnClose.move(210, 160)
btnClose.clicked.connect(closeApp)

btnSubmit = QPushButton("Submit", parent=window)
btnSubmit.move(120, 160)
btnSubmit.clicked.connect(submitInfo)

window.show()
app.exec()