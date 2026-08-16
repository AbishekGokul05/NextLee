import sys
from pathlib import Path
from rich.console import Console

sys.path.append(str(Path(__file__).parent.parent))

from Utils.utils import get_easy_problem_count, get_hard_problem_count,get_medium_problem_count,get_slugs,get_title_slugs,get_total_problems_count

def update_info():
    console = Console()

    console.print("⚠️  Updations takes time, Please hold for a moment",style="red")
    easy_count = get_easy_problem_count()
    total_count = get_total_problems_count()
    medium_count = get_medium_problem_count()
    hard_count = get_hard_problem_count()
    total_topic_count = get_slugs()

    console.print(f"Easy problem count: {easy_count}",style="white")
    console.print(f"Medium problem count: {medium_count}",style="white")
    console.print(f"Hard problem count: {hard_count}",style="white")
    console.print(f"Total problem count: {total_count}",style="white")
    console.print(f"Total Topics: {len(total_topic_count)}",style="blue")


def welcome():
    console = Console()
    welcome_note='''
                    Welceme to NextLee😎
                    Get rid of the confusion and start grinding Leetcode with nextlee💪.
                    NextLee takes care of the confusion you only care about solving the problem👾.

                    Try : nextlee random --> to get started with the problems.

                    Try : nextlee potd --> to open the daily problem.
                '''
    
    console.print(welcome_note,style="cyan")