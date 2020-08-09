import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

class RunView:

	def create_view(self):
		button = qtw.QPushButton('Run')
		layout = qtw.QVBoxLayout()
		layout.addWidget(button)
		layout.setAlignment(Qt.AlignCenter)
		return layout