from app.Config.constants import REQUEST_URL
from app.Config.session import create_session


def get_potd_problem():
     session = create_session()

     query = '''
          query questionOfToday {
               activeDailyCodingChallengeQuestion {
                    link
                    question {
                         titleSlug
                    }
               }
          }
     '''

     response = session.post(url=REQUEST_URL, json={"query": query})
     data = response.json()

     potd = data.get("data", {}).get("activeDailyCodingChallengeQuestion")
     if not potd:
          return None

     question = potd.get("question") or {}
     title_slug = question.get("titleSlug")
     if title_slug:
          return title_slug

     link = potd.get("link") or ""
     if link:
          return link.rstrip("/").split("/")[-1]

     return None