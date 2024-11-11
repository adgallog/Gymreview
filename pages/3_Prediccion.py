from modules.data_loader import load_model
from modules.prediction import predict_gender

model = load_model()
predict_gender(model)
