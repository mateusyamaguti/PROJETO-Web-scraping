import requests

response = requests.get('https://jornadadodev.com.br/cursos/front-end')

# print('Status code:', response.status_code)
# print('↓↓ Header ↓↓')
# print(response.headers["X-Nf-Request-Id"])
# print(type(response.headers))

# print('\n↓↓ Content ↓↓')
print(response.content)