import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from main.run.run_service import RunService

class RunView:

	def __init__(self):
		self.run_service = RunService()


	def create_view(self):
		button = qtw.QPushButton('Run')
		button.clicked.connect(self.run_service.run)

		layout = qtw.QVBoxLayout()
		layout.addWidget(button)
		layout.setAlignment(Qt.AlignCenter)
		return layout