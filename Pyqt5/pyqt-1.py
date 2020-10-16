import sys
from PyQt5 import QtWidgets,QtGui

def Window():

    app = QtWidgets.QApplication(sys.argv)

    okay = QtWidgets.QPushButton("Okay")
    cancel = QtWidgets.QPushButton("Cancel")

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(okay)
    v_box.addWidget(cancel)


    h_box = QtWidgets.QHBoxLayout()
    #h_box.addWidget(okay)
    #h_box.addWidget(cancel)
    h_box.addStretch()
    h_box.addLayout(v_box)



    window = QtWidgets.QWidget()

    button = QtWidgets.QPushButton(window)

    button.setText("This is a button.....")

    window.setWindowTitle("PyQt5 Lesson 1")

    label1 = QtWidgets.QLabel(window)

    label2 = QtWidgets.QLabel(window)
    label2.setPixmap(QtGui.QPixmap("python.png"))

    label1.setText("This is a.....")
    label1.move(350,30)

    window.setLayout(h_box)

    window.setGeometry(100,100,800,500)

    window.show()

    sys.exit(app.exec_())

Window()