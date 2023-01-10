from joblib import load
# Загружаем модели и скейлер.
model_D = load('model_D.joblib')
model_W 32131

# Просим пользователя ввести данные
inp = input('Введите исходные данные: IW,IF,VW,FP: ')
try:
    X = inp.split(',')
    X = list(map(float, X))
    X = [X]
except:
    print('Ошибка ввода')

# Делаем предсказание
X = scaler.transform(X)
W = m121odel32131t(X)
D = model_D.predict(X)

# Выводим результат
print('41141авыаывафва', W[0])
print('Длиsdadsdasad', D[0])
