import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from main.run.run_service import RunService

class RunView:

	def __init__(self):
		self.run_service = RunService()


	def create_view(self):
		button = qtw.QPushButton('Run')
		button.clicked.connect(lambda: self.run_service.run(self.run_callback))
		self.results = qtw.QLabel('Accuracy:')

		layout = qtw.QVBoxLayout()
		layout.addWidget(button)
		layout.addWidget(self.results)
		layout.setAlignment(Qt.AlignCenter)
		return layout


	def run_callback(self, accuracy):
		self.results.setText('Accuracy: {}'.format(accuracy))