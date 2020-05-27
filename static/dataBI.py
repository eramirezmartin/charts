import os
import json
import shutil

from datetime import datetime
import gitlab

TOKEN = 'bUXR6N_H9bETU6VAPSyx'


def read_milestone_files():
    PATH = 'data'
    list_files = sorted(os.listdir(PATH))
    for file in list_files:
        if file.startswith('devel_'):
            with open(os.path.join(PATH, file)) as mil_rep:
                file_json = json.load(mil_rep)
                if file_json['milestone'] != 'devel_sprint_2020_weeks0809':
                    json_milestone(file_json)


def json_milestone(json_file):
    with open('milestone_analysis.json', mode='r') as milestone_file:
        temporal_report_milestone = json.load(milestone_file)
    milestone_file.close()
    try:
        total = json_file['milestone_closed_issues']
    except KeyError:
        total = json_file['original_total_issues']
    if json_file['milestone_closed_issues'] > 0:
        json_file['priority'] = reverse_calculate_percentage(json_file['priority'], total)
        json_file['type'] = reverse_calculate_percentage(json_file['type'], total)
        temporal_dict = {"milestone": json_file['milestone'].replace("_"," ").title(),
                         "dates": "",
                         "milestone_closed_issues": json_file['milestone_closed_issues'],
                         "milestone_merge_request": json_file['milestone_merge_request'],
                         "milestone_planned_issues": json_file['original_total_issues'],
                         "milestone_planned_percentage": json_file['% milestone'],
                         "milestone_added_issues": json_file['number_added_issues'],
                         "p_critical": json_file['priority']['p_critical'],
                         "p_high": json_file['priority']['p_high'],
                         "p_hotfix": json_file['priority']['p_hotfix'],
                         "p_medium": json_file['priority']['p_medium'],
                         "p_low": json_file['priority']['p_low'],
                         "tp_bug": json_file['type']['tp_bug'],
                         "tp_new_feature": json_file['type']['tp_new_feature'],
                         "tp_technical_debt Debt": json_file['type']['tp_technical_debt'],
                         "tp_discussion": json_file['type']['tp_discussion'],
                         "tp_poc": json_file['type']['tp_poc'],
                         "tp_support": json_file['type']['tp_support']}
        temporal_report_milestone.append(temporal_dict)
        with open('milestone_analysis.json', mode='w') as milestone_file:
            json.dump(temporal_report_milestone, milestone_file)
        milestone_file.close()


def reverse_calculate_percentage(json_file, total):
    for item in json_file:
        json_file[item] = round(float(json_file[item][:-1]) * total / 100)
    return json_file


def gitlab_init():
    gitlab_client = gitlab.Gitlab('https://primus.omniaccess.com', private_token=TOKEN)
    gitlab_client.auth()
    return gitlab_client.projects.list(all=True)


def get_issues(milestone):
    tp_map = {
        'tp_bug': 'Bug',
        'tp_new_feature': 'New Feature',
        'tp_technical_debt': 'Technical Debt',
        'tp_discussion': 'Discussion',
        'tp_poc': 'Poc',
        'tp_support': 'Support'
    }

    p_map = {
        'p_hotfix': 'Hotfix',
        'p_critical': 'Critical',
        'p_high': 'High',
        'p_medium': 'Medium',
        'p_low': 'Low'
    }

    f_map = {'fl_analysis': 'Analysis',
             'fl_doing': 'Doing',
             'fl_ready': 'Ready',
             'fl_qa': 'QA',
             'fl_waiting': 'Waiting'}

    pending_issues = []
    for project in gitlab_init():
        try:
            issues = project.issues.list(milestone=milestone, all=True)
            for issue in issues:
                if issue.state != 'closed':
                    pending_issues.append({"issue_project": project.name_with_namespace[14:].replace(" / ", "/"),
                                           "issue_title": issue.title,
                                           "issue_link": issue.web_url,
                                           "issue_priority": match(issue.labels, p_map, 'Undefined'),
                                           "issue_type": match(issue.labels, tp_map, 'Undefined'),
                                           "issue_status": match(issue.labels, f_map, 'Open'),
                                           "issue_assigned": issue.assignee["username"] if issue.assignee else "Unassigned"})
        except Exception as e:
            print(str(e))
    order_list = []
    for priority in ['Hotfix', 'Critical', 'High', 'Medium', 'Low', 'Undefined']:
        order_list.extend(list(filter(lambda x: x['issue_priority'] == priority, pending_issues)))
    with open('milestone_issues.json', mode='w') as milestone_file:
        json.dump(order_list, milestone_file)
    milestone_file.close()


def match(json_label, s_map, default):
    description = default
    try:
        match = next(x for x in json_label if x in s_map)
        description = s_map[match]
    except StopIteration:
        pass
    return description


def get_mr():
    pending_mr = []
    for project in gitlab_init():
        try:
            project_mr_list = project.mergerequests.list(all=True)
            if len(project_mr_list) > 0:
                for mr in project_mr_list:
                    if mr.state == 'opened' and not mr.title.startswith("WIP: ") and mr.milestone:
                        if mr.milestone['title'].startswith("devel_sprint_"):
                            pending_requester = 0
                            discussions = mr.discussions.list()
                            for discussion in discussions:
                                notes = discussion.attributes['notes']
                                for note in notes:
                                    if note['resolvable']:
                                        if not note['resolved']:
                                            pending_requester += 1
                            if pending_requester == 0:
                                PendingDiscussion = False
                            else:
                                PendingDiscussion = True
                            pending_mr.append({"mr_project": project.name_with_namespace[14:].replace(" / ", "/"),
                                               "mr_title": mr.title,
                                               "mr_link": mr.web_url,
                                               "mr_updated": mr.updated_at[:10],
                                               "mr_pending_discussion": PendingDiscussion,
                                               "mr_up_votes": mr.upvotes,
                                               "mr_down_votes": mr.downvotes})

        except Exception as e:
            print(str(e))
    pending_mr = sorted(pending_mr, key=lambda k: k['mr_updated'])
    with open('milestone_mr.json', mode='w') as milestone_file:
        json.dump(pending_mr, milestone_file)
    milestone_file.close()


# print(datetime.now())
# read_milestone_files()
print(datetime.now())
get_mr()
print(datetime.now())
get_issues("devel_sprint_2020_weeks2122")
print(datetime.now())
