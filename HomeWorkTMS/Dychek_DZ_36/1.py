import asyncio
import aiohttp
import ssl

sslcontext = ssl.create_default_context()
sslcontext.check_hostname = False
sslcontext.verify_mode = ssl.CERT_NONE

github_token = "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"


async def fetch_repos(username):
    headers = {
        "Authorization": f"Bearer {github_token}"
    }
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=sslcontext)) as session:
        url = f"https://api.github.com/users/{username}"
        async with session.get(url=url, headers=headers) as response:
            data = await response.json()
            if response.status == 200:
                repos = [repo["repo_url"] for repo in data.get("repos", [])]
                return repos
            else:
                print(f"Ошибка при получении репозиториев для пользователя {username}: {data}")


async def main(users):
    tasks = []
    for username in users:
        task = asyncio.create_task(fetch_repos(username))
        tasks.append(task)

    # Ожидаем выполнения всех задач
    results = await asyncio.gather(*tasks)

    # Выводим результаты
    for username, repos in zip(users, results):
        if repos:
            print(f"Репозитории для пользователя {username}:")
            for repo in repos:
                print(repo)
        else:
            print(f"Для пользователя {username} не найдено репозиториев")


if __name__ == '__main__':
    users = [
        "Arantir1", "EgorTimofeychik", "maximax15", "letov2110", "denirix",
        "Noowkies", "NikDychek", "marinamonit", "PolonskyIllya",
        "temabuchka88", "LuydmilaKot", "katherinepcholka", "telenchenkosergey"
    ]

    asyncio.run(main(users))
