import aiohttp, asyncio, ssl

sslcontext = ssl.create_default_context()
sslcontext.check_hostname = False
sslcontext.verify_mode = ssl.CERT_NONE


# Функция для выполнения запроса
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


# Функция для получения рецепта
async def get_recipe(session):
    url = 'https://www.themealdb.com/api/json/v1/1/random.php'
    recipe_data = await fetch(session, url)
    return recipe_data['meals'][0]


# Функция для получения категории рецепта
async def get_category(recipe):
    return recipe['strCategory']


# Функция для получения списка блюд в заданной категории
async def get_category_meals(session, category):
    url = f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}'
    category_data = await fetch(session, url)
    return category_data['meals']


# Функция для проверки наличия масла в ингредиентах блюда
async def has_butter(session, recipe_id):
    url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_id}'
    recipe_data = await fetch(session, url)
    recipe = recipe_data['meals'][0]
    ingredients = [recipe['strIngredient1'], recipe['strIngredient2'], recipe['strIngredient3'],
                   recipe['strIngredient4'], recipe['strIngredient5']]
    return 'Butter' in ingredients


# Асинхронная функция для выполнения всей программы
async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=sslcontext)) as session:
        # Получаем 3 рецепта
        recipe_tasks = [get_recipe(session) for _ in range(3)]
        recipes = await asyncio.gather(*recipe_tasks)

        for recipe in recipes:
            # Получаем категорию рецепта
            category = await get_category(recipe)
            print('Категория:', category)

            # Получаем список блюд в категории
            category_meals = await get_category_meals(session, category)

            # Выводим названия блюд из категории, содержащих масло
            for meal in category_meals:
                if await has_butter(session, meal['idMeal']):
                    print('Блюда с маслом:', meal['strMeal'])


# Запускаем асинхронную программу
asyncio.run(main())
