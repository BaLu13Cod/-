#!/usr/bin/env python3
"""
Конфигурация Cloud Security System
Настройки для всех модулей системы
"""

import os
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class MLConfig:
    """Конфигурация машинного обучения"""
    auto_optimization: bool = True
    rl_training_steps: int = 10000
    ga_population_size: int = 100
    ga_mutation_rate: float = 0.1
    ga_crossover_rate: float = 0.8
    model_save_path: str = "models/"
    results_save_path: str = "results/"

@dataclass
class QuantumCryptoConfig:
    """Конфигурация квантового шифрования"""
    default_algorithm: str = "lattice"
    lwe_dimension: int = 256
    lwe_modulus: int = 7681
    lwe_std_dev: float = 3.2
    multivariate_variables: int = 64
    multivariate_equations: int = 80
    hash_tree_height: int = 20

@dataclass
class BlockchainConfig:
    """Конфигурация блокчейн-логгирования"""
    max_events_per_block: int = 100
    difficulty: int = 4
    blockchain_file: str = "security_blockchain.json"
    db_path: str = "security_events.db"
    backup_path: str = "backup/"

@dataclass
class AIConfig:
    """Конфигурация AI ассистента"""
    voice_enabled: bool = True
    chat_enabled: bool = True
    language: str = "ru-RU"
    voice_rate: int = 150
    voice_volume: float = 0.8
    openai_api_key: str = ""
    max_conversation_history: int = 50

@dataclass
class CloudConfig:
    """Конфигурация облачных интеграций"""
    aws_access_key: str = ""
    aws_secret_key: str = ""
    azure_subscription_id: str = ""
    gcp_project_id: str = ""
    kubernetes_config_path: str = ""
    docker_socket: str = "unix://var/run/docker.sock"
    connection_timeout: int = 30
    retry_attempts: int = 3

@dataclass
class SecurityConfig:
    """Конфигурация безопасности"""
    encryption_algorithm: str = "AES-256"
    hash_function: str = "SHA-256"
    jwt_secret: str = ""
    jwt_expiration: int = 3600
    mfa_enabled: bool = True
    audit_logging: bool = True

@dataclass
class SystemConfig:
    """Общая конфигурация системы"""
    log_level: str = "INFO"
    log_file: str = "cloud_security.log"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug_mode: bool = False
    max_workers: int = 4
    data_dir: str = "data/"
    temp_dir: str = "temp/"

