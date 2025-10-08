
## Инструкция по запуску проекта

### Системные требования
- Python 3.11+
- Docker и docker-compose
- Poetry
- PostgreSQL (запускается через Docker)

### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/test_task.git
   cd test_task
   ```

2. Настройте окружение:
   - Используйте .env.example как пример
   - Заполните переменные для кастомных параметров

3. Установите зависимости:
   ```bash
   poetry install
   poetry shell
   ```

4. Запустите Docker:
   ```bash
   docker-compose up --build -d
   ```
   > Миграции применяются автоматически через `entrypoint.sh`
   
### Запуск

   - Документация API: [Swagger](http://localhost:8000/swagger/)
   - Админка: [Admin](http://localhost:8000/admin/)

---

### Архитектура
Проект реализован с использованием **чистой архитектуры**:
- `api/core/domain` — бизнес-логика и сущности
- `api/core/application` — сценарии использования
- `api/core/infrastructure` — адаптеры для БД

---

### Структура проекта
```
test_task/
├── api/               # Контроллеры и DTO / Ядро (Clean Architecture)
├── credit_application # Модуль кредитных заявок, с реализованной логикой в api/core
```

Остальные модели были также реализованы, но логика CRUD была опущены в рамках тестового задания.

- Docker настроен через multistage build
- Проброшены volumes для удобной локальной пере-сборки контейнеров
- Остальные модели реализованы, но CRUD опущен в рамках тестового задания
