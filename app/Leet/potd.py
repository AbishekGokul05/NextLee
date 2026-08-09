from Config.session import create_session
from Config.constants import REQUEST_URL

session = create_session()

query ='''query questionOfToday{
            activeDailyCodingChallengeQuestion{
            link
            }
            }
       '''

result = session.post(url=REQUEST_URL,json={"query":query})
print(result.text)