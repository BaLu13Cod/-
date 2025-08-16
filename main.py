#!/usr/bin/env python3
"""
Cloud Security System - Главный файл запуска
Система защиты облачных сред с эволюционным обучением
"""

import asyncio
import logging
import signal
import sys
from pathlib import Path
import time

# Добавление корневой директории в путь
sys.path.append(str(Path(__file__).parent))

from core.security_monitor import SecurityMonitor, SecurityEvent, ThreatLevel
from core.integration_manager import IntegrationConfig, IntegrationType
from core.advanced_ml_system import AdvancedMLSystem
from core.quantum_crypto import QuantumResistantCrypto
from core.blockchain_logger import BlockchainLogger, SecurityEventLogger
from core.ai_assistant import AIAssistant
from core.cloud_integrations import CloudIntegrationManager, CloudProvider
from config import config

# Настройка логирования
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cloud_security.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class CloudSecuritySystem:
    """Основной класс системы безопасности"""
    
    def __init__(self):
        self.monitor = SecurityMonitor()
        self.advanced_ml = AdvancedMLSystem()
        self.quantum_crypto = QuantumResistantCrypto()
        self.blockchain_logger = BlockchainLogger()
        self.security_logger = SecurityEventLogger(self.blockchain_logger)
        self.ai_assistant = AIAssistant()
        self.cloud_manager = CloudIntegrationManager()
        
        self.running = False
        self.tasks = []
        
        # Настройка обработчиков сигналов
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Обработчик сигналов для корректного завершения"""
        logger.info(f"Получен сигнал {signum}, завершение работы...")
        self.running = False
    
    async def initialize(self):
        """Инициализация системы"""
        try:
            logger.info("Инициализация Cloud Security System...")
            
            # Инициализация монитора безопасности
            await self.monitor.initialize()
            
            # Инициализация расширенной ML системы
            await self.advanced_ml.initialize()
            
            # Инициализация AI ассистента
            await self.ai_assistant.start()
            
            # Настройка облачных интеграций
            await self._setup_cloud_integrations()
            
            # Добавление обработчика событий
            self.monitor.add_event_handler(self._security_event_handler)
            
            # Настройка базовых интеграций
            await self._setup_default_integrations()
            
            logger.info("Cloud Security System инициализирована успешно")
            return True
            
        except Exception as e:
            logger.error(f"Ошибка инициализации: {e}")
            return False
    
    async def _setup_cloud_integrations(self):
        """Настройка облачных интеграций"""
        try:
            # AWS интеграция (пример)
            aws_provider = CloudProvider(
                name="AWS_Production",
                type="aws",
                credentials={
                    "access_key": config.AWS_ACCESS_KEY,
                    "secret_key": config.AWS_SECRET_KEY
                },
                regions=["us-east-1", "us-west-2"],
                services=["ec2", "s3", "lambda", "guardduty", "securityhub"]
            )
            await self.cloud_manager.add_provider(aws_provider)
            
            # Azure интеграция (пример)
            azure_provider = CloudProvider(
                name="Azure_Production",
                type="azure",
                credentials={
                    "subscription_id": config.AZURE_SUBSCRIPTION_ID
                },
                regions=["eastus", "westus2"],
                services=["compute", "network", "security", "monitor"]
            )
            await self.cloud_manager.add_provider(azure_provider)
            
            # Kubernetes интеграция
            k8s_provider = CloudProvider(
                name="K8s_Cluster",
                type="kubernetes",
                credentials={},
                regions=["cluster"],
                services=["pods", "services", "deployments"]
            )
            await self.cloud_manager.add_provider(k8s_provider)
            
            # Docker интеграция
            docker_provider = CloudProvider(
                name="Local_Docker",
                type="docker",
                credentials={},
                regions=["local"],
                services=["containers", "images", "networks"]
            )
            await self.cloud_manager.add_provider(docker_provider)
            
            logger.info("Облачные интеграции настроены")
            
        except Exception as e:
            logger.error(f"Ошибка настройки облачных интеграций: {e}")
    
    async def _setup_default_integrations(self):
        """Настройка базовых интеграций"""
        try:
            # Интеграция с AWS (пример)
            aws_config = IntegrationConfig(
                name="AWS_Production",
                type=IntegrationType.CLOUD,
                endpoint_url="https://ec2.amazonaws.com",
                credentials={"region": "us-east-1"}
            )
            await self.monitor.add_integration(aws_config)
            
            # Интеграция с Azure (пример)
            azure_config = IntegrationConfig(
                name="Azure_Production",
                type=IntegrationType.CLOUD,
                endpoint_url="https://management.azure.com",
                credentials={"subscription_id": "example"}
            )
            await self.monitor.add_integration(azure_config)
            
            # Интеграция с локальным устройством (пример)
            device_config = IntegrationConfig(
                name="Local_Network_Device",
                type=IntegrationType.DEVICE,
                endpoint_url="http://192.168.1.100:8080",
                polling_interval=30
            )
            await self.monitor.add_integration(device_config)
            
            logger.info("Базовые интеграции настроены")
            
        except Exception as e:
            logger.error(f"Ошибка настройки базовых интеграций: {e}")
    
    async def _security_event_handler(self, event: SecurityEvent):
        """Обработчик событий безопасности"""
        try:
            logger.info(f"Обработка события безопасности: {event.event_type}")
            
            # Логгирование в блокчейн
            await self.security_logger.log_threat_detected(
                threat_type=event.event_type,
                source_ip=event.source,
                target_ip="local",
                confidence=0.8,
                details={
                    "description": event.description,
                    "severity": event.severity,
                    "timestamp": event.timestamp
                }
            )
            
            # Анализ с помощью ML
            if hasattr(event, 'features'):
                threat_analysis = await self.advanced_ml.predict_threat(event.features)
                logger.info(f"ML анализ угрозы: {threat_analysis}")
            
            # Уведомление AI ассистента
            if event.severity in [ThreatLevel.HIGH, ThreatLevel.CRITICAL]:
                await self.ai_assistant.emergency_alert(
                    f"Обнаружена критическая угроза: {event.description}"
                )
            
            # Автоматическая блокировка IP если необходимо
            if event.severity == ThreatLevel.CRITICAL and hasattr(event, 'source'):
                await self.cloud_manager.block_ip_across_providers(
                    event.source,
                    f"Critical threat: {event.description}"
                )
                
        except Exception as e:
            logger.error(f"Ошибка обработки события безопасности: {e}")
    
    async def start_monitoring(self):
        """Запуск мониторинга"""
        try:
            logger.info("Запуск мониторинга безопасности...")
            
            # Запуск мониторинга
            await self.monitor.start_monitoring()
            
            # Запуск фоновых задач
            self.tasks.append(asyncio.create_task(self._ml_optimization_loop()))
            self.tasks.append(asyncio.create_task(self._blockchain_maintenance_loop()))
            self.tasks.append(asyncio.create_task(self._cloud_status_loop()))
            
            logger.info("Мониторинг запущен")
            
        except Exception as e:
            logger.error(f"Ошибка запуска мониторинга: {e}")
    
    async def _ml_optimization_loop(self):
        """Цикл оптимизации ML моделей"""
        while self.running:
            try:
                await asyncio.sleep(3600)  # Каждый час
                
                logger.info("Запуск автоматической оптимизации ML моделей...")
                await self.advanced_ml.auto_optimize_models()
                
                # Эволюция генетического алгоритма
                await self.advanced_ml.evolve_genetic_algorithm()
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Ошибка в цикле оптимизации ML: {e}")
                await asyncio.sleep(300)  # Пауза 5 минут при ошибке
    
    async def _blockchain_maintenance_loop(self):
        """Цикл обслуживания блокчейна"""
        while self.running:
            try:
                await asyncio.sleep(1800)  # Каждые 30 минут
                
                logger.info("Проверка целостности блокчейна...")
                integrity_status = self.blockchain_logger.verify_chain_integrity()
                
                if not integrity_status['valid']:
                    logger.warning(f"Обнаружены проблемы в блокчейне: {integrity_status['errors']}")
                
                # Экспорт блокчейна для резервного копирования
                if integrity_status['valid']:
                    self.blockchain_logger.export_chain(
                        f"backup/blockchain_backup_{int(time.time())}.json"
                    )
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Ошибка в цикле обслуживания блокчейна: {e}")
                await asyncio.sleep(300)
    
    async def _cloud_status_loop(self):
        """Цикл проверки статуса облачных сервисов"""
        while self.running:
            try:
                await asyncio.sleep(900)  # Каждые 15 минут
                
                logger.info("Проверка статуса облачных сервисов...")
                cloud_status = await self.cloud_manager.get_all_security_status()
                
                # Логгирование статуса
                await self.security_logger.log_system_event(
                    "cloud_status_check",
                    "cloud_manager",
                    f"Статус облачных сервисов: {len(cloud_status['providers'])} провайдеров активны"
                )
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Ошибка в цикле проверки облачных сервисов: {e}")
                await asyncio.sleep(300)
    
    async def run(self):
        """Основной цикл работы системы"""
        try:
            self.running = True
            
            # Запуск мониторинга
            await self.start_monitoring()
            
            # Основной цикл
            while self.running:
                await asyncio.sleep(1)
                
        except KeyboardInterrupt:
            logger.info("Получен сигнал прерывания")
        except Exception as e:
            logger.error(f"Критическая ошибка в основном цикле: {e}")
        finally:
            await self.cleanup()
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            logger.info("Очистка ресурсов системы...")
            
            # Остановка мониторинга
            if hasattr(self.monitor, 'stop_monitoring'):
                await self.monitor.stop_monitoring()
            
            # Остановка AI ассистента
            await self.ai_assistant.stop()
            
            # Очистка облачных интеграций
            await self.cloud_manager.cleanup()
            
            # Очистка блокчейн логгера
            self.blockchain_logger.cleanup()
            
            # Отмена всех задач
            for task in self.tasks:
                if not task.done():
                    task.cancel()
            
            # Ожидание завершения задач
            if self.tasks:
                await asyncio.gather(*self.tasks, return_exceptions=True)
            
            logger.info("Система остановлена корректно")
            
        except Exception as e:
            logger.error(f"Ошибка при очистке ресурсов: {e}")
    
    def get_system_status(self) -> dict:
        """Получение статуса системы"""
        return {
            'running': self.running,
            'monitor_status': self.monitor.get_status() if hasattr(self.monitor, 'get_status') else 'unknown',
            'ml_status': self.advanced_ml.get_system_status(),
            'blockchain_status': self.blockchain_logger.get_chain_status(),
            'ai_assistant_status': self.ai_assistant.get_status(),
            'cloud_providers': self.cloud_manager.list_providers(),
            'active_tasks': len([t for t in self.tasks if not t.done()])
        }

async def main():
    """Главная функция"""
    try:
        # Создание и инициализация системы
        system = CloudSecuritySystem()
        
        # Инициализация
        if not await system.initialize():
            logger.error("Не удалось инициализировать систему")
            return 1
        
        # Запуск системы
        await system.run()
        
        return 0
        
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        return 1

if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        logger.info("Программа прервана пользователем")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")
        sys.exit(1)
