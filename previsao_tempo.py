import requests

cidade = input("Qual cidade do Brasil você deseja saber a previsão do tempo? ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade},BR&appid=332c5f7091420efab975c2970262bbd9"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    descricao = data['weather'][0]['description']
    temperatura = round(data['main']['temp'] - 273.15, 2)
    umidade = data['main']['humidity']
    velocidade_vento = data['wind']['speed']
    print(f"Previsão do tempo em {cidade}:")
    print(f"Descrição: {descricao}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade: {umidade}%")
    print(f"Velocidade do vento: {velocidade_vento}m/s")
else:
    print("Erro ao obter a previsão do tempo.")