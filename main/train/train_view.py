import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIntValidator
from main.train.train_service import TrainService

class TrainView:

	def __init__(self):
		self.train_service = TrainService()


	def create_view(self):
		label = qtw.QLabel('Train split percent:')
		self.train_box = qtw.QLineEdit()
		self.train_box.setValidator(QIntValidator(0, 99))
		self.train_box.textChanged.connect(self.train_box_changed)

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.train_box)
		return layout

		
	def train_box_changed(self):
		new_text = self.train_box.text()
		self.train_service.train_split_changed(new_text)
