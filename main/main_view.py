import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from service.file import FileService
from service.prediction import PredictionService


class MainView(qtw.QMainWindow):
	def __init__(self, parent=None):
		super(MainView, self).__init__(parent)

		self.file_service = FileService()
		self.prediction_service = PredictionService()

		view = self.create_view()
		self.setCentralWidget(view)
		self.show()


	def create_view(self):
		layout = qtw.QVBoxLayout()
		layout.addLayout(self.create_csv_view())
		layout.addLayout(self.create_pred_column_view())
		layout.addLayout(self.create_pred_type_view())
		layout.addLayout(self.create_algo_select_view())
		layout.addLayout(self.create_train_percent_view())
		layout.addLayout(self.create_run_view())
		
		layout.setContentsMargins(25, 25, 25, 25)
		layout.setSpacing(15)

		view = qtw.QWidget()
		view.setLayout(layout)
		return view


	def create_train_percent_view(self):
		return self.create_label_box_view('Train split percent:')


	def create_run_view(self):
		button = qtw.QPushButton('Run')
		layout = qtw.QVBoxLayout()
		layout.addWidget(button)
		layout.setAlignment(Qt.AlignCenter)
		return layout


	def create_algo_select_view(self):
		label = qtw.QLabel('Algorithm:')
		self.algo_combo_box = qtw.QComboBox()

		selected_pred_type = str(self.pred_type_combo_box.currentText())
		self.algo_combo_box.addItems(self.prediction_service.get_algos(selected_pred_type))

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.algo_combo_box)
		return layout


	def create_pred_type_view(self):
		label = qtw.QLabel('Prediction type:')
		self.pred_type_combo_box = qtw.QComboBox()
		self.pred_type_combo_box.addItems(self.prediction_service.get_pred_types())
		self.pred_type_combo_box.currentIndexChanged.connect(self.pred_combo_change)

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.pred_type_combo_box)
		return layout


	def pred_combo_change(self, index):
		selected_pred_type = str(self.pred_type_combo_box.currentText())
		self.algo_combo_box.clear()
		self.algo_combo_box.addItems(self.prediction_service.get_algos(selected_pred_type))


	def create_csv_view(self):
		label = qtw.QLabel('Path to csv:')
		self.csv_name_box = qtw.QLineEdit()

		button = qtw.QPushButton('Find')
		button.clicked.connect(lambda: self.file_service.get_file(self.get_file_callback))

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.csv_name_box)
		layout.addWidget(button)
		return layout


	def create_pred_column_view(self):
		label = qtw.QLabel('Column to predict:')
		self.column_input_box = qtw.QLineEdit()

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.column_input_box)
		return layout


	def create_label_box_view(self, label_text):
		label = qtw.QLabel(label_text)
		input_box = qtw.QLineEdit()

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(input_box)
		return layout


	def get_file_callback(self, fname):
		self.csv_name_box.setText(fname)
