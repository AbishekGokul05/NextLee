import webbrowser

from app.Config.constants import PROBLEM_URL
from app.Leet.problems import get_problem

def open_problem(problem_title:str):

    URL = PROBLEM_URL.replace("{title_slug}",problem_title)
    webbrowser.open(url=URL)