# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:31:48 2022
@author: ASUS
"""
#获取你的综合素质分-
#先访问网站http://a.cqie.edu.cn/cas/login?service=http%3A%2F%2Fi.cqie.edu.cn%2Fportal_main%2FtoPortalPage
#输入账号和密码
from selenium.webdriver import Chrome,ChromeOptions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import sys
import pandas as pd
    #——————————————登录功能——————————————
username=input("请输入账号:")
password=input('请输入密码:')
opt=ChromeOptions()
    #创建参数对象
    #opt.headless=True
opt.headless=True  #浏览器设置成无界面模式
opt.add_argument('headless')
    #创建参数对象
#
wd=webdriver.Chrome(executable_path=r'C:\Users\ASUS\.wdm\drivers\chromedriver\win32\chromedriver.exe')

# wd=webdriver.Chrome(executable_path=r'C:\Users\ASUS\.wdm\drivers\chromedriver\win32\105.0.5195.52\.wdm\drivers\chromedriver\win32\107.0.5304.62\chromedriver.exe')
wd.get("http://a.cqie.edu.cn/cas/login?service=http%3A%2F%2Fi.cqie.edu.cn%2Fportal_main%2FtoPortalPage") #打开百度网盘
wd.implicitly_wait(5)
   # wd.find_element(By.XPATH,"//*[@id='pass_phoenix_btn']/ul/li[2]/a").click()

wd.find_element(By.ID,"username").send_keys(username)#发送数据
time.sleep(1)
wd.find_element(By.ID,"password").send_keys(password)#发送密码
time.sleep(0.5)

a=wd.find_elements(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/div[7]/a[1]")[0]
#a=a[0]
a.click()
time.sleep(1)
wd.implicitly_wait(5)
#打开网页后
#获取姓名



def zongcefen():
    try:
        your_name=wd.find_element(By.XPATH,"//*[@id='login_id']").text
        b=wd.find_elements(By.XPATH,'//*[@id="hdxx"]/div/div[1]/a')[0]
        b.click()
    except:
        print("密码或账号错误")
        sys.exit()
#打开更多后
    time.sleep(0.5)
    wd.implicitly_wait(5)
    new_window=wd.window_handles[-1]
    wd.switch_to.window(new_window)
    
    wd.find_element(By.ID,"wdxxhd").click()
    time.sleep(1)
    #我的线下活动
    rows=wd.find_elements(By.XPATH,'//*[@id="tbody"]')
    #print(rows)
    thisdatas=[]
    #继续BUG
    result=[]
    df1 = pd.DataFrame(data=result,
                       columns=['活动名称', '活动类别','活动大类','活动学年',
                                '活动学期','积分/学时'])
    name=[]
    active_class=[]
    act_big=[]
    act_age=[]
    act_item=[]
    act_count=[]
    max_Page=wd.find_element(By.XPATH,"//*/font[@id='maxPage']").text
    click_count=wd.find_element(By.XPATH,"//*[@id='footer']/div/ul/li[4]/a")
    from io import StringIO
    print("<程序正在读取数据，请稍后…………>\n")
    for l in range(0,int(max_Page)):
        wd.implicitly_wait(1)
        for row in rows:
            row1=row.find_elements(By.XPATH,"./tr")
            #print(row1)
            for i in row1:
                #print(i)
                name.append(i.find_element(By.XPATH,"./td[1]").text)
                active_class.append(i.find_element(By.XPATH,"./td[2]").text)
                act_big.append(i.find_element(By.XPATH,"./td[3]").text)
                act_age.append(i.find_element(By.XPATH,"./td[4]").text)
                act_item.append(i.find_element(By.XPATH,"./td[5]").text)
                act_count.append(i.find_element(By.XPATH,"./td[6]").text)
                #翻页 
        click_count.click()
        time.sleep(1)
    name=pd.Series(data=name)
    active_class=pd.Series(data=active_class)
    act_big=pd.Series(data=act_big)
    act_age=pd.Series(data=act_age)
    act_item=pd.Series(data=act_item)
    act_count=pd.Series(data=act_count)
    df=pd.concat([name,active_class],axis=1,join='outer')
    df1=pd.concat([df,act_big],axis=1,join='outer')
    df2=pd.concat([df1,act_age],axis=1,join='outer')
    df3=pd.concat([df2,act_item],axis=1,join='outer')
    df4=pd.concat([df3,act_count],axis=1,join='outer')
    df4.columns=['活动名称', '活动类别','活动大类','活动学年','活动学期','积分/学时']
    df=df4
    #search_item=
    #print("请选择要查询的年份：\n")
    #print("<1> "
    #search_age=input("")
    #search_class=input("请输入需要查询的类别:分别为[A]、[B]、[C]、[D]、[劳动]、[社会实践]")
    
    print(your_name)
    #开始查询
    print("请选择要查询的年份：学期、以及查询类型")
    Flag=1
    while Flag==1:
        flag=1
        while flag==1:
            try:
                select_age=int(input("<1>2020-2021       <2>2021-2022      <3>2022-2023\n"))
                if select_age==1:
                    select_age='2020 - 2021'
                    flag=2
                elif select_age==2:
                    select_age='2021 - 2022'
                    flag=2
                elif select_age == 3:
                    select_age='2022 - 2023'
                    flag = 2
                else:
                    print("请选择正确的值")
            except:
                print("请输入数字并回车确定")
        
        flag1=1
        while flag1==1:
            try:
                select_item=int(input("<1>第一学期       <2>第二学期\n"))
                if select_item==1:
                    select_item='第一学期'
                    flag1=2
                elif select_item==2:
                    select_item='第二学期'
                    flag1=2
                else:
                    print("请选择正确的值")
            except:
                print("请输入数字并回车确定")
        #A类
        print(your_name)
        yours_grade=df[(df.活动学年==select_age)&(df.活动学期==select_item)&(df.活动类别=='A类思想品德素质')]
        yours_grade['积分/学时']=yours_grade['积分/学时'].astype(float)
        your_count=yours_grade['积分/学时'].sum()
        print('%s %s 您的A类总分为：%d'%(select_age,select_item,your_count))
        A_count=your_count
        #B类
        yours_grade=df[(df.活动学年==select_age)&(df.活动学期==select_item)&(df.活动类别=='B类科学文化素质')]
        yours_grade['积分/学时']=yours_grade['积分/学时'].astype(float)
        your_count=yours_grade['积分/学时'].sum()
        print('%s %s 您的B类总分为：%d'%(select_age,select_item,your_count))
        B_count=your_count
        #C类
        yours_grade=df[(df.活动学年==select_age)&(df.活动学期==select_item)&(df.活动类别=='C类身体心理素质')]
        yours_grade['积分/学时']=yours_grade['积分/学时'].astype(float)
        your_count=yours_grade['积分/学时'].sum()
        print('%s %s 您的C类总分为：%d'%(select_age,select_item,your_count))
        C_count=your_count
        #D类
        yours_grade=df[(df.活动学年==select_age)&(df.活动学期==select_item)&(df.活动类别=='D类就业创业能力')]
        yours_grade['积分/学时']=yours_grade['积分/学时'].astype(float)
        your_count=yours_grade['积分/学时'].sum()
        print('%s %s 您的D类总分为：%d'%(select_age,select_item,your_count))
        D_count=your_count
        if A_count>100:
            A_count=100
        if B_count>100:
            B_count=100
        if C_count>100:
            C_count=100
        if D_count>100:
            D_count=100
        print("素质分为：%.2f" %(A_count*0.35+B_count*0.3+C_count*0.2+D_count*0.15))
        try:
                sele=int(input("<1>继续查询其他年份       <2>退出\n"))
                if sele==1:
                    Flag=1
                elif sele==2:
                    Flag=2
                else:
                    print("请选择正确的值")
        except:
                print("请输入数字并回车确定")
        

zongcefen()
