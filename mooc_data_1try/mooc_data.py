import time,re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pandas import DataFrame, read_csv
import pandas as pd 

def getMoocDataCourse():
    browser = webdriver.Chrome()

    #urlAll ='https://www.icourse163.org/category/all'
    urlJingpin = 'https://www.icourse163.org/category/guojiajingpin'
    urlComputer = 'https://www.icourse163.org/category/computer'
    urlManager = 'https://www.icourse163.org/category/eco-management'
    urlPsyco = 'https://www.icourse163.org/category/psychology'
    urlForeign = 'https://www.icourse163.org/category/foreign-language'
    urlHistory = 'https://www.icourse163.org/category/literary-history'
    urlDesign = 'https://www.icourse163.org/category/art-design'
    urlEngineer = 'https://www.icourse163.org/category/engineering'
    urlScience = 'https://www.icourse163.org/category/science'
    urlBio = 'https://www.icourse163.org/category/biomedicine'
    urlPhilo = 'https://www.icourse163.org/category/philosophy'
    urlLaw = 'https://www.icourse163.org/category/law'
    urlTeaching = 'https://www.icourse163.org/category/teaching-method'

    categotyUrl = urlJingpin
    browser.get(categotyUrl)
    wait = WebDriverWait(browser, 10)

    totalNumberStr = browser.find_element_by_css_selector('#j-result-view > div.m-tag-bar.f-cb > ul.u-tag-left.f-f0.f-fl.f-cb > li.f-fl.ga-click.cur.border-right').text
    totalNumber = int(re.search('\d+', totalNumberStr).group())
    pageNumber = int(totalNumber/20) + 1
    print(pageNumber)
    allCourseInfo = []


    for j in range (int(pageNumber) - 1):
        """         nextUrl = str(categotyUrl) + '#?type=30&orderBy=0&pageIndex=' + str(j + 1)
        print(nextUrl)
        browser.get(nextUrl) """
        windowAll=browser.current_window_handle 

        sleep(5)

        classNameNode = browser.find_element_by_class_name('m-course-list')
        classNodeId = re.search('\d+',classNameNode.get_attribute("id")).group()

        for i in range (20):
            nodeStr = '#auto-id-' + classNodeId + '> div > div:nth-child(' + str(i+1) +') > div.g-mn1 > div > div > div.t1.f-f0.f-cb.first-row > a:nth-child(1)'

            try:
                browser.find_element_by_css_selector(nodeStr)
                a = True
            except:
                a = False

            if a == True:
                submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, nodeStr)))
                submit.click()    
                windows = browser.window_handles
                for window in windows:
                    if window != windowAll:
                        browser.switch_to.window(window)

                sleep(2) 

                try:
                    browser.find_elements_by_class_name('u-icon-thin-caret-down')
                    a = True
                except:
                    a = False
                    print('@@@@@@@@@@@@@@@')
                
                if (a == True):
                    moreSubmits = browser.find_elements_by_class_name('u-icon-thin-caret-down')
                    for moreSubmit in moreSubmits:
                        try: 
                            moreSubmit.click()
                        except:
                            print('not clibable')




                """                 try: 
                    browser.find_element_by_class_name('cover-overflow-wrapper_btn j-btn')
                    a = True
                except: 
                    a = False

                if a == True:
                    moreNode = browser.find_element_by_class_name('cover-overflow-wrapper_btn j-btn')
                    moreNodeId = re.search('\d+',moreNode.get_attribute("id")).group()
                    moreNodeStr = '#auto-id-' + str(moreNodeId)
                    submitMore = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, moreNodeStr)))
                    submitMore.click()  """

                courseName = ''
                courseLink = ''
                courseIntro = ''
                courseBook = ''
                courseSchool = ''
                courseAgenda = ''
                coursePreKnowledge = ''
                
                courseNameNode = browser.find_element_by_css_selector('#g-body > div.m-top.f-cb.f-pr.f-f0 > div > div.g-mn1.course-enroll-info-wrapper > div > div.f-cb.f-pr > div.f-fl.course-title-wrapper > span.course-title.f-ib.f-vam')
                courseName = courseNameNode.text

                courseLink = browser.current_url

                courseIntroNode = browser.find_element_by_css_selector('#content-section > div:nth-child(4) > div')
                courseIntro = courseIntroNode.text

                for k in range (15):
                    node = '#content-section > div:nth-child(' + str(k) + ') > span:nth-child(2)'
                    try: 
                        browser.find_element_by_css_selector(node)
                        a = True
                    except: 
                        a = False

                    if a == True:
                        check = browser.find_element_by_css_selector(node)
                        if (check.text == '课程大纲'):
                            courseAgendaNode = browser.find_element_by_css_selector('#content-section > div:nth-child(' + str(k+1) +') > div.f-richEditorText')
                            courseAgenda = courseAgendaNode.text

                courseSchoolNode = browser.find_element_by_css_selector('#g-body > div.g-flow > div.g-wrap.f-cb > div.g-sd2.m-sd2 > div.m-sdinfo > div.f-bgw > div > a > img')
                courseSchool = courseSchoolNode.get_attribute('alt')

                for k in range (15):
                    node = '#content-section > div:nth-child(' + str(k) + ') > span:nth-child(2)'
                    try: 
                        browser.find_element_by_css_selector(node)
                        a = True
                    except: 
                        a = False

                    if a == True:
                        check = browser.find_element_by_css_selector(node)
                        if (check.text == '预备知识'):
                            coursePreKnowledgeNode = browser.find_element_by_css_selector('#content-section > div:nth-child(' + str(k+1) + ') > div')
                            coursePreKnowledge = coursePreKnowledgeNode.text

                for k in range (15):
                    node = '#content-section > div:nth-child(' + str(k) + ') > span:nth-child(2)'
                    try: 
                        browser.find_element_by_css_selector(node)
                        a = True
                    except: 
                        a = False

                    if a == True:
                        check = browser.find_element_by_css_selector(node)
                        if (check.text == '参考资料'):
                            courseBookNode = browser.find_element_by_css_selector('#content-section > div:nth-child(' + str(k+1) +') > div.f-richEditorText')
                            courseBook = courseBookNode.text
                        
                """                 try:
                    browser.find_element_by_css_selector('#content-section > div:nth-child(12) > div > p:nth-child(1)')
                    b = True
                except:
                    b = False
                if b == True:
                    courseBookNode = browser.find_element_by_css_selector('#content-section > div:nth-child(12) > div > p:nth-child(1)')
                    courseBook = courseBookNode.text """

                #courseAgendaNode = browser.find_element_by_css_selector('#content-section > div:nth-child(8) > div.f-richEditorText')
                #courseAgenda = courseAgendaNode.text

                """                 try:
                    browser.find_element_by_css_selector('#content-section > div:nth-child(10) > div')
                    c = True
                except:
                    c = False
                if c == True:
                    coursePreKnowledgeNode = browser.find_element_by_css_selector('#content-section > div:nth-child(10) > div')
                    coursePreKnowledge = coursePreKnowledgeNode.text """

                courseInfo = [courseName, courseLink, courseIntro, courseSchool, courseBook, courseAgenda, coursePreKnowledge]
                #print(courseInfo)

                allCourseInfo.append(courseInfo)

                browser.close()

                browser.switch_to.window(windowAll)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        nextSubmit = browser.find_element_by_css_selector('#j-courseCardListBox > div.course-card-list-pager.ga-click.f-f0 > ul > li.ux-pager_btn.ux-pager_btn__next > a')
        nextSubmit.click()
    df = pd.DataFrame(data = allCourseInfo, columns=['courseName', 'courseLink', 'courseIntro', 'courseSchool', 'courseBook', 'courseAgenda', 'coursePreKnowledge'])  
    df.to_csv('Jingpin.csv', index=False, header=['courseName', 'courseLink', 'courseIntro', 'courseSchool', 'courseBook', 'courseAgenda', 'coursePreKnowledge'])
    print(len(allCourseInfo))
    """ 
    
    df = pd.DataFrame(data = allCourseInfo, columns=['courseName', 'courseLink', 'courseIntro', 'courseSchool', 'courseBook', 'courseAgenda', 'coursePreKnowledge'])  
    df.to_csv('Foreign.csv', index=False, header=['courseName', 'courseLink', 'courseIntro', 'courseSchool', 'courseBook', 'courseAgenda', 'coursePreKnowledge'])
    """
if __name__ == "__main__":
    getMoocDataCourse()
