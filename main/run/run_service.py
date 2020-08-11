from model.train_request import TrainRequest
from service.ml_service import MLService

class RunService:

	def __init__(self):
		self.ml_service = MLService();


	def run(self, callback):
		req = TrainRequest.get_instance()
		accuracy = self.ml_service.train(req)
		callback(accuracy)
		