from PyQt5 import uic, QtWidgets
import Login




app=QtWidgets.QApplication([])
principal =uic.loadUi('Tela_principal.ui')
primeira_tela =uic.loadUi("tela1.ui")
segunda_tela  =uic.loadUi("tela2.ui")
tela_cadastro =uic.loadUi("tela_cadastro.ui")

principal.show()
app.exec()
