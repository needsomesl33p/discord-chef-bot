import requests
import random
from food import Food
from bs4 import BeautifulSoup


BASE_URL_SEARCH = 'https://streetkitchen.hu/kereses/?q='


def _get_food_articles(url: str) -> set:
    food_list: list = []
    server_response = requests.get(url)
    soup = BeautifulSoup(server_response.text, 'html.parser')
    articles = soup.find_all(name='div', class_='entry-image')

    for article in articles:
        if len(article['class']) == 1:
            img = article.find('img')
            image_url = img.get('src')
            link = article.find('a')
            name = link.get('title')
            url = link.get('href')
            food_list.append(Food(name, url, image_url))

    return list(set(food_list))


def _build_url_params(food_name: str, category_id: str) -> str:
    if category_id:
        return f'{BASE_URL_SEARCH}{food_name}&cat={category_id} \
            %2C&cat_array%5B%5D={category_id}'
    return f'{BASE_URL_SEARCH}{food_name}'


def _choose_article(food_list: list) -> Food:
    return random.choice(food_list)


def get_food(food_name: str, category_id=None) -> Food:
    url: str = _build_url_params(food_name, category_id)
    foods: set = _get_food_articles(url)
    food: Food = _choose_article(foods)
    return food


if __name__ == '__main__':
    print('All good!')
