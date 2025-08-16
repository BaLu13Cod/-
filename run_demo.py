#!/usr/bin/env python3
"""
Демонстрационный скрипт для Cloud Security System
Показывает основные возможности системы на примерах
"""

import asyncio
import requests
import json
import time
from datetime import datetime
import sys
import os

# Добавление корневой директории в путь
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.security_monitor import SecurityMonitor, SecurityEvent, ThreatLevel
from core.integration_manager import IntegrationConfig, IntegrationType

class SecuritySystemDemo:
    """Демонстрация системы безопасности"""
    
    def __init__(self):
        self.api_base_url = "http://localhost:8000"
        self.monitor = SecurityMonitor()
        self.demo_incidents = []
        
    async def initialize(self):
        """Инициализация демонстрации"""
        print("🚀 Инициализация Cloud Security System...")
        
        try:
            await self.monitor.initialize()
            print("✅ Система инициализирована успешно")
            return True
        except Exception as e:
            print(f"❌ Ошибка инициализации: {e}")
            return False
    
    def check_api_status(self):
        """Проверка статуса API"""
        try:
            response = requests.get(f"{self.api_base_url}/health")
            if response.status_code == 200:
                print("✅ API сервер доступен")
                return True
            else:
                print(f"⚠️ API сервер недоступен: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ API сервер не запущен")
            return False
    
    async def demo_threat_database(self):
        """Демонстрация базы данных угроз"""
        print("\n📊 Демонстрация базы данных угроз")
        print("=" * 50)
        
        # Получение всех угроз
        try:
            response = requests.get(f"{self.api_base_url}/threats")
            if response.status_code == 200:
                threats = response.json()
                print(f"📈 Всего угроз в базе: {len(threats)}")
                
                # Показ угроз по категориям
                categories = {}
                for threat in threats:
                    category = threat['category']
                    if category not in categories:
                        categories[category] = []
                    categories[category].append(threat['name'])
                
                for category, threat_names in categories.items():
                    print(f"\n🔍 {category}:")
                    for name in threat_names[:3]:  # Показываем первые 3
                        print(f"   • {name}")
                    if len(threat_names) > 3:
                        print(f"   ... и еще {len(threat_names) - 3}")
                
                # Поиск конкретной угрозы
                print(f"\n🔍 Поиск угрозы 'WannaCry':")
                search_response = requests.get(f"{self.api_base_url}/threats?search=WannaCry")
                if search_response.status_code == 200:
                    search_results = search_response.json()
                    for threat in search_results:
                        print(f"   • {threat['name']} - {threat['severity']}")
                        print(f"     {threat['description']}")
                
            else:
                print(f"⚠️ Не удалось получить угрозы: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Ошибка демонстрации базы угроз: {e}")
    
    async def demo_security_events(self):
        """Демонстрация событий безопасности"""
        print("\n🚨 Демонстрация событий безопасности")
        print("=" * 50)
        
        # Создание демонстрационных событий
        demo_events = [
            {
                "source": "network_monitor",
                "event_type": "suspicious_connection",
                "severity": "HIGH",
                "description": "Подозрительное подключение к известному вредоносному IP",
                "data": {
                    "source_ip": "192.168.1.100",
                    "target_ip": "91.121.28.34",  # IP из базы угроз WannaCry
                    "source_host": "workstation-01",
                    "target_host": "unknown",
                    "connection_type": "outbound_tcp",
                    "port": 443
                }
            },
            {
                "source": "file_monitor",
                "event_type": "suspicious_file_creation",
                "severity": "CRITICAL",
                "description": "Создан файл с расширением .wncry",
                "data": {
                    "file_path": "/tmp/important_document.wncry",
                    "file_hash": "24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c",
                    "source_host": "workstation-02",
                    "process_name": "explorer.exe",
                    "user": "admin"
                }
            },
            {
                "source": "dns_monitor",
                "event_type": "suspicious_dns_query",
                "severity": "HIGH",
                "description": "DNS запрос к подозрительному домену",
                "data": {
                    "domain": "iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com",
                    "source_ip": "192.168.1.75",
                    "source_host": "workstation-03",
                    "query_type": "A",
                    "timestamp": datetime.now().isoformat()
                }
            },
            {
                "source": "system_monitor",
                "event_type": "high_cpu_usage",
                "severity": "MEDIUM",
                "description": "Обнаружена необычно высокая активность CPU",
                "data": {
                    "source_host": "workstation-04",
                    "cpu_usage": 95.5,
                    "process_name": "xmrig.exe",
                    "file_hash": "d4e5f6a7b8c9",
                    "network_connections": ["pool.minexmr.com:3333"],
                    "memory_usage": "2.1 GB"
                }
            }
        ]
        
        print("📝 Создание демонстрационных событий безопасности...")
        
        for i, event_data in enumerate(demo_events, 1):
            try:
                print(f"\n📋 Событие {i}: {event_data['event_type']}")
                print(f"   Источник: {event_data['source']}")
                print(f"   Уровень: {event_data['severity']}")
                print(f"   Описание: {event_data['description']}")
                
                # Отправка события через API
                response = requests.post(f"{self.api_base_url}/events", json=event_data)
                if response.status_code == 200:
                    result = response.json()
                    print(f"   ✅ Событие создано: {result.get('incident_id', 'N/A')}")
                else:
                    print(f"   ⚠️ Ошибка создания события: {response.status_code}")
                
                # Небольшая пауза между событиями
                await asyncio.sleep(1)
                
            except Exception as e:
                print(f"   ❌ Ошибка: {e}")
        
        print(f"\n📊 Всего создано событий: {len(demo_events)}")
    
    async def demo_integrations(self):
        """Демонстрация интеграций"""
        print("\n🔗 Демонстрация интеграций")
        print("=" * 50)
        
        # Создание демонстрационных интеграций
        demo_integrations = [
            {
                "name": "AWS_Production_Demo",
                "type": "cloud",
                "endpoint_url": "https://ec2.amazonaws.com",
                "credentials": {
                    "region": "us-east-1",
                    "access_key": "demo_access_key",
                    "secret_key": "demo_secret_key"
                }
            },
            {
                "name": "Azure_Production_Demo",
                "type": "cloud",
                "endpoint_url": "https://management.azure.com",
                "credentials": {
                    "subscription_id": "demo_subscription_id",
                    "tenant_id": "demo_tenant_id"
                }
            },
            {
                "name": "Local_Network_Device_Demo",
                "type": "device",
                "endpoint_url": "http://192.168.1.100:8080",
                "polling_interval": 30
            }
        ]
        
        print("🔧 Создание демонстрационных интеграций...")
        
        for integration_data in demo_integrations:
            try:
                print(f"\n🔗 Создание интеграции: {integration_data['name']}")
                print(f"   Тип: {integration_data['type']}")
                print(f"   Endpoint: {integration_data.get('endpoint_url', 'N/A')}")
                
                response = requests.post(f"{self.api_base_url}/integrations", json=integration_data)
                if response.status_code == 200:
                    result = response.json()
                    print(f"   ✅ {result['message']}")
                else:
                    print(f"   ⚠️ Ошибка: {response.status_code}")
                
            except Exception as e:
                print(f"   ❌ Ошибка: {e}")
        
        # Получение списка интеграций
        print(f"\n📋 Получение списка интеграций...")
        try:
            response = requests.get(f"{self.api_base_url}/integrations")
            if response.status_code == 200:
                integrations = response.json()
                print(f"   📊 Всего интеграций: {len(integrations)}")
                
                for integration in integrations:
                    status_icon = "🟢" if integration['status'] == 'active' else "🔴"
                    print(f"   {status_icon} {integration['name']} ({integration['type']}) - {integration['status']}")
            else:
                print(f"   ⚠️ Не удалось получить интеграции: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
    
    async def demo_incident_management(self):
        """Демонстрация управления инцидентами"""
        print("\n🚨 Демонстрация управления инцидентами")
        print("=" * 50)
        
        # Получение списка инцидентов
        try:
            print("📋 Получение списка инцидентов...")
            response = requests.get(f"{self.api_base_url}/incidents")
            if response.status_code == 200:
                incidents = response.json()
                print(f"   📊 Всего инцидентов: {len(incidents)}")
                
                if incidents:
                    # Показ деталей первого инцидента
                    first_incident = incidents[0]
                    print(f"\n🔍 Детали инцидента: {first_incident['incident_id']}")
                    print(f"   Угроза: {first_incident.get('threat_id', 'Неизвестно')}")
                    print(f"   Уровень: {first_incident['severity']}")
                    print(f"   Статус: {first_incident['status']}")
                    print(f"   Описание: {first_incident['description']}")
                    
                    # Обновление статуса инцидента
                    print(f"\n📝 Обновление статуса инцидента...")
                    update_data = {"status": "investigating"}
                    update_response = requests.put(
                        f"{self.api_base_url}/incidents/{first_incident['incident_id']}/status",
                        params={"status": "investigating"}
                    )
                    
                    if update_response.status_code == 200:
                        result = update_response.json()
                        print(f"   ✅ {result['message']}")
                    else:
                        print(f"   ⚠️ Ошибка обновления: {update_response.status_code}")
                    
                    # Показ действий по реагированию
                    if first_incident.get('response_actions'):
                        print(f"\n🛡️ Выполненные действия по реагированию:")
                        for action in first_incident['response_actions']:
                            print(f"   • {action}")
                    else:
                        print(f"\n📝 Действия по реагированию не найдены")
                    
                    # Показ ML предсказаний
                    if first_incident.get('ml_predictions'):
                        print(f"\n🤖 ML предсказания:")
                        for model, prediction in first_incident['ml_predictions'].items():
                            if 'error' not in prediction:
                                print(f"   • {model}: {prediction}")
                    
                else:
                    print("   📝 Инциденты не найдены")
                    
            else:
                print(f"   ⚠️ Не удалось получить инциденты: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
    
    async def demo_learning_system(self):
        """Демонстрация системы обучения"""
        print("\n🧠 Демонстрация системы обучения")
        print("=" * 50)
        
        try:
            # Получение метрик производительности
            print("📊 Получение метрик производительности...")
            response = requests.get(f"{self.api_base_url}/learning/performance")
            if response.status_code == 200:
                metrics = response.json()
                if metrics:
                    print(f"   📈 Поколение: {metrics.get('generation', 'N/A')}")
                    print(f"   🕒 Время: {metrics.get('timestamp', 'N/A')}")
                    
                    overall = metrics.get('overall_performance', {})
                    print(f"   🎯 Лучшая точность: {overall.get('best_accuracy', 'N/A'):.4f}")
                    print(f"   📊 Средняя точность: {overall.get('average_accuracy', 'N/A'):.4f}")
                    print(f"   🔢 Всего моделей: {overall.get('total_models', 'N/A')}")
                    
                    # Детальные метрики
                    detailed = metrics.get('detailed_performance', {})
                    if detailed:
                        print(f"\n🔍 Детальные метрики:")
                        for model_name, model_metrics in detailed.items():
                            print(f"   • {model_name}:")
                            print(f"     - Точность: {model_metrics.get('accuracy', 'N/A'):.4f}")
                            print(f"     - F1-мера: {model_metrics.get('f1_score', 'N/A'):.4f}")
                else:
                    print("   📝 Метрики производительности не найдены")
                    
            else:
                print(f"   ⚠️ Не удалось получить метрики: {response.status_code}")
            
            # Демонстрация эволюции системы
            print(f"\n🔄 Демонстрация эволюции системы обучения...")
            
            # Создание новых угроз для обучения
            new_threats = [
                {
                    "name": "Demo_Threat_1",
                    "category": "DEMO",
                    "severity": "MEDIUM",
                    "description": "Демонстрационная угроза для тестирования",
                    "ioc_patterns": {
                        "ip_addresses": ["192.168.1.200"],
                        "domains": ["demo-malware.com"]
                    }
                },
                {
                    "name": "Demo_Threat_2",
                    "category": "DEMO",
                    "severity": "HIGH",
                    "description": "Еще одна демонстрационная угроза",
                    "ioc_patterns": {
                        "file_hashes": ["demo_hash_12345"],
                        "domains": ["demo-attack.net"]
                    }
                }
            ]
            
            print(f"   📝 Добавление {len(new_threats)} новых угроз...")
            
            # Добавление угроз в базу
            for threat in new_threats:
                threat_response = requests.post(f"{self.api_base_url}/threats", json=threat)
                if threat_response.status_code == 200:
                    print(f"   ✅ Угроза '{threat['name']}' добавлена")
                else:
                    print(f"   ⚠️ Ошибка добавления угрозы: {threat_response.status_code}")
            
            # Эволюция системы обучения
            print(f"   🧠 Запуск эволюции системы обучения...")
            evolve_response = requests.post(f"{self.api_base_url}/learning/evolve", json=new_threats)
            
            if evolve_response.status_code == 200:
                result = evolve_response.json()
                print(f"   ✅ {result['message']}")
            else:
                print(f"   ⚠️ Ошибка эволюции: {evolve_response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
    
    async def demo_monitoring(self):
        """Демонстрация мониторинга"""
        print("\n📡 Демонстрация мониторинга")
        print("=" * 50)
        
        try:
            # Получение статуса мониторинга
            print("📊 Получение статуса мониторинга...")
            response = requests.get(f"{self.api_base_url}/monitor/status")
            if response.status_code == 200:
                status = response.json()
                print(f"   🟢 Мониторинг активен: {status.get('is_running', False)}")
                print(f"   📈 Всего событий: {status.get('total_events', 0)}")
                print(f"   🚨 Всего инцидентов: {status.get('total_incidents', 0)}")
                print(f"   🔗 Активных интеграций: {status.get('active_integrations', 0)}")
                
                # Запуск мониторинга
                if not status.get('is_running', False):
                    print(f"\n▶️ Запуск мониторинга...")
                    start_response = requests.post(f"{self.api_base_url}/monitor/start")
                    if start_response.status_code == 200:
                        result = start_response.json()
                        print(f"   ✅ {result['message']}")
                    else:
                        print(f"   ⚠️ Ошибка запуска: {start_response.status_code}")
                else:
                    print(f"\n⏸️ Мониторинг уже запущен")
                
                # Пауза для демонстрации работы
                print(f"\n⏳ Ожидание 5 секунд для демонстрации работы...")
                await asyncio.sleep(5)
                
                # Повторная проверка статуса
                print(f"📊 Повторная проверка статуса...")
                response = requests.get(f"{self.api_base_url}/monitor/status")
                if response.status_code == 200:
                    status = response.json()
                    print(f"   📈 Событий: {status.get('total_events', 0)}")
                    print(f"   🚨 Инцидентов: {status.get('total_incidents', 0)}")
                
            else:
                print(f"   ⚠️ Не удалось получить статус: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
    
    async def run_demo(self):
        """Запуск полной демонстрации"""
        print("🎯 Cloud Security System - Демонстрация")
        print("=" * 60)
        
        # Проверка API
        if not self.check_api_status():
            print("\n❌ API сервер недоступен. Запустите сервер командой:")
            print("   python -m api.main")
            return
        
        # Инициализация
        if not await self.initialize():
            return
        
        # Демонстрации
        await self.demo_threat_database()
        await self.demo_security_events()
        await self.demo_integrations()
        await self.demo_incident_management()
        await self.demo_learning_system()
        await self.demo_monitoring()
        
        print("\n🎉 Демонстрация завершена!")
        print("\n📚 Для получения дополнительной информации:")
        print("   • Документация: README.md")
        print("   • API документация: http://localhost:8000/docs")
        print("   • Запуск системы: python main.py")

async def main():
    """Главная функция"""
    demo = SecuritySystemDemo()
    await demo.run_demo()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⏹️ Демонстрация прервана пользователем")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        sys.exit(1)
