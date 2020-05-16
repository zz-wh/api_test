from hyrobot.common import *
from lib.webui import  *
from time import sleep
import os


class c1:
    name = 'UI-0001' # 测试用例名字

    # 测试用例步骤
    def teststeps(self):

        STEP(1, '登陆网站')

        wd = open_browser()
        wd.set_window_size(1903,894)
        mgr_login(wd)
        wd.assertEqual(2+2,4)

        # STEP(2, '点击系统管理')
        # wd.find_element_by_class_name("head_right_span1").click()
        # sleep(3)
        # wd.find_element_by_link_text("系统管理").click()
        # sleep(5)
        #
        # STEP(3, '添加场景并保存')
        # wd.find_element_by_link_text("场景管理").click()
        # sleep(5)
        # wd.find_element_by_css_selector("#add_scenario").click()
        # sleep(5)
        # wd.find_element_by_css_selector("body > div.control_main > ul > li.right.relative > div.equip_topo_add > ul.topology_detail_2 > li > span.detail_2_spanstyle > input").send_keys("测试场景")
        # sleep(5)
        # wd.find_element_by_css_selector("#saveBtn").click()
        # sleep(5)

        # STEP(4, '验证场景名称是否保存成功')
        # item = wd.find_elements_by_class_name('search-result-item')[0]
        #
        # fields = item.find_elements_by_tag_name('span')[:6]
        #
        # texts = [field.text for field in fields]
        # print(texts)






