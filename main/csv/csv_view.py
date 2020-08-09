import PyQt5.QtWidgets as qtw
from main.csv.csv_service import CsvService


class CsvView():

	def __init__(self):
		self.csv_service = CsvService()


	def create_view(self):
		label = qtw.QLabel('Path to csv:')
		self.csv_name_box = qtw.QLineEdit()
		self.csv_name_box.textChanged.connect(self.text_changed)

		button = qtw.QPushButton('Find')
		button.clicked.connect(lambda: self.csv_service.get_file(self.get_file_callback))

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.csv_name_box)
		layout.addWidget(button)
		return layout

	
	def text_changed(self):
		new_text = self.csv_name_box.text()
		self.csv_service.text_changed(new_text)


	def get_file_callback(self, fname):
		self.csv_name_box.setText(fname)