import PyQt5.QtWidgets as qtw
from main.csv.file import FileService


class CsvView():

	def __init__(self):
		self.file_service = FileService()


	def create_view(self):
		label = qtw.QLabel('Path to csv:')
		self.csv_name_box = qtw.QLineEdit()

		button = qtw.QPushButton('Find')
		button.clicked.connect(lambda: self.file_service.get_file(self.get_file_callback))

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.csv_name_box)
		layout.addWidget(button)
		return layout


	def get_file_callback(self, fname):
		self.csv_name_box.setText(fname)