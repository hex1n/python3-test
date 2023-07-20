

import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By

from name import RandomUtil
from phoneNum import create_phone
from selenium.webdriver.chrome.options import Options


import datetime
import time

# target_time = datetime.datetime.combine(datetime.date.today(), datetime.time(0, 0))
# target_time += datetime.timedelta(days=1)  # 将目标时间设置为明天的午夜




options = Options()
# o.add_argument('--incognito') #无痕模式
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options, )
driver.maximize_window()  # 设置打开页面最大化,目的是更好的截取错误图

fileAddr='/Users/hex1n/Pictures/aa/'

def loop_work():
    driver.get("http://hubei.123js.cn/Computer2_Redis/Repair.aspx?DSID=124&uid=")

    # driver.get("http://hubei.123js.cn/Computer2_Redis/Repair.aspx?DSID=124&uid=")

    input_box = driver.find_element(By.ID, 'txtvcLoginDesc1')  # 获取首页输入框元素

    input_box.send_keys(RandomUtil().random_name_str('男'))  # 向输入框中输入内容

    input_box2 = driver.find_element(By.ID, 'ddlvcLoginDesc3')  # 获取首页输入框元素
    input_box2.click()  # 点击搜索按钮
    input_box2.send_keys('郑州市')  # 向输入框中输入内容

    input_box3 = driver.find_element(By.ID, 'sltBranch1')  # 获取首页输入框元素
    time.sleep(1)
    input_box3.click()  # 点击搜索按钮
    input_box3.send_keys('金水区')  # 向输入框中输入内容

    input_box2 = driver.find_element(By.ID, 'sltBranch2')  # 获取首页输入框元素
    time.sleep(1)
    input_box2.click()  # 点击搜索按钮
    input_box2.send_keys('未来路街道办事处')  # 向输入框中输入内容

    input_box2 = driver.find_element(By.ID, 'txtvcLoginDesc4')  # 获取首页输入框元素

    input_box2.send_keys('名门')  # 向输入框中输入内容

    input_box2 = driver.find_element(By.ID, 'txtvcLoginDesc7')  # 获取首页输入框元素
    phoneNum = create_phone()
    input_box2.send_keys(phoneNum)  # 向输入框中输入内容

    input_box2 = driver.find_element(By.ID, 'ddlvcLoginDesc15')  # 获取首页输入框元素

    input_box2.send_keys('18-60岁')  # 向输入框中输入内容

    input_box2 = driver.find_element(By.ID, 'ddlvcLoginDesc16')  # 获取首页输入框元素

    input_box2.send_keys('城镇居民')  # 向输入框中输入内容  find_elements_by_tag_name

    search_button = driver.find_element(By.ID, 'a_btn')  # 获取开始答题按钮元素

    search_button.click()  # 点击开始答题

    time.sleep(1)
    counta = 0
    while (counta < 5):
        # 第一题
        counta += 1
        print("第"+str(counta)+"题")
        time.sleep(1)
        div= driver.find_element(By.ID,'type_div')
        if(div.text!='多选'):
            driver.find_element(By.CLASS_NAME, 'noselectDiv').click()
        else:
            driver.find_element(By.CLASS_NAME, 'noselectDiv1').click()
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, 'noselectDiv1').click()

        # 下一题
        driver.find_element(By.ID, 'a_btn').click()
        time.sleep(2)
    inputTag = driver.find_element(By.XPATH, 'html/body/div/div/input')
    print(inputTag.text)
    inputTag.click()
    # 滚动页面
    driver.execute_script("window.scrollTo(0, 300);")
    name= fileAddr + phoneNum + '.png'
    print(name)
    driver.get_screenshot_as_file(name)




# count=0
# while datetime.datetime.now() < target_time:
#     # 在这里编写需要执行的程序代码
#     print("程序正在运行..."+"现在时间--"+str(datetime.datetime.now())+"--目标时间"+str(target_time))
#     count += 1
#     print("开始第" + str(count) + "个")
#     try:
#         loop_work()
#     except Exception as e:
#         print(traceback.format_exc())
#         count -= 1
#         continue
#
#     # 可以在程序中设置条件来判断是否需要提前退出
#     # 程序运行完一次后休眠一段时间
#     time.sleep(1)



count = 0
while True:
    now = datetime.datetime.now()
    start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(5, 0))  # 早上5点
    end_time = datetime.datetime.combine(datetime.date.today(), datetime.time(23, 58))  # 晚上12点
    print("程序正在运行..." + "现在时间--" + str(now) + "--运行时间：" + str(start_time) + '到' + str(end_time))

    if start_time <= now <= end_time:
        # 在时间范围内执行你的代码
        count += 1
        print("开始第" + str(count) + "个")
        try:
            loop_work()
        except Exception as e:
            print(traceback.format_exc())
            count -= 1
            continue

        # 可以在程序中设置条件来判断是否需要提前退出
        # 程序运行完一次后休眠一段时间
        time.sleep(1)
    else:
        print('不在运行时间范围内-------')
        # 在时间范围外等待直到达到下一个早上5点
        next_start_time = start_time if now < start_time else start_time + datetime.timedelta(days=1)
        wait_time = (next_start_time - now).seconds
        print('下一次开始运行时间-------' + str(next_start_time))
        print('等待时间-------' + str(wait_time))
        time.sleep(wait_time)



# 当时间达到或超过目标时间时，程序将停止运行
print("程序已停止")
driver.quit()

# count=0
# while(count < 200):
#     count+=1
#     print("开始第"+ str(count)+"个")
#     try:
#         loop_work()
#     except Exception as e:
#         print(traceback.format_exc())
#         count -= 1
#         continue
#
#
# print('循环结束------------'+str(count))
# driver.quit()




print("done.......")



# driver.switch_to.window(driver.window_handles[-1])


# 开始答题

# input_box2 = driver.find_element(By.TAG_NAME, 'C') # 获取首页输入框元素

# driver.find_element(By.TAG_NAME, 'A')

# input_box2.click() # 向输入框中输入内容  find_elements_by_tag_name

# driver.set_script_timeout(5) #设置脚本延时五秒后执行
#
# driver.quit() #关闭浏览器并关闭驱动
