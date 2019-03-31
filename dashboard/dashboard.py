from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
import qrc_dashboard


if __name__ == "__main__":
    import sys

    # Create an instance of the application
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(":/fonts/DejaVuSans.ttf")
    app.setFont(QFont("DejaVu Sans"))
    # Create QML engine
    engine = QQmlApplicationEngine()
    # Load the qml file into the engine
    engine.load(QUrl("qrc:/qml/dashboard.qml"))

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())