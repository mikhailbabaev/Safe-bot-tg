import random

WELCOME_MESSAGE = """
🚨 В России каждый месяц угоняют более 10 тысяч telegram-аккаунтов. В зоне риска каждый 3й россиянин.

Мошенники используют их для спама, вымогательств и кражи денег. 

Самое печальное, что в большинстве случаев украденный профиль уже не вернуть.

💡 Этот бот выполняет все возможные проверки и действия для защиты аккаунта и снижает вероятность кражи до минимума.

Текущий статус защищенности вашего аккаунта - “не определен” 

👉 Нажмите «Проверить аккаунт» и узнайте, насколько ваш telegram защищен.
"""

# Сообщения этапов проверки
SECURITY_STEPS = [
    ("🔍 Анализ уязвимостей", 10),
    ("🔑 Проверка паролей", 25),
    ("🛡️ Оценка двухфакторной защиты", 40),
    ("📡 Поиск утечек в даркнете", 60),
    ("⚙️ Анализ активности входов", 80),
    ("✅ Завершающий этап", 95)
]


# Возможные результаты проверки
FINAL_RESULTS = [
    "✅ Безопасность на высоком уровне. Угроз не обнаружено.",
    "⚠️ Найдены потенциальные риски. Рекомендуется сменить пароли.",
    "🚨 Обнаружены утечки данных! Срочно обновите пароли и включите 2FA!"
]


FAQ_TEXT =\
"""📘 Для подробной информации о нашем сервисе, пожалуйста, ознакомьтесь с ответами на часто задаваемые вопросы:
"[Перейти к FAQ](https://telegra.ph/FAQ-02-22-6)"
"""

PAYMENT_TEXT = """
<b>Исправить уязвимости Telegram</b>  
<b>Цена: 199₽</b>

Что вы получаете?  
• Расширенные проверки безопасности аккаунта (детальный анализ)  
• Автоматическое исправление найденных уязвимостей (где возможно)  
• Видео-инструкции по исправлению найденных уязвимостей (где невозможно автоматически)

<u>Мы используем только официальные инструменты Telegram, не запрашиваем админские права и не получаем доступ к вашим данным</u>
"""


PROMOCODE = """
Функция промокодов в разработке. Запустим через месяц.
"""


# Функция для выбора случайного финального результата
def get_random_result():
    return random.choice(FINAL_RESULTS)

# Функция для генерации прогресс-бара
def progress_bar(percent):
    filled = "█" * (percent // 10)
    empty = "░" * (10 - percent // 10)
    return f"[{filled}{empty}] {percent}%"
