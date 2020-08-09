import json

class TrainRequest:
	_instance = None

	@staticmethod
	def get_instance():
		if TrainRequest._instance is None:
			TrainRequest._instance = TrainRequest()
		return TrainRequest._instance


	def __init__(self):
		self._csv_path = None
		self._pred_type = None
		self._pred_column = None
		self._algo = None
		self._train_split = None


	@property
	def csv_path(self):
		return self._csv_path


	@csv_path.setter
	def csv_path(self, value):
		self._csv_path = value


	@property
	def pred_type(self):
		return self._pred_type


	@pred_type.setter
	def pred_type(self, value):
		self._pred_type = value


	@property
	def pred_column(self):
		return self._pred_column


	@pred_column.setter
	def pred_column(self, value):
		self._pred_column = value
	

	@property
	def algo(self):
		return self._algo


	@algo.setter
	def algo(self, value):
		self._algo = value


	@property
	def train_split(self):
		return self._train_split


	@train_split.setter
	def train_split(self, value):
		self._train_split = value


	def __str__(self):
		return json.dumps(self.__dict__)