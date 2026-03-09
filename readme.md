# Python 自动化测试项目
软件测试实习面试展示项目

## 技术栈
- Python 3.14
- pytest
- Selenium + Edge 浏览器
- requests
- pytest-html 测试报告

## 项目1：UI 自动化测试 (ui_auto_test)
- 实现 Edge 浏览器自动化操作
- 测试必应搜索功能
- 生成 HTML 测试报告

## 项目2：接口自动化测试 (api_auto_test)
- GET 请求：获取用户信息
- POST 请求：创建新帖子
- 对响应状态码和数据进行断言

## 运行结果截图
![项目运行结果](https://github.com/你的用户名/python_test_project/raw/main/all_result.jpg)
![UI测试报告](https://github.com/你的用户名/python_test_project/raw/main/report.jpg)

## 运行命令
```bash
# UI 自动化测试
cd ui_auto_test
pytest test_bing_search.py -v --html=report.html

# 接口自动化测试
cd api_auto_test
pytest test_demo_api.py -v