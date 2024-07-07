from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from tqdm import tqdm

IF_HEADLESS = False  # 是否以无窗口模式运行（首次运行建议使用有窗口模式以观察是否符合预期）
COURSE_URL = 'https://course.hitsz.edu.cn/pro/lms/BMrkCZUnBsi/17121246/studycontent'  # 要刷的课的地址（获取方式见README）
COOKIE = 'c76eq11m1hxjgsxp0khn4cmogrf98f2l'  # 打死也不要告诉别人哦（获取方式见README）这只是样例


option = webdriver.ChromeOptions()

if IF_HEADLESS:
    option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.maximize_window()
IMPLICITLY_WAIT = 10
driver.implicitly_wait(IMPLICITLY_WAIT)


def setCookie(cookies):
    driver.delete_all_cookies()
    for name, value in cookies.items():
        driver.add_cookie({'name': name, 'value': value, 'path': '/'})

homePageURL = 'https://' + COURSE_URL.split('https://')[1].split('/')[0] + '/'
driver.get(homePageURL)
setCookie({'sessionid': COOKIE})
driver.get(COURSE_URL)
sleep(3)
if 'pro/portal/home' in driver.current_url:
    print('cookie失效或设置有误，请重设cookie或选择每次扫码登录')
    driver.get(homePageURL)
    driver.find_element(By.CLASS_NAME, 'login-btn').click()
    print("请扫码登录")
    while 'courselist' not in driver.current_url:  # 判断是否已经登录成功
        sleep(0.5)
    print('登录成功')
    driver.get(COURSE_URL)

answer=[[] for _ in range(200)]
def grabanswer():
    #sleep(5)
    allHomework = driver.find_elements(By.CLASS_NAME, "icon--zuoye")
    print('正在获取答案，请耐心等待')
    global n
    n=-1  #第几个作业
    for icon in tqdm(allHomework):
        print(end='\n') 
        sleep(0.5)
        
        icon.click()
        all_windows = driver.window_handles
        n+=1
        if len(all_windows) > 1:
            # 切换到新窗口
            new_window = all_windows[-1]  # 假设新窗口是最后一个打开的窗口
            driver.switch_to.window(new_window)
            
            #切换题号
            buttons = driver.find_elements(By.CLASS_NAME, 'subject-item')
            # 依次点击每个按钮
            for i in range(0,len(buttons)-1):
                button=buttons[i]
                button.click()
                #查找内容
                
                #请按需修改xpath
                target_div = driver.find_elements(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[3]/div/div/div[3]/div')
                target_div1 = driver.find_elements(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[3]/div/div/div[3]/div')
                
                if target_div:  # 如果列表不为空
                    ans1=str(target_div[0].text)
                    answer[n].append(ans1)
                    print(answer[n][-1][5:])
                elif target_div1:
                    # print(taeget_div1[0].text)
                    ans1=str(target_div1[0].text)
                    answer[n].append(ans1)
                    print(answer[n][-1][5:])
                else:
                    raise Exception("没有找到匹配的元素。")
                sleep(0.5)

            # 关闭当前窗口
            driver.close()
            # 切换回之前的窗口，假设之前的窗口是列表中的倒数第二个
            previous_window = all_windows[-2]
            driver.switch_to.window(previous_window)
        
    return False


while grabanswer():
    driver.refresh()
driver.quit()

digit_map = {
    1: '一', 2: '二', 3: '三', 4: '四',
    5: '五', 6: '六', 7: '七', 8: '八',
    9: '九', 10: '十', 11: '十一', 12: '十二',
    13: '十三', 14: '十四', 15: '十五', 16: '十六',
    17: '十七'
}

#输出格式，请自行修改
with open('answer.txt', 'w') as file:
    N=1
    num=1
    file.write(digit_map[N])
    file.write('\n')
    N+=1
    for i in range(0,n+1):
        if(i!=0 and len(answer[i-1])==20):
            file.write('\n')
            file.write(digit_map[N])
            file.write('\n')
            N+=1
            if(N==11): N+=1
            num=1
        file.write(str(num)+'、 ')
        num+=1
        for j in range(0,len(answer[i])):
            file.write(str(j+1)+'.'+str(answer[i][j][5:])+' ')
        file.write('\n')

print('恭喜！答案获取完毕')