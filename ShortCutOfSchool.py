from selenium.webdriver import Chrome
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

#健康系统自动填报模块 time：2020/12/01 year
#author hua 基于selenium

ok = False

def tow():
    # 第二个模块体温提交点击确定
    time.sleep(0.5)
    chrome.find_element_by_class_name('layui-m-layerbtn').click()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '体温提交完成。')
    return True

def one():
    #第一个模块填报完成点击确定
    time.sleep(0.5)
    chrome.find_element_by_tag_name('span').click()
    # chrome.find_element_by_class_name('layui-m-layerbtn').click()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '今天的健康情况已经填报完成。')
    return True

def isElementPresent(value):
    #判断是否有某个元素
    try:
        # element = self.driver.find_element(by=by, value=value) self, by,
        chrome.find_element_by_tag_name(value)
    except NoSuchElementException as e:
        return False
    else:
        return True

#指定目标驱动
from selenium import webdriver
chrome_driver="D:\TestForUrllib\selenium\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver)

# chrome = Chrome()
chrome = driver

chrome.get('http://xgxlsg.cqbvc.edu.cn:17535/SPCP/Web/')
chrome.find_element_by_id('StudentId').send_keys('学号')
chrome.find_element_by_id('Name').send_keys('密码')
y = chrome.find_element_by_id('code-box').text
chrome.find_element_by_id('codeInput').send_keys(y)
chrome.find_element_by_id('Submit').click()
time.sleep(0.5)
chrome.find_element_by_id('platfrom2').click()

done = isElementPresent('form')
if(done) :
    # 进行填报
    print("进入填报ing")
    selectBtn = Select(chrome.find_element_by_name('County'))
    selectBtn.select_by_index(1)
    chrome.find_element_by_id('ckCLS').click()
    chrome.find_element_by_class_name('save_form').click()
    ok = True
    print("填报完成")
    time.sleep(0.5)
    ok = one()
else:
    # 已经提交过今天的报告
    time.sleep(0.5)
    ok = one()

time.sleep(0.5)
chrome.find_element_by_id('platfrom1').click()

done = isElementPresent('form')
if(done) :
    print('体温填报ing')
    selectBtn = Select(chrome.find_element_by_name('Temper1'))
    selectBtn.select_by_index(3)
    selectBtn = Select(chrome.find_element_by_name('Temper2'))
    selectBtn.select_by_index(6)
    chrome.find_element_by_class_name('save_form').click()
    ok = True
    time.sleep(0.5)
    ok = tow()
else:
    time.sleep(0.5)
    ok = tow()

if(ok) :
    chrome.quit()
    print('您已完成今天所有填报任务！！')