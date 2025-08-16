#!/usr/bin/env python3
"""
Быстрый запуск Cloud Security System
"""

import sys
import os
import subprocess
import time

def main():
    print("🚀 Cloud Security System - Быстрый запуск")
    print("=" * 50)
    
    # Проверка Python версии
    if sys.version_info < (3, 8):
        print("❌ Требуется Python 3.8 или выше")
        sys.exit(1)
    
    print("✅ Python версия:", sys.version.split()[0])
    
    # Проверка зависимостей
    print("\n📦 Проверка зависимостей...")
    try:
        import fastapi
        import uvicorn
        import sklearn
        import numpy
        print("✅ Все зависимости установлены")
    except ImportError as e:
        print(f"❌ Отсутствуют зависимости: {e}")
        print("📥 Установите зависимости командой: pip install -r requirements.txt")
        sys.exit(1)
    
    # Создание директорий
    print("\n📁 Создание необходимых директорий...")
    os.makedirs("models", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    print("✅ Директории созданы")
    
    # Запуск API сервера
    print("\n🌐 Запуск API сервера...")
    print("   API будет доступен по адресу: http://localhost:8000")
    print("   Документация API: http://localhost:8000/docs")
    
    try:
        # Запуск API сервера в фоновом режиме
        api_process = subprocess.Popen([
            sys.executable, "-m", "api.main"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Ожидание запуска сервера
        print("   ⏳ Ожидание запуска сервера...")
        time.sleep(3)
        
        # Проверка доступности API
        import requests
        try:
            response = requests.get("http://localhost:8000/health", timeout=5)
            if response.status_code == 200:
                print("   ✅ API сервер запущен успешно")
            else:
                print(f"   ⚠️ API сервер отвечает с кодом: {response.status_code}")
        except requests.exceptions.RequestException:
            print("   ⚠️ API сервер еще не готов, продолжаем...")
        
        print("\n🎯 Система запущена!")
        print("\n📚 Доступные команды:")
        print("   • Демонстрация: python run_demo.py")
        print("   • Основной режим: python main.py")
        print("   • Остановка API: Ctrl+C в этом терминале")
        
        print("\n🔍 Для просмотра логов:")
        print("   • API логи: в этом терминале")
        print("   • Системные логи: cloud_security.log")
        
        # Ожидание завершения
        try:
            api_process.wait()
        except KeyboardInterrupt:
            print("\n\n⏹️ Остановка API сервера...")
            api_process.terminate()
            api_process.wait()
            print("✅ API сервер остановлен")
            
    except Exception as e:
        print(f"❌ Ошибка запуска API сервера: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        sys.exit(1)
