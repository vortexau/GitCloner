#!/usr/bin/env python

# Setup imports as needed
# requires pip install gitpython
import git, os

# Get the file with the projects we wish to clone.
projects = "projects.txt"

print ""
print "GitCloner."
print "Clone, and keep up to date, any remote GIT repo."
print "Author: James McLean <james.mclean@gmail.com>"
print ""

with open(projects) as f:
    for gitrepo in f:
        # for each project, see if the directory exists
        gitrepo = gitrepo.strip()

        print "Processing " + gitrepo
        detail = gitrepo.split('/')

        # if directory doesn't exist, create, then clone.
        if(os.path.exists(detail[4]) == False):
            print detail[4] + "repo not found. Cloning..."
            git.Repo.clone_from(gitrepo, detail[4])
            print "Cloned."
        else:
            # if directory does exist, enter, then git pull
            print detail[4] + " exists. Getting latest..."
            repo = git.Repo(detail[4])
            pull = repo.remotes.origin
            pull.pull()

        # keep a log of what's changed.

        # keep a log of the total size of all these directories, they can get big
        # for some projects!
        print ""
