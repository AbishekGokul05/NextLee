import sys
from pathlib import Path

sys.path.append((str(Path(__file__).resolve().parent.parent)))

from Config.session import create_session
from Config.constants import REQUEST_URL
from Storage.cache import cache


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
get_total_problems_count()
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