#!/usr/bin/env python3
"""
Демонстрация расширенных возможностей Cloud Security System
Показывает работу Advanced ML, Quantum Crypto, Blockchain Logger, AI Assistant и Cloud Integrations
"""

import asyncio
import logging
import time
import numpy as np
from pathlib import Path
import sys

# Добавление корневой директории в путь
sys.path.append(str(Path(__file__).parent))

from core.advanced_ml_system import AdvancedMLSystem
from core.quantum_crypto import QuantumResistantCrypto
from core.blockchain_logger import BlockchainLogger, SecurityEventLogger
from core.ai_assistant import AIAssistant
from core.cloud_integrations import CloudIntegrationManager, CloudProvider

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class AdvancedFeaturesDemo:
    """Демонстрация расширенных возможностей системы"""
    
    def __init__(self):
        self.ml_system = AdvancedMLSystem()
        self.quantum_crypto = QuantumResistantCrypto()
        self.blockchain_logger = BlockchainLogger()
        self.security_logger = SecurityEventLogger(self.blockchain_logger)
        self.ai_assistant = AIAssistant()
        self.cloud_manager = CloudIntegrationManager()
        
    async def run_demo(self):
        """Запуск полной демонстрации"""
        try:
            logger.info("🚀 Запуск демонстрации расширенных возможностей Cloud Security System")
            logger.info("=" * 80)
            
            # Демонстрация Advanced ML
            await self._demo_advanced_ml()
            
            # Демонстрация квантового шифрования
            await self._demo_quantum_crypto()
            
            # Демонстрация блокчейн-логгирования
            await self._demo_blockchain_logger()
            
            # Демонстрация AI ассистента
            await self._demo_ai_assistant()
            
            # Демонстрация облачных интеграций
            await self._demo_cloud_integrations()
            
            # Демонстрация интеграции всех компонентов
            await self._demo_integration()
            
            logger.info("=" * 80)
            logger.info("✅ Демонстрация завершена успешно!")
            
        except Exception as e:
            logger.error(f"❌ Ошибка в демонстрации: {e}")
            raise
    
    async def _demo_advanced_ml(self):
        """Демонстрация расширенной ML системы"""
        logger.info("🧠 Демонстрация Advanced ML System")
        logger.info("-" * 50)
        
        try:
            # Инициализация ML системы
            await self.ml_system.initialize()
            logger.info("✅ ML система инициализирована")
            
            # Создание демонстрационных данных
            X = np.random.random((100, 10))  # 100 образцов, 10 признаков
            y = np.random.randint(0, 3, 100)  # 3 класса угроз
            
            # Обучение модели глубокого обучения
            logger.info("🔄 Обучение модели глубокого обучения...")
            await self.ml_system.train_deep_learning_model('threat_classifier', X, y)
            
            # Обучение агента RL
            logger.info("🔄 Обучение агента обучения с подкреплением...")
            await self.ml_system.train_reinforcement_agent('security_agent', timesteps=1000)
            
            # Эволюция генетического алгоритма
            logger.info("🔄 Запуск эволюции генетического алгоритма...")
            best_strategy, best_fitness = await self.ml_system.evolve_genetic_algorithm(
                chromosome_length=30, generations=20
            )
            logger.info(f"🎯 Лучшая стратегия: приспособленность = {best_fitness:.4f}")
            
            # Предсказание угрозы
            logger.info("🔮 Тестирование предсказания угроз...")
            test_features = np.random.random(10)
            threat_analysis = await self.ml_system.predict_threat(test_features)
            logger.info(f"📊 Анализ угрозы: {threat_analysis}")
            
            # Статус системы
            status = self.ml_system.get_system_status()
            logger.info(f"📈 Статус ML системы: {len(status['deep_learning_models'])} моделей, "
                       f"{len(status['rl_agents'])} агентов")
            
        except Exception as e:
            logger.error(f"❌ Ошибка в демонстрации ML: {e}")
    
    async def _demo_quantum_crypto(self):
        """Демонстрация квантово-устойчивого шифрования"""
        logger.info("🔐 Демонстрация Quantum-Resistant Cryptography")
        logger.info("-" * 50)
        
        try:
            # Информация об алгоритмах
            algorithms = self.quantum_crypto.get_supported_algorithms()
            logger.info(f"🔑 Поддерживаемые алгоритмы: {algorithms}")
            
            for algorithm in algorithms:
                info = self.quantum_crypto.get_algorithm_info(algorithm)
                logger.info(f"📋 {algorithm}: {info['name']} - {info['security_level']}")
            
            # Тестирование LWE шифрования
            logger.info("🔄 Тестирование LWE шифрования...")
            private_key, public_key = self.quantum_crypto.generate_keypair("lattice")
            message = "Секретное сообщение для тестирования LWE".encode('utf-8')
            
            ciphertext = self.quantum_crypto.encrypt(message, public_key, "lattice")
            decrypted = self.quantum_crypto.decrypt(ciphertext, private_key, "lattice")
            
            success = message == decrypted
            logger.info(f"🔒 LWE шифрование: {'✅' if success else '❌'}")
            
            # Тестирование Multivariate шифрования
            logger.info("🔄 Тестирование Multivariate шифрования...")
            private_key, public_key = self.quantum_crypto.generate_keypair("multivariate")
            message = "Тест Multivariate шифрования".encode('utf-8')
            
            ciphertext = self.quantum_crypto.encrypt(message, public_key, "multivariate")
            decrypted = self.quantum_crypto.decrypt(ciphertext, private_key, "multivariate")
            
            success = message == decrypted
            logger.info(f"🔒 Multivariate шифрование: {'✅' if success else '❌'}")
            
            # Тестирование Hash-based подписей
            logger.info("🔄 Тестирование Hash-based подписей...")
            private_keys, root_hash = self.quantum_crypto.generate_keypair("hash")
            message = "Сообщение для подписи".encode('utf-8')
            
            signature = self.quantum_crypto.sign(message, 0)
            verified = self.quantum_crypto.verify(message, signature, root_hash)
            
            logger.info(f"🔒 Hash-based подписи: {'✅' if verified else '❌'}")
            
            # Бенчмарк производительности
            logger.info("⏱️ Тестирование производительности алгоритмов...")
            benchmark_results = self.quantum_crypto.benchmark_algorithms()
            
            for algorithm, results in benchmark_results.items():
                logger.info(f"📊 {algorithm}: генерация ключей = {results['key_generation']:.4f}с, "
                           f"шифрование = {results['encryption']:.4f}с")
            
        except Exception as e:
            logger.error(f"❌ Ошибка в демонстрации квантового шифрования: {e}")
    
    async def _demo_blockchain_logger(self):
        """Демонстрация блокчейн-логгирования"""
        logger.info("⛓️ Демонстрация Blockchain Logger")
        logger.info("-" * 50)
        
        try:
            # Логгирование различных типов событий
            logger.info("📝 Логгирование событий безопасности...")
            
            # Угроза
            await self.security_logger.log_threat_detected(
                threat_type="malware_detection",
                source_ip="192.168.1.100",
                target_ip="10.0.0.1",
                confidence=0.95,
                details={"malware_type": "ransomware", "file_hash": "abc123def456"}
            )
            
            # Инцидент
            await self.security_logger.log_security_incident(
                incident_type="data_breach",
                affected_system="database_server",
                description="Обнаружена попытка несанкционированного доступа к БД",
                impact_level="high",
                response_actions=["block_ip", "isolate_system", "notify_admin"]
            )
            
            # Попытка доступа
            await self.security_logger.log_access_attempt(
                user_id="admin",
                resource="admin_panel",
                access_type="login",
                success=False,
                ip_address="203.0.113.45"
            )
            
            # Системное событие
            await self.security_logger.log_system_event(
                event_type="system_startup",
                component="security_monitor",
                message="Система мониторинга безопасности запущена",
                severity="INFO"
            )
            
            # Пауза для обработки событий
            await asyncio.sleep(2)
            
            # Проверка статуса блокчейна
            status = self.blockchain_logger.get_chain_status()
            logger.info(f"📊 Статус блокчейна: {status['chain_length']} блоков, "
                       f"{status['pending_events']} событий в ожидании")
            
            # Проверка целостности
            integrity = self.blockchain_logger.verify_chain_integrity()
            logger.info(f"🔍 Целостность блокчейна: {'✅' if integrity['valid'] else '❌'}")
            
            if not integrity['valid']:
                logger.warning(f"⚠️ Ошибки в блокчейне: {integrity['errors']}")
            
            # Получение событий по типу
            threat_events = self.blockchain_logger.get_events_by_type("threat_detected", limit=5)
            logger.info(f"📋 События угроз: {len(threat_events)} найдено")
            
            # Экспорт блокчейна
            export_path = f"demo_blockchain_export_{int(time.time())}.json"
            self.blockchain_logger.export_chain(export_path)
            logger.info(f"💾 Блокчейн экспортирован в {export_path}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка в демонстрации блокчейн-логгера: {e}")
    
    async def _demo_ai_assistant(self):
        """Демонстрация AI ассистента"""
        logger.info("🤖 Демонстрация AI Assistant")
        logger.info("-" * 50)
        
        try:
            # Запуск AI ассистента
            await self.ai_assistant.start()
            logger.info("✅ AI ассистент запущен")
            
            # Установка пользователя
            self.ai_assistant.set_user("demo_user")
            logger.info("👤 Пользователь установлен: demo_user")
            
            # Тестирование чат-бота
            logger.info("💬 Тестирование чат-бота...")
            
            test_messages = [
                "Проверить статус системы",
                "Обнаружена угроза",
                "Сгенерировать отчет",
                "Помощь"
            ]
            
            for message in test_messages:
                response = await self.ai_assistant.process_text_message("demo_user", message)
                logger.info(f"💭 Вопрос: {message}")
                logger.info(f"🤖 Ответ: {response[:100]}...")
                await asyncio.sleep(1)
            
            # Тестирование голосовых команд
            logger.info("🎤 Тестирование голосовых команд...")
            logger.info("💡 Скажите: 'Проверить статус' или 'Помощь'")
            
            # Пауза для голосовых команд
            await asyncio.sleep(5)
            
            # Статус ассистента
            status = self.ai_assistant.get_status()
            logger.info(f"📊 Статус AI ассистента: голос = {'✅' if status['voice_enabled'] else '❌'}, "
                       f"чат = {'✅' if status['chat_enabled'] else '❌'}")
            
            # Экстренное оповещение
            logger.info("🚨 Тестирование экстренного оповещения...")
            await self.ai_assistant.emergency_alert("Тестовое экстренное оповещение")
            
        except Exception as e:
            logger.error(f"❌ Ошибка в демонстрации AI ассистента: {e}")
    
    async def _demo_cloud_integrations(self):
        """Демонстрация облачных интеграций"""
        logger.info("☁️ Демонстрация Cloud Integrations")
        logger.info("-" * 50)
        
        try:
            # Создание демонстрационных провайдеров
            logger.info("🔧 Создание демонстрационных облачных провайдеров...")
            
            # Docker провайдер (локальный)
            docker_provider = CloudProvider(
                name="Local_Docker",
                type="docker",
                credentials={},
                regions=["local"],
                services=["containers", "images", "networks"]
            )
            
            # Kubernetes провайдер (если доступен)
            k8s_provider = CloudProvider(
                name="Demo_K8s",
                type="kubernetes",
                credentials={},
                regions=["cluster"],
                services=["pods", "services", "deployments"]
            )
            
            # Добавление провайдеров
            await self.cloud_manager.add_provider(docker_provider)
            logger.info("✅ Docker провайдер добавлен")
            
            try:
                await self.cloud_manager.add_provider(k8s_provider)
                logger.info("✅ Kubernetes провайдер добавлен")
            except Exception as e:
                logger.warning(f"⚠️ Kubernetes провайдер недоступен: {e}")
            
            # Получение статуса всех провайдеров
            logger.info("📊 Получение статуса облачных сервисов...")
            cloud_status = await self.cloud_manager.get_all_security_status()
            
            for provider_name, status in cloud_status['providers'].items():
                if 'error' not in status:
                    logger.info(f"☁️ {provider_name}: активен")
                else:
                    logger.warning(f"⚠️ {provider_name}: ошибка - {status['error']}")
            
            # Получение списка инстансов
            logger.info("📋 Получение списка инстансов...")
            instances = await self.cloud_manager.get_all_instances()
            
            total_instances = sum(len(inst_list) for inst_list in instances.values())
            logger.info(f"📊 Всего инстансов: {total_instances}")
            
            for provider, inst_list in instances.items():
                if inst_list:
                    logger.info(f"☁️ {provider}: {len(inst_list)} инстансов")
            
            # Тестирование блокировки IP
            logger.info("🚫 Тестирование блокировки IP...")
            test_ip = "203.0.113.100"
            block_results = await self.cloud_manager.block_ip_across_providers(
                test_ip, "Демонстрационная блокировка"
            )
            
            for provider, success in block_results.items():
                status = "✅" if success else "❌"
                logger.info(f"🚫 {provider}: блокировка IP {test_ip} - {status}")
            
            # Список провайдеров
            providers = self.cloud_manager.list_providers()
            logger.info(f"📋 Доступные провайдеры: {providers}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка в демонстрации облачных интеграций: {e}")
    
    async def _demo_integration(self):
        """Демонстрация интеграции всех компонентов"""
        logger.info("🔗 Демонстрация интеграции всех компонентов")
        logger.info("-" * 50)
        
        try:
            # Симуляция комплексного сценария безопасности
            logger.info("🎭 Симуляция комплексного сценария безопасности...")
            
            # 1. Обнаружение угрозы через ML
            logger.info("1️⃣ Обнаружение угрозы через ML...")
            threat_features = np.random.random(10)
            threat_analysis = await self.ml_system.predict_threat(threat_features)
            
            if threat_analysis.get('is_anomaly', False):
                logger.info("🚨 ML система обнаружила аномалию!")
                
                # 2. Логгирование в блокчейн
                logger.info("2️⃣ Логгирование в блокчейн...")
                await self.security_logger.log_threat_detected(
                    threat_type="ml_anomaly_detection",
                    source_ip="192.168.1.200",
                    target_ip="10.0.0.50",
                    confidence=threat_analysis.get('anomaly_score', 0.8),
                    details={
                        "ml_model": "anomaly_detector",
                        "prediction": threat_analysis,
                        "response_action": threat_analysis.get('recommended_action', 'monitor')
                    }
                )
                
                # 3. Уведомление AI ассистента
                logger.info("3️⃣ Уведомление AI ассистента...")
                await self.ai_assistant.emergency_alert(
                    f"ML система обнаружила аномалию! Рекомендуемое действие: {threat_analysis.get('recommended_action', 'unknown')}"
                )
                
                # 4. Автоматическая блокировка IP
                logger.info("4️⃣ Автоматическая блокировка IP...")
                block_results = await self.cloud_manager.block_ip_across_providers(
                    "192.168.1.200", "ML обнаруженная аномалия"
                )
                
                blocked_providers = [p for p, s in block_results.items() if s]
                if blocked_providers:
                    logger.info(f"✅ IP заблокирован в провайдерах: {blocked_providers}")
                
                # 5. Проверка целостности блокчейна
                logger.info("5️⃣ Проверка целостности блокчейна...")
                integrity = self.blockchain_logger.verify_chain_integrity()
                logger.info(f"🔍 Блокчейн валиден: {'✅' if integrity['valid'] else '❌'}")
                
                # 6. Генерация отчета
                logger.info("6️⃣ Генерация отчета...")
                await self.ai_assistant.process_text_message(
                    "demo_user", "Сгенерировать отчет по последним угрозам"
                )
                
                logger.info("🎯 Комплексный сценарий безопасности выполнен успешно!")
            
            else:
                logger.info("✅ Угроз не обнаружено, система работает нормально")
            
            # Финальная статистика
            logger.info("📊 Финальная статистика системы:")
            
            ml_status = self.ml_system.get_system_status()
            blockchain_status = self.blockchain_logger.get_chain_status()
            ai_status = self.ai_assistant.get_status()
            cloud_providers = self.cloud_manager.list_providers()
            
            logger.info(f"🧠 ML модели: {len(ml_status['deep_learning_models'])}")
            logger.info(f"⛓️ Блокчейн: {blockchain_status['chain_length']} блоков")
            logger.info(f"🤖 AI ассистент: {'активен' if ai_status['is_active'] else 'неактивен'}")
            logger.info(f"☁️ Облачные провайдеры: {len(cloud_providers)}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка в демонстрации интеграции: {e}")
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            logger.info("🧹 Очистка ресурсов...")
            
            # Остановка AI ассистента
            await self.ai_assistant.stop()
            
            # Очистка облачных интеграций
            await self.cloud_manager.cleanup()
            
            # Очистка блокчейн логгера
            self.blockchain_logger.cleanup()
            
            logger.info("✅ Ресурсы очищены")
            
        except Exception as e:
            logger.error(f"❌ Ошибка при очистке: {e}")

async def main():
    """Главная функция демонстрации"""
    demo = AdvancedFeaturesDemo()
    
    try:
        await demo.run_demo()
    finally:
        await demo.cleanup()

if __name__ == "__main__":
    try:
        print("🚀 Запуск демонстрации расширенных возможностей Cloud Security System")
        print("=" * 80)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️ Демонстрация прервана пользователем")
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        sys.exit(1)
