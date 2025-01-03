import os,sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon

# -----------------------------------------------------------------------------
# --- classe loginDialog
# -----------------------------------------------------------------------------

class loginDialog(QDialog):
    def __init__(self) -> None:
        
        super().__init__()
        self.setWindowTitle("Login")

        # Layouts
        mainLayout = QVBoxLayout()
        userLayout = QHBoxLayout()
        passwordLayout = QHBoxLayout() 

        # Widgets
        self.userText = QLabel("Nom d'utilisateur")
        self.userLine = QLineEdit()

        self.passText = QLabel("Mot de passe")
        self.passLine = QLineEdit()
        self.passLine.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn = QPushButton("Entrer")
        self.btn.clicked.connect(self.login)

        # Ajout des widgets et layouts
        userLayout.addWidget(self.userText)
        userLayout.addWidget(self.userLine)
        mainLayout.addLayout(userLayout)

        passwordLayout.addWidget(self.passText)
        passwordLayout.addWidget(self.passLine)
        mainLayout.addLayout(passwordLayout)

        mainLayout.addWidget(self.btn)

        self.setLayout(mainLayout)
    
    loginClicked = pyqtSignal(dict)

    def getLogin(self):
        """
        Cette fonction permet d'avoir le nom d'utilisateur et le mot de passe dans un dictionnaire.

        Paramètres :self (loginDialog): L'instance de la classe.
        Return :dict: Un dictionnaire contenant le nom d'utilisateur et le mot de passe.
        """
        dictionary = {}
        dictionary["username"] = self.userLine.text()
        dictionary["password"] = self.passLine.text()
        return dictionary

    def login(self):
        dict = self.getLogin()
        self.loginClicked.emit(dict)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = loginDialog()  
    window.show()
    sys.exit(app.exec())