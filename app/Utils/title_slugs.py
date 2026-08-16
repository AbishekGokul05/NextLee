import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from app.Config.session import create_session
from app.Config.constants import REQUEST_URL
from app.Storage.cache import cache

count = cache.get(key="random_total") or 0

slugs = set()
limit = 100
session = create_session()
def get_slugs():
    title_slug = {}
    if count <= 0:
        cache.set(key="title_slug", value=slugs)
        return slugs

    for skip in range(0,count,limit):
        query = f'''
            query problemsetQuestionList{{
            problemsetQuestionList:questionList(
            categorySlug:""
            limit:{limit}
            skip:{skip}
            filters:{{}}
            ){{
            question: data{{
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

        questions = result.json()["data"]["problemsetQuestionList"]["question"]

        for question in questions:
            for tag in question["topicTags"]:
                title_slug[tag["name"]] = tag["slug"]
                slugs.add(tag["slug"])
    
    cache.set(key="title_slug",value=slugs)

    return slugs