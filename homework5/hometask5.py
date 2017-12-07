import argparse
import requests
import getpass
import json
import datetime

parser = argparse.ArgumentParser("GitHub request about PR's\n\nexample of full request: python hometask5.py -u wr37ch -do -l -c -a -d -m\n", version='1.0')
parser.add_argument('-u', '--user', action='store', dest='user', help='set User whose stats You want to check (get Login if not defined)')
parser.add_argument('-do', '--days-opened', action='store_true', default=False, dest='days_switch', help='prints term of PR being opened')
parser.add_argument('-l', '--labels', action='store_true', default=False, dest='labels_switch', help='prints label of PR if exists')
parser.add_argument('-c', '--comments', action='store_true', default=False, dest='comments_switch', help='prints number of comments per PR')
parser.add_argument('-a', '--additions', action='store_true', default=False, dest='adds_switch', help='prints number of added lines per PR')
parser.add_argument('-d', '--deletions', action='store_true', default=False, dest='dels_switch', help='prints number of deleted lines per PR')
parser.add_argument('-m', '--merged', action='store_true', default=False, dest='merged_switch', help='prints User who merged PR or "Still not merged" if it still not merged')

results = parser.parse_args()

print "Username for login:"
u = raw_input()
p = getpass.getpass()

if results.user is None:
    user = u
else:
    user = results.user

# Counters for open/closed PR's
state_opened = 0
state_closed = 0
for i in (1, 2, 3, 4):
    page = i
    r = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all&page="+str(page), auth=(u, p))
    response = r.json()

    for x in response:
        if x['state'] == 'open':
            state_opened += 1
        elif x['state'] == 'closed':
            state_closed += 1


print "Total open PR's: ", state_opened
print "Total closed PR's: ", state_closed

if any((results.days_switch, results.labels_switch, results.comments_switch, results.adds_switch, results.dels_switch, results.merged_switch)) is True:
    print "\n\nStats for "+user+":"

    for i in (1, 2, 3, 4):
        page = i
        r = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all&page="+str(page), auth=(u, p))
        response = r.json()

        for x in response:
            if x['user']['login'] == user:

                print "Created at: ", x['created_at']
                print "Pull number: ", x['number']

                # Delta from opening till close
                if results.days_switch is True:
                    current_date = datetime.datetime.now()
                    date_cr = datetime.datetime.strptime(x['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                    if x['closed_at'] is not None:
                        date_cl = datetime.datetime.strptime(x['closed_at'], "%Y-%m-%dT%H:%M:%SZ")
                        delta = date_cl - date_cr
                    else:
                        delta = current_date - date_cr
                    delta_days = str(delta).split(',')
                    print "Time being opened: ", delta_days[0]

                # Adding labels
                if results.labels_switch:
                    r2 = requests.get("https://api.github.com/repos/alenaPy/devops_lab/issues/"+str(x['number'])+"/labels", auth=(u, p))
                    response2 = r2.json()
                    for y in response2:
                        if y['name'] is None:
                            print "Label: None"
                        else:
                            print "Label: ", y['name']
                if any((results.comments_switch, results.adds_switch, results.dels_switch, results.merged_switch)) is True:
                    r3 = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls/"+str(x['number']), auth=(u, p))
                    response3 = r3.json()

                    # Adding number of comments
                    print "Number of review comments: ", response3['review_comments']

                    # Adding number of added lines
                    print "Additions: ", response3['additions']

                    # Adding number of deletions
                    print "Deletions: ", response3['deletions']

                    # print response3
                    # Who merged
                    if response3['merged_by'] is None:
                        print "Still not merged"
                    else:
                        print "Merged by: ", response3['merged_by']['login']

                if results.user is True:
                    # User who opened
                    print "Opened by: ", user

                print "\n"
