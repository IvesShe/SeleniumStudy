from selenium import webdriver

# 創建WebDriver對象，指明使用Chrome瀏覽器驅動
wd = webdriver.Chrome()

wd.get("https://www.baidu.com")

# 根據id選擇元素，返回的就是該元素對應的WebElement
element = wd.find_element_by_id('kw')

# 通過該WebElement對象，就可以對頁面元素進行操作了
# 比如輸入字符串到這個輸入框里
element.send_keys('IvesShe\n')
# element.send_keys('IvesShe')

# element = wd.find_elements_by_id('su')
# element.click()

# pass