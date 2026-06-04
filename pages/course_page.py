import allure
import time
from pages.base_page import BasePage


class CoursePage(BasePage):
    # 课程页面元素定位器（根据实际页面结构）
    
    # 添加课按钮
    ADD_COURSE_BUTTON = 'button:has-text("添加课")'
    
    # 课名称输入框 - 通过ng-model定位
    COURSE_NAME_INPUT = 'input[ng-model="addData.name"]'
    
    # 详情描述输入框 - 通过ng-model定位
    COURSE_DESC_INPUT = 'textarea[ng-model="addData.desc"]'
    
    # 展示次序输入框 - 通过ng-model定位
    DURATION_INPUT = 'input[ng-model="addData.display_idx"]'
    
    # 创建按钮
    SUBMIT_BUTTON = 'button:has-text("创建")'
    
    # ==================== 编辑功能相关元素 ====================
    
    # 编辑按钮 - 通用选择器
    EDIT_BUTTON = 'button:has-text("编辑")'
    
    # 编辑表单 - 次序输入框
    EDIT_DISPLAY_IDX_INPUT = 'input[ng-model="editOne.display_idx"]'
    
    # 编辑表单 - 名称输入框
    EDIT_NAME_INPUT = 'input[ng-model="editOne.name"]'
    
    # 编辑表单 - 描述输入框
    EDIT_DESC_INPUT = 'textarea[ng-model="editOne.desc"]'
    
    # 确定按钮
    CONFIRM_BUTTON = 'button:has-text("确定")'
    
    # ==================== 删除功能相关元素 ====================
    
    # 删除按钮 - 通用选择器
    DELETE_BUTTON = 'button:has-text("删除")'
    
    # 确认删除对话框 - 确定按钮
    CONFIRM_DELETE_BUTTON = 'button:has-text("确定")'

    @allure.step("点击添加课按钮")
    def click_add_course(self):
        self.page.wait_for_selector(self.ADD_COURSE_BUTTON, state='visible')
        self.click(self.ADD_COURSE_BUTTON)
        # 等待表单出现
        self.page.wait_for_timeout(2000)

    @allure.step("输入课名称: {name}")
    def enter_course_name(self, name: str):
        self.fill(self.COURSE_NAME_INPUT, name)

    @allure.step("输入详情描述: {desc}")
    def enter_course_desc(self, desc: str):
        self.fill(self.COURSE_DESC_INPUT, desc)

    @allure.step("输入展示次序: {duration}")
    def enter_duration(self, duration: str):
        self.fill(self.DURATION_INPUT, duration)

    @allure.step("点击创建按钮")
    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)

    @allure.step("添加课程")
    def add_course(self, name: str, desc: str, duration: str):
        self.click_add_course()
        self.enter_course_name(name)
        self.enter_course_desc(desc)
        self.enter_duration(duration)
        self.click_submit()

    @allure.step("生成带时间戳的课程名称")
    def generate_course_name(self, base_name: str = "测试") -> str:
        timestamp = int(time.time())
        return f"{base_name}{timestamp}"

    @allure.step("验证添加课程成功")
    def verify_course_added(self):
        self.page.wait_for_load_state("networkidle")

    # ==================== 编辑功能方法 ====================
    
    @allure.step("点击第一个编辑按钮")
    def click_first_edit_button(self):
        # 先等待编辑按钮可见
        self.page.wait_for_selector(self.EDIT_BUTTON, state='visible')
        # 点击第一个编辑按钮
        edit_buttons = self.page.locator(self.EDIT_BUTTON).all()
        if edit_buttons:
            edit_buttons[0].click()
            self.page.wait_for_timeout(2000)

    @allure.step("编辑课程 - 输入次序: {display_idx}")
    def enter_edit_display_idx(self, display_idx: str):
        self.page.wait_for_selector(self.EDIT_DISPLAY_IDX_INPUT, state='visible')
        # 先清空输入框
        self.page.locator(self.EDIT_DISPLAY_IDX_INPUT).fill('')
        self.page.wait_for_timeout(100)
        # 再输入新值
        self.fill(self.EDIT_DISPLAY_IDX_INPUT, display_idx)

    @allure.step("编辑课程 - 输入名称: {name}")
    def enter_edit_name(self, name: str):
        self.page.wait_for_selector(self.EDIT_NAME_INPUT, state='visible')
        self.page.locator(self.EDIT_NAME_INPUT).fill('')
        self.page.wait_for_timeout(100)
        self.fill(self.EDIT_NAME_INPUT, name)

    @allure.step("编辑课程 - 输入描述: {desc}")
    def enter_edit_desc(self, desc: str):
        self.page.wait_for_selector(self.EDIT_DESC_INPUT, state='visible')
        self.page.locator(self.EDIT_DESC_INPUT).fill('')
        self.page.wait_for_timeout(100)
        self.fill(self.EDIT_DESC_INPUT, desc)

    @allure.step("点击确定按钮")
    def click_confirm_button(self):
        self.page.wait_for_selector(self.CONFIRM_BUTTON, state='visible')
        self.click(self.CONFIRM_BUTTON)

    @allure.step("编辑课程完整流程")
    def edit_course(self, display_idx: str, name: str, desc: str):
        self.click_first_edit_button()
        self.enter_edit_display_idx(display_idx)
        self.enter_edit_name(name)
        self.enter_edit_desc(desc)
        self.click_confirm_button()
    
    # ==================== 删除功能方法 ====================
    
    @allure.step("点击包含指定课程名称行的删除按钮")
    def click_delete_button_by_name(self, course_name: str):
        """根据课程名称找到对应的行并点击删除按钮"""
        # 等待课程列表加载
        self.page.wait_for_selector("tbody tr", state='visible')
        
        # 遍历所有行，找到包含指定课程名称的行
        rows = self.page.locator("tbody tr").all()
        
        for i, row in enumerate(rows):
            row_text = row.inner_text()
            if course_name in row_text:
                print(f"找到课程 '{course_name}' 在第 {i+1} 行")
                # 找到该行的删除按钮
                delete_btn = row.locator('button:has-text("删除")')
                if delete_btn.count() > 0:
                    delete_btn.click()
                    self.page.wait_for_timeout(1000)
                    return True
        
        raise Exception(f"未找到包含课程名称 '{course_name}' 的行")
    
    @allure.step("在确认对话框中点击确定按钮")
    def click_confirm_delete(self):
        """在确认对话框中点击确定"""
        # 等待对话框出现
        self.page.wait_for_timeout(1000)
        # 点击确定按钮 - 使用last()以避免点击到其他确定按钮
        confirm_buttons = self.page.locator('button:has-text("确定")').all()
        if confirm_buttons:
            # 点击最后一个可见的确定按钮（通常是对话框中的）
            for btn in reversed(confirm_buttons):
                if btn.is_visible():
                    btn.click()
                    # 等待删除操作完成 - 增加等待时间
                    self.page.wait_for_timeout(3000)
                    return
        
        # 如果没有找到，尝试直接点击
        self.page.wait_for_timeout(2000)
    
    @allure.step("删除指定课程")
    def delete_course_by_name(self, course_name: str):
        """删除指定名称的课程"""
        self.click_delete_button_by_name(course_name)
        self.click_confirm_delete()
        
        # 刷新页面确保列表更新
        self.page.reload()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
    
    @allure.step("验证删除成功 - 检查课程列表中不包含: {course_name}")
    def verify_course_deleted(self, course_name: str):
        """验证课程已成功删除"""
        self.page.wait_for_load_state("networkidle")
        # 等待页面更新
        self.page.wait_for_timeout(2000)
        # 获取课程列表中的所有课程名称
        course_names = self.page.locator("tbody td:nth-child(2)").all_inner_texts()
        # 断言被删除的课程名称不在列表中
        assert course_name not in course_names, f"课程 '{course_name}' 仍然存在于列表中，删除失败"
    
    @allure.step("验证删除成功 - 检查课程数量减少")
    def verify_course_count_decreased(self, before_count: int):
        """验证课程数量减少"""
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        # 获取当前的课程数量
        course_rows = self.page.locator("tbody tr").count()
        # 断言课程数量减少
        assert course_rows < before_count, f"课程数量未减少，删除失败"
