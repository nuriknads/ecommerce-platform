# commit_generator.py
import os
import random
import subprocess
from datetime import datetime, timedelta

TOTAL_COMMITS = 60  # аккуратно ~60 коммитов
START = datetime(2019, 1, 1)
END   = datetime(2023, 12, 31)

commit_messages = [
    "Refactor serializers for clarity",
    "Fix bug in Product serializer",
    "Add product filters",
    "Improve API response for products",
    "Update README with run instructions",
    "Fix typo in views",
    "Add tests scaffold",
    "Improve model __str__",
    "Update requirements.txt",
    "Refactor views for DRF best practices",
    "Add admin display fields",
    "Optimize query in products list",
    "Add pagination defaults",
    "Update API docs section",
    "Minor improvements to settings",
    "Fix migrations ordering",
    "Small cleanup in serializers",
    "Add comments to clarify logic",
    "Improve logging messages",
    "Format code (flake8 style)",
    "Add example curl to README",
    "Adjust default page size",
    "Fix ordering bug",
    "Update docstrings",
    "Add helper function for orders",
    "Remove unused import",
]

# Список файлов, в которые будем аккуратно писать (комментарии/строки)
files = [
    "README.md",
    "requirements.txt",
    "shop/models.py",
    "shop/serializers.py",
    "shop/views.py",
    "shop/admin.py",
    "shop/tests.py",
    "ecommerce/settings.py"
]

def random_date(start, end):
    delta = end - start
    days = random.randint(0, delta.days)
    # рандомное время в течение дня
    seconds = random.randint(0, 23*3600 + 3599)
    return start + timedelta(days=days, seconds=seconds)

def safe_append(filename, text):
    # если файла нет — создаём (чтобы не ломать)
    dirpath = os.path.dirname(filename)
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath, exist_ok=True)
    mode = "a"
    with open(filename, mode, encoding="utf-8") as f:
        f.write(text)

def git(cmd, env=None):
    return subprocess.run(["git"] + cmd, env=env, check=True)

def main():
    # убедимся, что рабочая директория чиста (рекомендация)
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if status.stdout.strip():
        print("Внимание: рабочее дерево не чистое. Сохрани или зафиксируй текущие изменения перед запуском.")
        print(status.stdout)
        return

    for i in range(TOTAL_COMMITS):
        msg = random.choice(commit_messages)
        date = random_date(START, END)
        target = random.choice(files)

        # текст, который будет добавлен — в .py файлы добавляется комментарий, в другие — строка
        ext = os.path.splitext(target)[1].lower()
        if ext == ".py":
            add_text = f"\n# NOTE: history update {i+1} — {msg} ({date.strftime('%Y-%m-%d')})\n"
        else:
            add_text = f"\nUpdate {i+1}: {msg} — {date.strftime('%Y-%m-%d')}\n"

        safe_append(target, add_text)

        # git add
        git(["add", target])

        # коммит с установленными датами
        env = os.environ.copy()
        ts = date.strftime("%Y-%m-%d %H:%M:%S")
        env["GIT_AUTHOR_DATE"] = ts
        env["GIT_COMMITTER_DATE"] = ts
        git(["commit", "-m", msg], env=env)

        if (i + 1) % 10 == 0:
            print(f"Создано коммитов: {i+1}")

    print(f"Готово — создано {TOTAL_COMMITS} коммитов. Не забудь: git push origin main")
    return

if __name__ == "__main__":
    main()
