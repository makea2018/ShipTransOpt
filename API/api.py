from fastapi import FastAPI
import pickle
import numpy as np

# Загрузка модели
try:
    with open("./KNN_models/KNN_model_3.pkl", "rb") as f:
        knnModel = pickle.load(f)
    # Ответ от модели
    model_answer = True
except:
    # Ответ от модели
    model_answer = False

# Создание объекта API приложения
app = FastAPI(
    title="ShipTransOpt API",
    version="1_0"
)

# Загрузка тестовых данных
values = {'vessel_title': 'Maria', 'vessel_type': 'сухогруз',
          'L': 12, 'B': 2, 'd': 0.3, 'DW': 100, 'speed': 2.2,
          'cargo_amount': 25, 'cost_per_mile': 1.2, 'cargo_demand': 'маленький',
          'cargo_value': 'ценный', 'cargo_fragility': 'не хрупкий',
          'cargo_danger': 'не опасный', 'sea_route': 1000,
          'wind_strength': 1, 'sea_state': 1}

# Предобработка данных
values['vessel_type'] = int(np.where(values['vessel_type'] == 'сухогруз', 0, 1))
values['cargo_demand'] = int(np.where(values['cargo_demand'] == "маленький", 0, 1))
values['cargo_value'] = int(np.select([values['cargo_value'] == "обычный", values['cargo_value'] == "ценный", values['cargo_value'] == "очень ценный"], [0, 1, 2]))
values['cargo_fragility'] = int(np.where(values['cargo_fragility'] == "не хрупкий", 0, 1))
values['cargo_danger'] = int(np.where(values['vessel_type'] == 'не опасный', 0, 1))

vars = list(values.values())[1:]

# Методы API
@app.get("/", description="Метод выдает информацию о том, успешно ли загрузилась модель нейросети")
def get_model_info():
    if model_answer:
        return "Модель knn успешно загружена и готова к работе"
    else:
        return "Ошибка при загрузке модели knn"
    
@app.post("/predict", description="Модель предсказывает стоимость транспортировки груза")
def predict(vars: list = vars):
    # Предсказание
    predictions = knnModel.predict([vars]).round(2)

    return {"prediction": predictions[0]}
