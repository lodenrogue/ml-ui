import PyQt5.QtWidgets as qtw

class TrainView:

	def create_view(self):
		label = qtw.QLabel('Train split percent:')
		input_box = qtw.QLineEdit()

		layout = qtw.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(input_box)
		return layout
		
