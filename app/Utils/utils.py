import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table

sys.path.append((str(Path(__file__).resolve().parent.parent)))

from app.Config.session import create_session
from app.Config.constants import REQUEST_URL
from app.Storage.cache import cache
from app.Utils.title_slugs import get_slugs


def get_total_problems_count():
    session = create_session()

    query = '''
            query problemsetQuestionList{
            problemsetQuestionList:questionList(
            categorySlug:""
            limit:1
            skip:0
            filters:{}
            ){
            total:totalNum
            }
            }
            '''

    response = session.post(url=REQUEST_URL,json={"query":query})
    data = response.json()
    problem_count = data["data"]["problemsetQuestionList"]["total"]

    cache.set(key="random_total",value=problem_count)

    return problem_count

def get_easy_problem_count():
    session = create_session()

    query = '''
        query problemsetQuestionList {
            problemsetQuestionList: questionList(
                categorySlug: ""
                limit: 1
                skip: 0
                filters: {difficulty: EASY}
            ) {
                total: totalNum
            }
        }
    '''

    response = session.post(
        url=REQUEST_URL,
        json={"query": query}
    )

    data = response.json()

    easy_problem_count = data["data"]["problemsetQuestionList"]["total"]

    cache.set(
        key="easy_total",
        value=easy_problem_count
    )

    return easy_problem_count
    

def get_medium_problem_count():
    session = create_session()

    query = '''
        query problemsetQuestionList {
            problemsetQuestionList: questionList(
                categorySlug: ""
                limit: 1
                skip: 0
                filters: {difficulty: MEDIUM}
            ) {
                total: totalNum
            }
        }
    '''

    response = session.post(
        url=REQUEST_URL,
        json={"query": query}
    )

    data = response.json()

    medium_problem_count = data["data"]["problemsetQuestionList"]["total"]

    cache.set(
        key="medium_total",
        value=medium_problem_count
    )
    return medium_problem_count

def get_hard_problem_count():
    session = create_session()

    query = '''
        query problemsetQuestionList {
            problemsetQuestionList: questionList(
                categorySlug: ""
                limit: 1
                skip: 0
                filters: {difficulty: HARD}
            ) {
                total: totalNum
            }
        }
    '''

    response = session.post(
        url=REQUEST_URL,
        json={"query": query}
    )

    data = response.json()

    hard_problem_count = data["data"]["problemsetQuestionList"]["total"]

    cache.set(
        key="hard_total",
        value=hard_problem_count
    )
    return hard_problem_count

def get_title_slugs():

    title_slugs = cache.get(key="title_slug")
    if not title_slugs:
        if not cache.get(key="random_total"):
            get_total_problems_count()
        title_slugs = get_slugs()


    console = Console()
    table = Table(title="Available Topics")

    table.add_column("No.",style="cyan",justify="center")
    table.add_column("Topic",style="white",justify="center")

    for no,topic in enumerate(sorted(title_slugs),start=1):
        table.add_row(str(no),topic)

    console.print(table)