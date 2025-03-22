import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_user_data():
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"}
    user_url = "https://api.github.com/user"
    response = requests.get(user_url, headers=headers)
    return response.json() if response.status_code == 200 else {}

def get_repos_data():
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"}
    repos_url = "https://api.github.com/user/repos"
    response = requests.get(repos_url, headers=headers)
    return response.json() if response.status_code == 200 else []

def prepare_resume_data():
    user_data = get_user_data()
    repos_data = get_repos_data()

    name = user_data.get('name') if user_data.get('name') else "Не указано"
    login = user_data.get('login', 'Не указано')
    email = user_data.get('email', 'Скрыт') if user_data.get('email') else "Скрыт"
    public_repos = user_data.get('public_repos', 0)
    
    achievements = sorted(repos_data, key=lambda x: x['stargazers_count'], reverse=True)[:3]

    return {
        'name': name,
        'login': login,
        'email': email,
        'public_repos': public_repos,
        'repos': repos_data,
        'achievements': achievements
    }