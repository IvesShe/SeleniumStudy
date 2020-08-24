from selenium import webdriver

import time

# 創建WebDriver對象，指明使用Chrome瀏覽器驅動
wd = webdriver.Chrome()

# ------------------------------------------------------

# wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")

# 根據class name選擇元素，返回的是一個列表
# 裡面都是class屬性值為animal的元素對應的WebElement對象
# elements = wd.find_elements_by_class_name('animal')
# for element in elements:
#    print(element.text)

# ------------------------------------------------------

# 尋找單一動物，注意只差一個s
# element = wd.find_element_by_class_name('animal')
# print(element.text)

# ------------------------------------------------------

# elements = wd.find_elements_by_tag_name('span')
# for element in elements:
#    print(element.text)

# ------------------------------------------------------

# 限制 選擇元素的範圍是 id 為 container 元素的內部
# element = wd.find_element_by_id('container')
# spans = element.find_elements_by_tag_name('span')
# for span in spans:
#     print(span.text)

# ======================================================

# 設定默認的等待時間
wd.implicitly_wait(5)

# wd.get("https://www.baidu.com")

# 根據id選擇元素，返回的就是該元素對應的WebElement
# element = wd.find_element_by_id('kw')

# 通過該WebElement對象，就可以對頁面元素進行操作了
# 比如輸入字符串到這個輸入框里
# element.send_keys('IvesShe\n')

# element.send_keys('IvesShe')
# wd.find_elements_by_id('su').click
 

# time.sleep(1)

# id為1的元素，就是第一個搜尋結果 
# element = wd.find_element_by_id('1')

# 打印出第一個搜索結果的文本字符串
# print(element.text)

# 獲取元素屬性的值
# print(element.get_attribute('srcid'))

# wd.quit()

# ------------------------------------------------------
# CSS 表達式

# wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")

# element = wd.find_element_by_css_selector('.plant')
# element = wd.find_element_by_class_name('plant')

# element = wd.find_element_by_css_selector('span')
# print(element.get_attribute('outerHTML'))

# elements = wd.find_elements_by_css_selector('span')
# elements = wd.find_elements_by_css_selector('#searchtext')
# elements = wd.find_elements_by_css_selector('#container > div')
# elements = wd.find_elements_by_css_selector('#layer1 > div')
# elements = wd.find_elements_by_css_selector('#layer1 span')
# elements = wd.find_elements_by_css_selector('span')
# elements = wd.find_elements_by_css_selector('.plant span')
# elements = wd.find_elements_by_css_selector('#container #inner11 > span')
# elements = wd.find_elements_by_css_selector('[href="http://www.miitbeian.gov.cn"]')
# elements = wd.find_elements_by_css_selector('[href]')

# for element in elements:
#     print('-------------------')
#     print(element.get_attribute('outerHTML'))

# ------------------------------------------------------

# wd.get("http://cdn1.python3.vip/files/selenium/sample1a.html")

# # 父元素的第n個子節點
# elements = wd.find_elements_by_css_selector('span:nth-child(2)')

# ------------------------------------------------------

#wd.get("http://cdn1.python3.vip/files/selenium/sample1b.html")

# 依類型的第n個子節點作選擇
# elements = wd.find_elements_by_css_selector('span:nth-of-type(2)')

# 依類型的倒數第n個子節點作選擇
# elements = wd.find_elements_by_css_selector('span:nth-last-of-type(2)')

# elements = wd.find_elements_by_css_selector('#t2 :nth-child(even')

# ------------------------------------------------------

wd.get("http://cdn1.python3.vip/files/selenium/sample2.html")

# wd.switch_to_frame('frame1')
# elements = wd.find_elements_by_css_selector('.plant')

# 切換到frame裡面去
wd.switch_to_frame(wd.find_element_by_css_selector('iframe[src="sample1.html"]'))
elements = wd.find_elements_by_css_selector('.plant')

for element in elements:
    print('-------------------')
    print(element.get_attribute('outerHTML'))

# 切換到外層
wd.switch_to_default_content()
wd.find_element_by_id('outerbutton').click()    

wd.quit()


#pass
