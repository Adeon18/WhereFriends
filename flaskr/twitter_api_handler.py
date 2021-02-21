'''
This module is used in pulling data from Twitter
'''
import requests

from pprint import pprint

base_url = 'https://api.twitter.com/'

search_url = f'{base_url}1.1/friends/list.json'


def pull_data(username: str, bearer_token: str) -> dict:
    '''
    Pull the data from twitter api using a bearer token
    '''
    search_headers = {
        'Authorization': 'Bearer {}'.format(bearer_token)
    }

    search_params = {
        'screen_name': username,
        'count': 20
    }

    result = requests.get(search_url, headers=search_headers, params=search_params)

    try:
        if result.json()['error'] == 'Not authorized.':
            return False
    except KeyError:
        return result.json()


def extract_data(twitter_data: dict) -> dict:
    '''
    Extract the needed data
    '''
    extracted_data = []

    for user in twitter_data['users']:
        extracted_data.append({'name': user['name'], 'location': user['location']})
    
    return extracted_data


if __name__ == '__main__':
    print(extract_data(pull_data('@Dream', 'sdssdds')))
