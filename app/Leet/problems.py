import json
import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from Config.session import create_session
from Config.constants import REQUEST_URL
from Storage.cache import cache

def get_problem(filter:str):
    session = create_session()

    skip_limit = cache.get(key=f"{filter.lower().strip()}_total")
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