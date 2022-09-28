from jira import JIRA
import myjira
import config

server = myjira.server
jira = JIRA(options=server, basic_auth=(myjira.username, myjira.api_token))


def title_checker(title):
    for data in config.titles:
        if title.lower().startswith(data):
            return True
    return False


def merge_request(data):
    for issue in data["issue_id"]:
        issue = jira.issue(issue)
        result = title_checker(data["title"])
        if result is True:
            print("true")
            if str(issue.fields.status) == "Review":
                jira.transition_issue(issue, config.transitions["In Progress"])
            else:
                jira.transition_issue(issue, config.transitions["Review"])
        if result is False:
            if str(issue.fields.status) == "To Do":
                jira.transition_issue(issue, config.transitions["In Progress"])
                jira.transition_issue(issue, config.transitions["Review"])

    # if "draft" != data["title"]:
    #     jira.transition_issue(issue,"21")
    # else:
    #     if issue.fields.status == "review":
    #         jira.transition_issue(issue, "21")


# def push_request(data):
