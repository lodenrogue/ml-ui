from service.base_service import BaseService
from sklearn.linear_model import Lasso, ElasticNet, Ridge
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor, ExtraTreesRegressor, AdaBoostRegressor, GradientBoostingRegressor

class RegressionService(BaseService):

	def __init__(self):
		self.models = {
			'Lasso': Lasso,
			'ElasticNet': ElasticNet,
			'Ridge': Ridge,
			'MLPRegressor': MLPRegressor,
			'BaggingRegressor': BaggingRegressor,
			'RandomForestRegressor': RandomForestRegressor,
			'ExtraTreesRegressor': ExtraTreesRegressor,
			'AdaBoostRegressor': AdaBoostRegressor,
			'GradientBoostingRegressor': GradientBoostingRegressor
		}


	def get_models(self):
		return self.models