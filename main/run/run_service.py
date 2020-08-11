from model.train_request import TrainRequest
from service.ml_service import MLService

class RunService:

	def __init__(self):
		self.ml_service = MLService();


	def run(self):
		req = TrainRequest.get_instance()
		self.ml_service.train(req)
		