class Config:
    """Основной класс конфигурации"""
    
    def __init__(self):
        # Загрузка переменных окружения
        self._load_environment()
        
        # Инициализация конфигураций
        self.ml = MLConfig()
        self.quantum_crypto = QuantumCryptoConfig()
        self.blockchain = BlockchainConfig()
        self.ai = AIConfig()
        self.cloud = CloudConfig()
        self.security = SecurityConfig()
        self.system = SystemConfig()
        
        # Применение переменных окружения
        self._apply_environment()
    
    def _load_environment(self):
        """Загрузка переменных окружения"""
        # Попытка загрузки из .env файла
        env_file = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(env_file):
            try:
                from dotenv import load_dotenv
                load_dotenv(env_file)
            except ImportError:
                pass
    
    def _apply_environment(self):
        """Применение переменных окружения к конфигурации"""
        # ML конфигурация
        self.ml.auto_optimization = os.getenv('ML_AUTO_OPTIMIZATION', 'true').lower() == 'true'
        self.ml.rl_training_steps = int(os.getenv('RL_TRAINING_STEPS', '10000'))
        self.ml.ga_population_size = int(os.getenv('GA_POPULATION_SIZE', '100'))
        
        # Квантовое шифрование
        self.quantum_crypto.default_algorithm = os.getenv('QUANTUM_CRYPTO_ALGORITHM', 'lattice')
        
        # Блокчейн
        self.blockchain.max_events_per_block = int(os.getenv('MAX_EVENTS_PER_BLOCK', '100'))
        self.blockchain.difficulty = int(os.getenv('BLOCKCHAIN_DIFFICULTY', '4'))
        
        # AI ассистент
        self.ai.voice_enabled = os.getenv('VOICE_ENABLED', 'true').lower() == 'true'
        self.ai.chat_enabled = os.getenv('CHAT_ENABLED', 'true').lower() == 'true'
        self.ai.openai_api_key = os.getenv('OPENAI_API_KEY', '')
        
        # Облачные интеграции
        self.cloud.aws_access_key = os.getenv('AWS_ACCESS_KEY', '')
        self.cloud.aws_secret_key = os.getenv('AWS_SECRET_KEY', '')
        self.cloud.azure_subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID', '')
        self.cloud.gcp_project_id = os.getenv('GCP_PROJECT_ID', '')
        
        # Безопасность
        self.security.jwt_secret = os.getenv('JWT_SECRET', '')
        self.security.mfa_enabled = os.getenv('MFA_ENABLED', 'true').lower() == 'true'
        
        # Система
        self.system.log_level = os.getenv('LOG_LEVEL', 'INFO')
        self.system.debug_mode = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
    
    def get_database_url(self) -> str:
        """Получение URL базы данных"""
        db_type = os.getenv('DATABASE_TYPE', 'sqlite')
        
        if db_type == 'postgresql':
            host = os.getenv('DB_HOST', 'localhost')
            port = os.getenv('DB_PORT', '5432')
            name = os.getenv('DB_NAME', 'cloud_security')
            user = os.getenv('DB_USER', 'postgres')
            password = os.getenv('DB_PASSWORD', '')
            
            return f"postgresql://{user}:{password}@{host}:{port}/{name}"
        
        elif db_type == 'mysql':
            host = os.getenv('DB_HOST', 'localhost')
            port = os.getenv('DB_PORT', '3306')
            name = os.getenv('DB_NAME', 'cloud_security')
            user = os.getenv('DB_USER', 'root')
            password = os.getenv('DB_PASSWORD', '')
            
            return f"mysql://{user}:{password}@{host}:{port}/{name}"
        
        else:  # sqlite
            db_path = os.getenv('DB_PATH', 'cloud_security.db')
            return f"sqlite:///{db_path}"
    
    def get_redis_url(self) -> str:
        """Получение URL Redis"""
        host = os.getenv('REDIS_HOST', 'localhost')
        port = os.getenv('REDIS_PORT', '6379')
        password = os.getenv('REDIS_PASSWORD', '')
        db = os.getenv('REDIS_DB', '0')
        
        if password:
            return f"redis://:{password}@{host}:{port}/{db}"
        else:
            return f"redis://{host}:{port}/{db}"
    
    def get_cloud_credentials(self, provider: str) -> Dict[str, Any]:
        """Получение учетных данных облачного провайдера"""
        if provider.lower() == 'aws':
            return {
                'access_key': self.cloud.aws_access_key,
                'secret_key': self.cloud.aws_secret_key
            }
        elif provider.lower() == 'azure':
            return {
                'subscription_id': self.cloud.azure_subscription_id
            }
        elif provider.lower() == 'gcp':
            return {
                'project_id': self.cloud.gcp_project_id
            }
        else:
            return {}
    
    def validate(self) -> bool:
        """Валидация конфигурации"""
        errors = []
        
        # Проверка обязательных параметров
        if not self.cloud.aws_access_key and not self.cloud.azure_subscription_id and not self.cloud.gcp_project_id:
            errors.append("Необходимо указать учетные данные хотя бы для одного облачного провайдера")
        
        if not self.security.jwt_secret:
            errors.append("JWT_SECRET не указан")
        
        # Проверка путей
        paths_to_check = [
            self.ml.model_save_path,
            self.ml.results_save_path,
            self.blockchain.backup_path,
            self.system.data_dir,
            self.system.temp_dir
        ]
        
        for path in paths_to_check:
            if not os.path.exists(path):
                try:
                    os.makedirs(path, exist_ok=True)
                except Exception as e:
                    errors.append(f"Не удается создать директорию {path}: {e}")
        
        if errors:
            for error in errors:
                print(f"❌ Ошибка конфигурации: {error}")
            return False
        
        return True
    
    def print_summary(self):
        """Вывод сводки конфигурации"""
        print("🔧 Конфигурация Cloud Security System")
        print("=" * 50)
        
        print(f"🧠 ML: автооптимизация = {self.ml.auto_optimization}, "
              f"RL шаги = {self.ml.rl_training_steps}")
        
        print(f"🔐 Квантовое шифрование: алгоритм = {self.quantum_crypto.default_algorithm}")
        
        print(f"⛓️ Блокчейн: события/блок = {self.blockchain.max_events_per_block}, "
              f"сложность = {self.blockchain.difficulty}")
        
        print(f"🤖 AI: голос = {self.ai.voice_enabled}, чат = {self.ai.chat_enabled}")
        
        cloud_providers = []
        if self.cloud.aws_access_key:
            cloud_providers.append("AWS")
        if self.cloud.azure_subscription_id:
            cloud_providers.append("Azure")
        if self.cloud.gcp_project_id:
            cloud_providers.append("GCP")
        
        print(f"☁️ Облачные провайдеры: {', '.join(cloud_providers) if cloud_providers else 'не настроены'}")
        
        print(f"🛡️ Безопасность: MFA = {self.security.mfa_enabled}, аудит = {self.security.audit_logging}")
        
        print(f"⚙️ Система: логирование = {self.system.log_level}, отладка = {self.system.debug_mode}")
        print("=" * 50)

# Создание глобального экземпляра конфигурации
config = Config()

# Экспорт для обратной совместимости
LOG_LEVEL = config.system.log_level
LOG_FILE = config.system.log_file
AWS_ACCESS_KEY = config.cloud.aws_access_key
AWS_SECRET_KEY = config.cloud.aws_secret_key
AZURE_SUBSCRIPTION_ID = config.cloud.azure_subscription_id
GCP_PROJECT_ID = config.cloud.gcp_project_id

if __name__ == "__main__":
    # Вывод сводки конфигурации
    config.print_summary()
    
    # Валидация
    if config.validate():
        print("✅ Конфигурация валидна")
    else:
        print("❌ Конфигурация содержит ошибки")
        exit(1)
