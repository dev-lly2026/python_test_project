from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# 夹具：初始化/关闭Edge浏览器
@pytest.fixture(scope="function")
def driver():
    # Selenium 4.6+ 自动识别Scripts目录下的msedgedriver
    driver = webdriver.Edge()
    driver.maximize_window()  # 最大化窗口，避免元素被遮挡
    yield driver
    driver.quit()

# 测试用例：必应搜索功能验证（无弹窗干扰，稳定通过）
def test_bing_search(driver):
    # 访问必应首页（替代百度，解决弹窗问题）
    driver.get("https://cn.bing.com")
    
    # 显式等待：10秒内等待搜索框可见（核心定位：必应搜索框ID为"sb_form_q"）
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "sb_form_q"))
    )
    
    # 执行搜索操作
    search_box.send_keys("软件测试实习")  # 输入求职相关关键词，贴合你的面试场景
    search_box.submit()  # 用回车提交，替代点击按钮，彻底避免点击异常
    
    # 断言：验证搜索结果页标题包含关键词（确保功能正常）
    assert "软件测试实习" in driver.title, "搜索功能失败，标题未匹配目标关键词"