
def extract_repository_languages(repos):
    return (repo["language"] for repo in repos if repo["language"] is not None)

def extract_organisation_names(organisations):
    return (org["login"] for org in organisations)

def extract_repository_names(repos):
    return (repo["name"] for repo in repos)

def analyze(input):
    terms = list(extract_repository_languages(input["repos"]))
    terms.extend(extract_organisation_names(input["orgs"]))
    terms.extend(extract_repository_names(input["repos"]))

    for term in set(terms):
        yield {
            "name": term
        }