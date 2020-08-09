import PyQt5.QtWidgets as qtw
from main.prediction.prediction_service import PredictionService

class PredictionView:
	def __init__(self):
		self.prediction_service = PredictionService()


	def create_view(self):
		layout = qtw.QVBoxLayout()
		layout.addLayout(self.create_pred_column_view())
		layout.addLayout(self.create_pred_type_view())
		layout.addLayout(self.create_algo_select_view())
		return layout


	def create_algo_select_view(self):
		label = qtw.QLabel('Algorithm:')
		self.algo_combo = qtw.QComboBox()

		selected_pred_type = str(self.pred_type_combo.currentText())
		self.algo_combo.addItems(self.prediction_service.get_algos(selected_pred_type))
		self.algo_combo.currentIndexChanged.connect(self.algo_combo_changed)

		selected_algo = str(self.algo_combo.currentText())
		self.prediction_service.algo_changed(selected_algo)

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.algo_combo)
		return layout


	def create_pred_type_view(self):
		label = qtw.QLabel('Prediction type:')
		self.pred_type_combo = qtw.QComboBox()
		self.pred_type_combo.addItems(self.prediction_service.get_pred_types())
		self.pred_type_combo.currentIndexChanged.connect(self.pred_combo_change)

		selected_pred_type = str(self.pred_type_combo.currentText())
		self.prediction_service.pred_changed(selected_pred_type)

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.pred_type_combo)
		return layout


	def pred_combo_change(self, _):
		selected_pred_type = str(self.pred_type_combo.currentText())
		self.algo_combo.clear()
		self.algo_combo.addItems(self.prediction_service.get_algos(selected_pred_type))
		self.prediction_service.pred_changed(selected_pred_type)


	def algo_combo_changed(self, _):
		selected_algo = str(self.algo_combo.currentText())
		self.prediction_service.algo_changed(selected_algo)


	def create_pred_column_view(self):
		label = qtw.QLabel('Column to predict:')
		self.column_input_box = qtw.QLineEdit()
		self.column_input_box.textChanged.connect(self.column_text_changed)

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.column_input_box)
		return layout


	def column_text_changed(self):
		new_text = self.column_input_box.text()
		self.prediction_service.column_text_changed(new_text)
