"""
Cloud Security System
Система защиты облачных сред с эволюционным обучением

Основные модули:
- core: Основная логика системы безопасности
- api: REST API для взаимодействия
- models: Модели данных
"""

__version__ = "1.0.0"
__author__ = "Cloud Security Team"
__description__ = "Система защиты облачных сред с эволюционным обучением"

from .core import SecurityMonitor, SecurityEvent, SecurityIncident
from .core import EvolutionarySecurityLearning, IntegrationManager

__all__ = [
    'SecurityMonitor',
    'SecurityEvent',
    'SecurityIncident', 
    'EvolutionarySecurityLearning',
    'IntegrationManager'
]
