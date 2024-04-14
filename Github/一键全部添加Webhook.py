import requests
import json


def 创建Webhook(repo_name, webhook_url, access_token):
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "name": "web",
        "active": True,
        "events": ["*"],
        "config": {"url": webhook_url, "content_type": "json"},
    }
    response = requests.post(
        f"https://api.github.com/repos/{repo_name}/hooks",
        headers=headers,
        data=json.dumps(data),
    )
    if response.status_code == 201:
        print(f"成功创建 {repo_name} 的Webhook")
    else:
        print(f"无法为 {repo_name} 创建Webhook。状态码: {response.status_code}")
        print(response.text)


def 主函数():
    # GitHub访问令牌（需要具有repo范围）
    access_token = "这里改成你的GitHub访问令牌"
    # Webhook URL
    webhook_url = "这里改成你的Webhook URL"

    # 获取仓库列表
    response = requests.get(
        "https://api.github.com/user/repos",
        headers={"Authorization": f"token {access_token}"},
    )
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            repo_name = repo["full_name"]
            创建Webhook(repo_name, webhook_url, access_token)
    else:
        print(f"无法获取仓库列表。状态码: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    主函数()
