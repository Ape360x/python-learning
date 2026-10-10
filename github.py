import requests

def find_repo_with_most_stars(data):
    best_stars = -1
    best_name = None
    for repo in data:
        if repo["stargazers_count"] > best_stars:
            best_stars = repo["stargazers_count"]
            best_name = repo["name"]
    return best_name

try:
    repo = requests.get("https://api.github.com/users/Ape360x", timeout=10)
    repo.raise_for_status()
    repos = repo.json()
    print(repos)
    print(repos.keys())
    print(repos["login"])
    print(repos["name"])
    print(repos["public_repos"])
    print(repos["followers"])
    print(repos["created_at"])
    repos = requests.get("https://api.github.com/users/Ape360x/repos").json()
    print(len(repos))
except requests.exceptions.ConnectionError:
    print("No internet connection")
except requests.exceptions.Timeout:
    print("Github took a long time to respond")
except requests.HTTPError as e:
    print("Github got an error", e)

else:
    print(find_repo_with_most_stars(repos))
    print(len(repos))
    len(repos)








