from fastapi import FastAPI
from pydantic import BaseModel, StrictStr
import pickle
import warnings

# Отключение предупреждения UserWarning
warnings.filterwarnings("ignore", category=UserWarning)

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

# Класс для валидации входных данных
class Data(BaseModel):
    vessel_title: StrictStr
    vessel_type: int
    L: float
    B: float
    d: float
    DW: int
    speed: float
    cargo_amount: int
    cost_per_mile: float
    cargo_demand: int
    cargo_value: int
    cargo_fragility: int
    cargo_danger: int
    sea_route: int
    wind_strength: int
    sea_state: int

# Методы API
@app.get("/", description="Метод выдает информацию о том, успешно ли загрузилась модель нейросети")
def get_model_info():
    if model_answer:
        return "Модель knn успешно загружена и готова к работе"
    else:
        return "Ошибка при загрузке модели knn"
    
@app.post("/predict", description="Модель предсказывает стоимость транспортировки груза")
def predict(vars: Data):
    # Определение предикторов из тела vars
    vars = list(dict(vars).values())[1:]
    
    # Предсказание модели
    predictions = knnModel.predict([vars]).round(2)

    return {"prediction": predictions[0]}
