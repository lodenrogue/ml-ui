from model.train_request import TrainRequest
from service.ml_service import MLService

class RunService:

	def __init__(self):
		self.ml_service = MLService();


	def run(self, callback):
		req = TrainRequest.get_instance()

		if self.has_all_fields(req):
			accuracy = self.ml_service.train(req)
			callback('Accuracy: {}'.format(accuracy))
		else:
			callback('Error: All fields are required')


	def has_all_fields(self, req):
		if req.csv_path is None or req.csv_path == '':
			return False

		if req.pred_type is None or req.pred_type == '':
			return False

		if req.pred_column is None or req.pred_column == '':
			return False

		if req.algo is None or req.algo == '':
			return False

		if req.train_split is None or req.train_split == '':
			return False

		return True
		