import subprocess
import random
import datetime

# Файлы, которые будем трогать
FILES = [
    "shop/views.py",
    "shop/models.py",
    "shop/serializers.py",
    "shop/admin.py",
    "shop/tests.py",
    "README.md",
    "requirements.txt",
]

# Сообщения коммитов (реалистичные)
MESSAGES = [
    "Refactor views for clarity",
    "Improve API pagination",
    "Add filtering for products",
    "Fix serializer validation",
    "Update admin panel configuration",
    "Optimize database queries",
    "Add product search feature",
    "Improve model __str__ representation",
    "Update API docs",
    "Refactor tests for better coverage",
    "Fix typo in README",
    "Improve error handling in views",
    "Add comments for maintainability",
    "Refactor serializers for DRY principle",
    "Add caching for product list",
    "Update requirements.txt",
    "Improve logging messages",
    "Fix bug in order calculation",
    "Refactor URL patterns",
    "Update docstrings for clarity",
    "Improve test performance",
    "Add constants for repeated values",
    "Fix bug in admin filter",
    "Enhance API response format",
    "Update permissions for views",
    "Add search index for products",
    "Improve performance for large datasets",
    "Update README with deployment steps",
    "Refactor model relationships",
    "Fix missing import in views",
]

def git(cmd):
    subprocess.run(["git"] + cmd, check=True)

def random_date():
    start = datetime.datetime(2024, 5, 1)  # начало истории
    end = datetime.datetime(2025, 8, 30)   # текущая дата
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_time = datetime.timedelta(seconds=random.randint(0, 86400))
    return start + datetime.timedelta(days=random_days) + random_time

def main():
    for i in range(50):  # 50 коммитов
        file = random.choice(FILES)
        message = random.choice(MESSAGES)
        date = random_date()
        # Вносим фиктивное изменение
        with open(file, "a", encoding="utf-8") as f:
            f.write(f"# {message}\n")
        # Добавляем в git
        git(["add", file])
        # Создаём коммит с кастомной датой
        env = {
            "GIT_COMMITTER_DATE": date.isoformat(),
            "GIT_AUTHOR_DATE": date.isoformat(),
        }
        subprocess.run(
            ["git", "commit", "-m", message],
            check=True,
            env={**env, **dict(**env)}
        )
        print(f"[{i+1}/50] {message} ({date.strftime('%Y-%m-%d')})")

if __name__ == "__main__":
    main()
