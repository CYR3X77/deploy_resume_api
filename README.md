# Resume Website

## Описание
Веб-сервис, который путем получения ваших данных с помощью API генерирует резюме-страницу с информацией о вас.

## Требования
- Python 3.8+
- Git
- GitHub аккаунт

## Установка и запуск

1. **Создание репозитория**
   - Перейдите на https://github.com/new
   - Создайте новый репозиторий
   - Склонируйте его: `git clone <ваш_url_репозитория>`

2. **Получение GitHub токена**
   - Перейдите в Settings → Developer settings → Personal access tokens
   - Нажмите "Generate new token"
   - Выберите scopes: `repo`, `user`
   - Скопируйте сгенерированный токен

3. **Настройка проекта**
   ```bash
   cd api_resume
   python -m venv venv
   source venv/bin/activate  # Если у вас Linux/Mac
   venv\Scripts\activate     # Если у вас Windows
   pip install -r requirements.txt # Установите библиотеки
   Создайте файл .env и вставьте свой токен:GITHUB_TOKEN="Ваш_Токен"