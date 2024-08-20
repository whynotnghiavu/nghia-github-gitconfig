import os
# pip install requests
import requests


def create_git_folder(list_username):

    for username in list_username:
        print(f"🚀username = {username}")
        gitdir = os.path.expanduser(f"~/Downloads/Nghia/Git/{username}/")

        # Create the directory if it doesn't exist
        os.makedirs(gitdir, exist_ok=True)


def create_gitconfig_global(list_username):

    content = """
[core]
excludesfile = ~/.gitignore
    """

    for username in list_username:
        print(f"🚀username = {username}")
        content += f"""
[includeIf "gitdir:~/Downloads/Nghia/Git/{username}/"]
path = ~/{username}.gitconfig
        """

    with open(".gitconfig", 'w') as file:
        file.write(content)


def get_github_id(username):

    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('id')
    else:
        return None


def get_github_email(username):

    github_id = get_github_id(username)
    if github_id:
        print(f'github_id = {github_id}')
    else:
        print(f'Not find github_id')
        exit()

    return f"{github_id}+{username}@users.noreply.github.com"


def create_gitconfig_file(username):

    github_email = get_github_email(username)
    if github_email:
        print(f'github_email = {github_email}')
    else:
        print(f'Not find github_email')
        exit()

    content = """
[user]
name = """ + username + """
email = """ + github_email + """

[github]
user = """ + username + """

[core]
sshCommand = "ssh -i ~/.ssh/""" + username + """"
    """

    with open(f"{username}.gitconfig", 'w') as file:
        file.write(content)


def create_symlink(list_username):
    list_gitconfig = []

    list_gitconfig.append(".gitconfig")
    for username in list_username:
        print(f"🚀username = {username}")
        list_gitconfig.append(f"{username}.gitconfig")
 
        

            

    for path in list_gitconfig:
        print(f"🚀path = {path}")
        symlink_path = os.path.expanduser(f"~/{path}")
        print(f"🚀symlink_path = {symlink_path}")

        try:
            os.remove(symlink_path)
            print(f"Đã xóa symlink: {symlink_path}")
            os.symlink(os.path.abspath(path), symlink_path)
            print(f"Symbolic link created at: {symlink_path}")
        except OSError as e:
            print(f"Failed to create symbolic link: {e}")



if __name__ == "__main__":

    list_username = [
        "whynotnghiavu", 
        "20206205",

        "vvn20206205",
        "hust20206205",
        "vuvannghia452002",
    ]

    print(f"👉 Step: create_git_folder")
    create_git_folder(list_username)

    print(f"👉 Step: create_gitconfig_global")
    create_gitconfig_global(list_username)

    for username in list_username:
        print(f"👉 Step: create_gitconfig_file")
        create_gitconfig_file(username)

    print(f"👉 Step: create_symlink")
    create_symlink(list_username)
