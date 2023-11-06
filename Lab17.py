# import sys
# from PySide6 import QtCore, QtWidgets

# class Example(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.text = QtWidgets.QLabel("Hello World")
#         self.layout = QtWidgets.QVBoxLayout()
#         self.layout.addWidget(self.text)
#         self.setLayout(self.layout)

# app = QtWidgets.QApplication([])

# ex = Example()
# ex.show()

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
boostrap = Bootstrap5(app)

@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2

@app.route('/mytemplate')
def t_test():
    return render_template('my_template_1.html')

@app.route('/andrea')
def andrea():
    return render_template('template.html')

# <!-- in templates/my_template_1.html -->
# <p>Sample paragraph!</p>

