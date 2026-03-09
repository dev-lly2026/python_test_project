import requests
import pytest

# 测试用例1：获取用户信息（GET请求）
def test_get_user_info():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url, timeout=10)
    
    # 断言1：响应状态码为200（请求成功）
    assert response.status_code == 200, f"预期状态码200，实际为{response.status_code}"
    # 断言2：响应数据包含用户姓名（数据有效性）
    assert "name" in response.json(), "响应数据中未找到'name'字段"

# 测试用例2：创建新帖子（POST请求）
def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    # 请求体
    payload = {
        "title": "软件测试接口自动化实践",
        "body": "这是一个用于面试展示的接口测试用例",
        "userId": 1
    }
    response = requests.post(url, json=payload, timeout=10)
    
    # 断言1：响应状态码为201（创建成功）
    assert response.status_code == 201, f"预期状态码201，实际为{response.status_code}"
    # 断言2：响应数据与请求体标题一致
    assert response.json()["title"] == payload["title"], "创建的帖子标题不匹配"

if __name__ == "__main__":
    pytest.main(["-v", "test_demo_api.py"])