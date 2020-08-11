from service.regression import RegressionService
from service.classification import ClassificationService

class MLService:

	def __init__(self):
		self.regression_service = RegressionService()
		self.classificaton_service = ClassificationService()


	def train(self, train_request):
		pred_type = train_request.pred_type

		if pred_type == 'Regression':
			self.regression_service.train(train_request)

		elif pred_type == 'Classification':
			self.classificaton_service.train(train_request)

		else:
			print('Unknown prediction type {}'.format(pred_type))