import requests

questions = requests.get(url='https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')
questions.raise_for_status()

question_data = questions.json()['results']

