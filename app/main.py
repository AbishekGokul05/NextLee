import sys
from pathlib import Path
from rich.console import Console

if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.Leet.open_problem import open_problem
from app.Leet.commands import update_info, welcome
from app.Config.constants import VALID_COMMANDS, VALID_DIFFICULTY
from app.Leet.potd import get_potd_problem
from app.Utils.utils import get_title_slugs
from app.Leet.problems import get_problem_type, get_problem
from app.Storage.cache import cache

console = Console()

def main():
    command_lenght = len(sys.argv)
    if command_lenght == 1:
        welcome()
        sys.exit(0)
    if command_lenght == 2:
        command = sys.argv[1]

        if command in VALID_COMMANDS:
            if command == "topics":
                get_title_slugs()
                sys.exit(0)
            if command == "potd":
                problem = get_potd_problem()
                if not problem:
                    console.print("No daily problem could be found")
                    sys.exit(1)

                open_problem(problem_title=problem)
                sys.exit(0)
            else:
                update_info()
                sys.exit(0)
        
        if command in VALID_DIFFICULTY:
            problem = get_problem(filter=command)
            if not problem:
                console.print(f"No problem could be selected for {command}")
                sys.exit(1)
            open_problem(problem_title=problem)
            sys.exit(0)
    
    if command_lenght==3:
        command_1 = sys.argv[1]
        command_2 = sys.argv[2]

        if command_1 not in VALID_DIFFICULTY:
            console.print(f"{command_1.lower().strip()} is not a valid command")
            sys.exit(1)

        title = cache.get(key="title_slug") or set()
        if command_2 not in title:
            console.print(f"{command_2} is not a valid comand")
            sys.exit(1)

        command = get_problem_type(difficulty_filter=command_1,problem_filter=command_2)

        if not command:
            console.print("No problem could be selected for that tag and difficulty")
            sys.exit(1)

        open_problem(problem_title=command)
        sys.exit(0)

if __name__ == "__main__":
    main()
