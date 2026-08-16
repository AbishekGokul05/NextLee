import json
import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.Config.session import create_session
from app.Config.constants import REQUEST_URL
from app.Storage.cache import cache

def get_problem(filter:str):
    session = create_session()

    skip_limit = cache.get(key=f"{filter.lower().strip()}_total") or 0
    if skip_limit < 2:
        from app.Utils.utils import (
            get_easy_problem_count,
            get_hard_problem_count,
            get_medium_problem_count,
            get_total_problems_count,
        )

        count_fetchers = {
            "random": get_total_problems_count,
            "easy": get_easy_problem_count,
            "medium": get_medium_problem_count,
            "hard": get_hard_problem_count,
        }
        skip_limit = count_fetchers[filter.lower().strip()]()

    if skip_limit < 2:
        return None
    skip = random.randint(1,skip_limit-1)

    if filter.lower().strip() == "random":
        filters = ""
    else:
        filters = f"difficulty:{filter.upper().strip()}"
    query=f'''
            query problemsetQuestionList{{
            problemsetQuestionList: questionList(
            categorySlug:""
            limit:1
            skip:{skip}
            filters:{{{filters}}}){{
            total: totalNum
            question: data{{
            difficulty
            title
            titleSlug
            topicTags{{
            name
            id
            slug
            }}
            }}
            }}
            }}
        '''

    result = session.post(url=REQUEST_URL,json={"query":query})

    data = result.json()

    problem_slug = data["data"]["problemsetQuestionList"]["question"][0]["titleSlug"]
    return problem_slug

def get_total_for_filter(session, filters):
    query = """
        query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList: questionList(
                categorySlug: ""
                limit: $limit
                skip: $skip
                filters: $filters
            ) {
                total: totalNum
            }
        }
    """
    payload = {
        "query": query,
        "variables": {
            "limit": 1,
            "skip": 0,
            "filters": filters
        }
    }
    response = session.post(url=REQUEST_URL, json=payload)
    return response.json()["data"]["problemsetQuestionList"]["total"]


def get_problem_type(difficulty_filter:str, problem_filter:str):
    
    session = create_session()

    if difficulty_filter.lower().strip() == "random":
        filters = {
            "tags": [problem_filter]
        }
    else:
        filters = {
            "tags": [problem_filter],
            "difficulty": difficulty_filter.upper().strip()
        }

    # get total for THIS specific filter combination
    total = get_total_for_filter(session, filters)

    if total == 0:
        print("No problems found for this tag/difficulty combination")
        return None

    skip = random.randint(0, total - 1)

    query = """
        query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList: questionList(
                categorySlug: ""
                limit: $limit
                skip: $skip
                filters: $filters
            ) {
                questions: data {
                    title
                    titleSlug
                    topicTags {
                        name
                        id
                        slug
                    }
                }
            }
        }
    """

    payload = {
        "query": query,
        "variables": {
            "limit": 1,
            "skip": skip,
            "filters": filters
        }
    }

    response = session.post(url=REQUEST_URL, json=payload)
    problem = response.json()
    
    problem_slug = problem["data"]["problemsetQuestionList"]["questions"][0]["titleSlug"]
    return problem_slug