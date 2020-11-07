from github import Github

# remove the minus sign from the key
#g = Github("7aa146eafee094d3a7b1e81aa1d8fcb0eec8b91-0")
g = Github("71b89bdc0378f2330931041ef2f2fc5730433365")

# for repo in g.get_user().get_repos():
#    print(repo.name)

repo = g.get_repo("datarepresentationstudent/aPrivateOne")
# print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
# print(urlOfFile)