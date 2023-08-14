# Remove Gitlab Access

This Pipeline is used to Remove a user's account from Gitlab(Project Access) after leaving the Org
It can also be use to scan projects to check members access.

## How to Run
- Generate Gitlab Access Token Create a variable in CI/CD , GITLAB_TOKEN and USER_NAMES
- Add USER_NAMES with users you want to remove can use ,(comma) sepration for multiple entries.

Please note that you should have Maintainer access to Remove people from Repo,
Cannot remove access provided by Group/org lvl access, to be removed from there it self.
