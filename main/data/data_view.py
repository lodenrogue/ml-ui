import PyQt5.QtWidgets as qtw
from main.data.data_service import DataService


class DataView():

	def __init__(self):
		self.data_service = DataService()


	def create_view(self):
		layout = qtw.QVBoxLayout()
		layout.addLayout(self.create_csv_view())
		layout.addLayout(self.create_pred_column_view())
		return layout


	def create_csv_view(self):
		label = qtw.QLabel('Path to csv:')
		self.csv_name_box = qtw.QLineEdit()
		self.csv_name_box.setEnabled(False)
		self.csv_name_box.textChanged.connect(self.file_path_changed)

		button = qtw.QPushButton('Find')
		button.clicked.connect(lambda: self.data_service.get_file(self.get_file_callback))

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.csv_name_box)
		layout.addWidget(button)
		return layout

	
	def file_path_changed(self):
		new_text = self.csv_name_box.text()
		self.data_service.file_path_changed(new_text)


	def get_file_callback(self, fname):
		self.csv_name_box.setText(fname)
		
		if fname is not None and fname != '':
			self.column_combo.addItems(self.data_service.get_columns(fname))


	def create_pred_column_view(self):
		label = qtw.QLabel('Column to predict:')
		self.column_combo = qtw.QComboBox()
		self.column_combo.currentIndexChanged.connect(self.column_combo_change)

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.column_combo)
		return layout


	def column_combo_change(self, _):
		selection = str(self.column_combo.currentText())
		self.data_service.column_selection_changed(selection)