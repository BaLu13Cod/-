# Инструкции по установке Cloud Security System

## Системные требования

### Минимальные требования
- **Операционная система**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python**: 3.8 или выше
- **RAM**: 4 GB
- **Дисковое пространство**: 2 GB
- **Процессор**: 2 ядра

### Рекомендуемые требования
- **RAM**: 8 GB или больше
- **Дисковое пространство**: 5 GB
- **Процессор**: 4 ядра или больше
- **Сеть**: Стабильное интернет-соединение

## Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-username/cloud-security-system.git
cd cloud-security-system
```

### 2. Создание виртуального окружения

#### Windows
```cmd
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка конфигурации

Создайте файл `.env` в корневой директории:

```env
# Основные настройки
APP_NAME=Cloud Security System
VERSION=1.0.0
DEBUG=true

# База данных
DATABASE_URL=postgresql://user:password@localhost/cloud_security
REDIS_URL=redis://localhost:6379

# API настройки
API_HOST=0.0.0.0
API_PORT=8000

# Безопасность
SECRET_KEY=your-super-secret-key-here-change-this
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# ML модели
MODEL_PATH=./models/
THREAT_DETECTION_THRESHOLD=0.8

# Мониторинг
LOG_LEVEL=INFO
METRICS_PORT=9090

# Интеграции
WEBHOOK_URL=https://your-webhook-url.com/security
SLACK_WEBHOOK=https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

## Быстрый запуск

### Вариант 1: Автоматический запуск

```bash
python start.py
```

Этот скрипт:
- Проверит зависимости
- Создаст необходимые директории
- Запустит API сервер
- Покажет инструкции по использованию

### Вариант 2: Ручной запуск

#### Запуск API сервера
```bash
python -m api.main
```

#### Запуск основной системы
```bash
python main.py
```

#### Запуск демонстрации
```bash
python run_demo.py
```

## Проверка установки

### 1. Проверка API

Откройте браузер и перейдите по адресу:
- **API**: http://localhost:8000
- **Документация**: http://localhost:8000/docs
- **Health check**: http://localhost:8000/health

### 2. Проверка логирования

Проверьте файл `cloud_security.log` в корневой директории.

### 3. Проверка моделей

Убедитесь, что директория `models/` создана и доступна для записи.

## Настройка интеграций

### AWS интеграция

1. Создайте IAM пользователя в AWS
2. Назначьте необходимые права доступа
3. Получите Access Key и Secret Key
4. Добавьте интеграцию через API:

```bash
curl -X POST "http://localhost:8000/integrations" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AWS_Production",
    "type": "cloud",
    "endpoint_url": "https://ec2.amazonaws.com",
    "credentials": {
      "region": "us-east-1",
      "access_key": "YOUR_ACCESS_KEY",
      "secret_key": "YOUR_SECRET_KEY"
    }
  }'
```

### Azure интеграция

1. Создайте Service Principal в Azure
2. Получите Client ID, Client Secret и Tenant ID
3. Добавьте интеграцию:

```bash
curl -X POST "http://localhost:8000/integrations" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Azure_Production",
    "type": "cloud",
    "endpoint_url": "https://management.azure.com",
    "credentials": {
      "subscription_id": "YOUR_SUBSCRIPTION_ID",
      "tenant_id": "YOUR_TENANT_ID",
      "client_id": "YOUR_CLIENT_ID",
      "client_secret": "YOUR_CLIENT_SECRET"
    }
  }'
```

### Локальные устройства

```bash
curl -X POST "http://localhost:8000/integrations" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Local_Device",
    "type": "device",
    "endpoint_url": "http://192.168.1.100:8080",
    "polling_interval": 30
  }'
```

## Настройка безопасности

### 1. Изменение секретного ключа

Обязательно измените `SECRET_KEY` в файле `.env` на уникальное значение.

### 2. Настройка JWT

```env
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Настройка CORS

По умолчанию CORS разрешен для всех источников. Для продакшена ограничьте доступ:

```python
# В api/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

## Мониторинг и логирование

### 1. Настройка уровней логирования

```env
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
```

### 2. Ротация логов

Система автоматически создает логи в файле `cloud_security.log`.

### 3. Метрики

Метрики доступны по адресу: http://localhost:9090

## Устранение неполадок

### Проблема: "Module not found"

**Решение**: Убедитесь, что виртуальное окружение активировано и зависимости установлены.

```bash
pip install -r requirements.txt
```

### Проблема: "Port already in use"

**Решение**: Измените порт в конфигурации или остановите процесс, использующий порт 8000.

```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/macOS
lsof -i :8000
kill -9 <PID>
```

### Проблема: "Permission denied"

**Решение**: Убедитесь, что у вас есть права на запись в директорию проекта.

### Проблема: "Database connection failed"

**Решение**: Проверьте настройки подключения к базе данных в файле `.env`.

## Обновление системы

### 1. Остановка системы

```bash
# Остановите все процессы
Ctrl+C
```

### 2. Обновление кода

```bash
git pull origin main
```

### 3. Обновление зависимостей

```bash
pip install -r requirements.txt --upgrade
```

### 4. Перезапуск

```bash
python start.py
```

## Резервное копирование

### 1. Модели ML

```bash
cp -r models/ models_backup_$(date +%Y%m%d_%H%M%S)/
```

### 2. Конфигурация

```bash
cp .env .env_backup_$(date +%Y%m%d_%H%M%S)
```

### 3. Логи

```bash
cp cloud_security.log cloud_security_backup_$(date +%Y%m%d_%H%M%S).log
```

## Поддержка

### Документация
- **README.md** - Основная документация
- **API docs** - http://localhost:8000/docs

### Логи
- **Системные логи**: `cloud_security.log`
- **API логи**: В терминале при запуске API сервера

### Тестирование
```bash
# Запуск демонстрации
python run_demo.py

# Проверка API
curl http://localhost:8000/health
```

## Следующие шаги

После успешной установки:

1. **Изучите API**: Откройте http://localhost:8000/docs
2. **Запустите демонстрацию**: `python run_demo.py`
3. **Настройте интеграции** с вашими облачными провайдерами
4. **Добавьте пользователей** и настройте права доступа
5. **Настройте уведомления** (Slack, Telegram, Email)

---

**Успешной установки! 🚀**
