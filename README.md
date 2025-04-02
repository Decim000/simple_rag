# Инструкция

Чтобы проект жил:

1. Скачать ollama и спуллить модели:
    - gemma3:4b
    - snowflake-arctic-embed2

2. Запустить модель Gemma3

3. Создать Record Manager из соответствующего скрипта, перенести в директорию /app

4. uvicorn app:app --reload