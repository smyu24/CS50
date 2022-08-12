
import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    #For example, if the return value of shortest_path were [(1, 2), (3, 4)], that would mean that the source
    #starred in movie 1 with person 2, person 2 starred in movie 3 with person 4, and person 4 is the target.
    #Source: a tuple tjat includes the (MOVIE_NUM, PERSON_NUM) - > (PERSON_NUM in MOVIE_NUM_2, PERSON_NUM_2 (TARGET))
    kick_off = Node(source, None, None)
    frontier = QueueFrontier()
    frontier.add(kick_off)

    #print("source:", source)
    #print("target:", target)

    while True:
        look_into = []
        path = []
        node_neighbor = ""

        if frontier.empty() == True:
            return None

        node = frontier.remove()
        #print((node.state, node.parent, node.action)) # literal node values (source_id, none, none)

        node_neighbor = neighbors_for_person(node.state) # searching for the first "frontiers" from the src value; Returns values in sets
        print(node_neighbor) # returns the sets of stars that worked in the same movies as src

        for movie_num, actor_id in node_neighbor:
            # for every index in the set "node_neighbor", ...
            if actor_id == target:
                path.append(str(movie_num) + " " + str(actor_id))
                #print(movie_num, actor_id)

            if actor_id == node.state:
                #print(movie_num, "HERE!")
                look_into.append(str(movie_num) + " " + str(actor_id))

        if len(path) == 0:
            return None

        found = (str(path[0]).split()) # split list of movie_num, then actor_id (ANSWER); Just need to back trace now for correct path

        for i in range(len(look_into)):
            if found[0] in ((look_into[i]).split())[0]:
                print("Found!")# if true, then the same movie_num should be in look_into list, therefore answer found
                #print(i, "::: ", look_into[i])
                #print(found)
                return([( ((look_into[i]).split())[0], ((look_into[i]).split())[1] ), (found[0], found[1])])
        # after contains_state, if the return is none, then remove
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """

    """
    Complete the implementation of the shortest_path function such that it returns the shortest path from the person with id source to the person with the id target.

    Assuming there is a path from the source to the target, your function should return a list, where each list item is the next (movie_id, person_id) pair in the path from the source
    to the target. Each pair should be a tuple of two strings. For example, if the return value of shortest_path were [(1, 2), (3, 4)], that would mean that the source starred
    in movie 1 with person 2, person 2 starred in movie 3 with person 4, and person 4 is the target. If there are multiple paths of minimum length from the source to the target,
    your function can return any of them. If there is no possible path between two actors, your function should return None.
    You may call the neighbors_for_person function, which accepts a person’s id as input, and returns a set of (movie_id, person_id) pairs for all people who starred in a movie with a given
    person.
    You should not modify anything else in the file other than the shortest_path function, though you may write additional functions and/or import other Python standard library modules.
    """
    """
    Hints
    While the implementation of search in lecture checks for a goal when a node is popped off the frontier, you can improve the efficiency of your search by checking for a goal as nodes are added to the frontier: if you detect a goal node, no need to add it to the frontier, you can simply return the solution immediately.
    You’re welcome to borrow and adapt any code from the lecture examples. We’ve already provided you with a file util.py that contains the lecture implementations for Node, StackFrontier, and QueueFrontier, which you’re welcome to use (and modify if you’d like).
    """
    # TODO
    raise NotImplementedError



def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
