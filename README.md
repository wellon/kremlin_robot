# Кремлебот 🤖
Бот, решающий куда ты пойдешь сегодня обедать. И всю твою судьбу вообще.

Очень простой в реализации. Bot API используется исключительно для отправки оповещений.

## Usage 
#### 1. Достаточно заполнить [файл с конфигом](https://github.com/wellon/kremlin_robot/blob/master/config.py) под себя, указав:
- [токен бота](https://github.com/wellon/kremlin_robot/blob/a249e1d391b9ecd5cf20e8eefbabe68104a2ab2f/config.py#L1) (берётся у [BotFather'а](https://t.me/botfather))
- [чат-айди](https://github.com/wellon/kremlin_robot/blob/a249e1d391b9ecd5cf20e8eefbabe68104a2ab2f/config.py#L2), куда будет отправляться оповещение
- [время оповещения](https://github.com/wellon/kremlin_robot/blob/a249e1d391b9ecd5cf20e8eefbabe68104a2ab2f/config.py#L4) (оповещение происходит [раз в сутки по будням](https://github.com/wellon/kremlin_robot/blob/a249e1d391b9ecd5cf20e8eefbabe68104a2ab2f/bot.py#L35))
- [варианты](https://github.com/wellon/kremlin_robot/blob/a249e1d391b9ecd5cf20e8eefbabe68104a2ab2f/config.py#L7) для выбора (обычно, названия заведений)
- данные от [socks-proxy](https://github.com/wellon/kremlin_robot/blob/a249e1d391b9ecd5cf20e8eefbabe68104a2ab2f/config.py#L13)
#### 2. Запустить, как обычный python-скрипт.
#### 3. Готово, вы восхитительны.
