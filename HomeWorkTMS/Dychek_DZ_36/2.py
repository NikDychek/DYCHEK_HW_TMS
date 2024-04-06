import aiohttp, asyncio, ssl

sslcontext = ssl.create_default_context()
sslcontext.check_hostname = False
sslcontext.verify_mode = ssl.CERT_NONE

github_token = "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"


async def fetch_repos(username):
    headers = {
        "Authorization": f"Bearer {github_token}"
    }


async def get_repositories(username):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=sslcontext)) as session:
        async with session.get(f"https://api.github.com/users/{username}") as response:
            user = await response.json()
            repositories_url = user["repos_url"]

            async with session.get(repositories_url) as repositories_response:
                repositories = await repositories_response.json()
                for repository in repositories:
                    print(repository["full_name"])


users = ["Arantir1", "EgorTimofeychik", "maximax15", "letov2110", "denirix", "Noowkies", "NikDychek", "marinamonit",
         "PolonskyIllya", "temabuchka88", "LuydmilaKot", "katherinepcholka", "telenchenkosergey"]


async def main():
    tasks = [get_repositories(username) for username in users]
    await asyncio.gather(*tasks)


asyncio.run(main())
