import problems.day1_p1
import problems.day1_p2

__all__ = ['solve']


__problems = {
    'd1p1': day1_p1.solve,
    'd1p2': day1_p2.solve
}


def solve(problem: str):
    problem = problem.lower().strip()
    if problem not in __problems:
        raise ValueError(f"undefined problem: {problem}")
    __problems[problem]()
