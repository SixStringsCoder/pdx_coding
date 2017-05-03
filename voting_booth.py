"""

Create a voting booth application. 

It will take in candidates names from a series of users, until someone types 'done'. Then calculate the vote counts for each candidate and print them out. 

"""

import chalk


def voting_machine(nominees):
    options = {index: cand for index, cand in enumerate(nominees, start=1)}
    votes = nominees

    try:
        vote_cast = int(input('Type the number for the candidate you want. --> '))
    except ValueError:
        chalk.red('Not valid! Try again')
        return voting_machine(nominees)

    choice = options[vote_cast]
    votes[choice] += 1

    chalk.green("Your vote has been counted.")
    chalk.yellow(f"Current standing: {votes}")

    more_votes = input("Continue voting?  Y/n ")
    if more_votes.lower() != 'n':
        voting_machine(nominees)
    else:
        winner = max(votes.items(), key=lambda t: t[-1])
        chalk.magenta(f"The winner is {winner[0]} with {winner[1]} votes.")


def display_marquee():
    banner_decor = ('-' * 41)
    spaces = (' ' * 18)
    marquee = f'\n{banner_decor}\n{spaces}OFFICIAL BALLOT{spaces}\n{banner_decor}'
    chalk.red(marquee)


def ballot_maker(candidates):
    display_marquee()

    nominees = dict()
    for i, p in enumerate(candidates, start=1):
        nominees.update({p: 0})                 #  Build up vote dictionary
        ballot = f"{i} ---> {p}"
        chalk.cyan(ballot)

    voting_machine(nominees)                    # call function 'voting_machine' with 'vote' dictionary passed thru


def data_collect():
    candidates = list()
    while True:
        i_want = input("Type in a candidate for office? ---> ")

        if i_want.lower() == 'done':
            break

        candidates.append(i_want)

    ballot_maker(candidates)

if __name__ == "__main__":
    data_collect()


