import requests
import random
from food import Food
from bs4 import BeautifulSoup


BASE_URL_SEARCH = 'https://streetkitchen.hu/kereses/?q='
EMPTY_SEARCH_RESULT_IMG = 'https://media.tenor.com/rhzC9_tMUukAAAAS/will-smith-eating-spaghetti-will-smith.gif'


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

    set_of_foods: set = list(set(food_list))
    if set_of_foods:
        return set_of_foods
    raise NoFoodWasFound


def _build_url_params(food_name: str, category_id: str) -> str:
    if category_id:
        return f'{BASE_URL_SEARCH}{food_name}&cat={category_id} \
            %2C&cat_array%5B%5D={category_id}'
    return f'{BASE_URL_SEARCH}{food_name}'


def _choose_article(food_list: list) -> Food:
    return random.choice(food_list)


def get_food(food_name: str, category_id=None) -> Food:
    try:
        url: str = _build_url_params(food_name, category_id)
        foods: set = _get_food_articles(url)
        food: Food = _choose_article(foods)
        return food
    except NoFoodWasFound as ex:
        return Food(ex.message, EMPTY_SEARCH_RESULT_IMG,
                    'no image for this time')


class NoFoodWasFound(Exception):
    '''Raised when the search did not find any food on the streetkitchen's site.'''

    def __init__(self):
        self.message = 'No food was found! Make sure there is no typo in you search and it is written Hungarian.'


if __name__ == '__main__':
    print('All good!')
