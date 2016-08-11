import pandas as pd
import numpy as np
import os
import hashlib
from github import Github
from collections import defaultdict


def get_langs(orgs):
    users = [user for user in orgs.get_public_members() if (user.name is not None and user.hireable)]
    for user in users:
    langs = defaultdict(int)
    repos = user.get_repos()
    for repo in repos:
        if not repo.private:
                l = repo.get_languages()
                for k in l:
                    langs[k] += l[k]
        peeps[hashlib.md5(user.name).hexdigest()] = langs
    return peeps


if __name__ == '__main__':
    user = os.environ['GITHUB_USER']
    password = os.environ['GITHUB_PASS']

    g = Github(user, password)
    orgs = g.get_user().get_orgs()[0]
    get files from git repo apipeeps = get_langs(orgs)
    df = pd.DataFrame.from_dict(peeps, orient='index', dtype=int)
