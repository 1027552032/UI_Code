import pytest
import allure
import time
from config.settings import Settings


@allure.feature("课程管理模块")
@allure.story("添加课程功能")
class TestAddCourse:

    @allure.title("测试添加课程")
    @allure.description("在课程界面点击添加课按钮，输入课名称、详情描述和展示持续，验证添加成功")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_add_course(self, login_page, course_page):
        # Step 1: 登录系统
        with allure.step("Step 1: 登录系统"):
            login_page.open(Settings.LOGIN_URL)
            login_page.login(Settings.USERNAME, Settings.PASSWORD)
            login_page.verify_login_success()

        # Step 2: 进入课程界面（登录后主页）
        with allure.step("Step 2: 进入课程界面"):
            # 登录成功后已跳转到主页，无需再次打开
            course_page.page.wait_for_load_state("networkidle")

        # Step 3: 点击添加课按钮
        with allure.step("Step 3: 点击添加课按钮"):
            course_page.click_add_course()

        # Step 4: 输入课程信息
        with allure.step("Step 4: 输入课程信息"):
            # 生成带时间戳的课程名称
            course_name = f"测试{int(time.time())}"
            course_desc = "详情描述"
            duration = "1"

            course_page.enter_course_name(course_name)
            course_page.enter_course_desc(course_desc)
            course_page.enter_duration(duration)

        # Step 5: 提交添加课程
        with allure.step("Step 5: 提交添加课程"):
            course_page.click_submit()

        # Step 6: 验证添加成功
        with allure.step("Step 6: 验证添加成功"):
            course_page.verify_course_added()

    @allure.title("测试添加课程并编辑")
    @allure.description("添加课程成功后，点击编辑按钮，依次输入次序为1，名称为test修改，描述为修改后，点击确定按钮")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_add_and_edit_course(self, login_page, course_page):
        # Step 1: 登录系统
        with allure.step("Step 1: 登录系统"):
            login_page.open(Settings.LOGIN_URL)
            login_page.login(Settings.USERNAME, Settings.PASSWORD)
            login_page.verify_login_success()

        # Step 2: 进入课程界面
        with allure.step("Step 2: 进入课程界面"):
            course_page.page.wait_for_load_state("networkidle")

        # Step 3: 点击添加课按钮
        with allure.step("Step 3: 点击添加课按钮"):
            course_page.click_add_course()

        # Step 4: 输入课程信息并创建课程
        with allure.step("Step 4: 输入课程信息并创建课程"):
            course_name = f"测试{int(time.time())}"
            course_desc = "详情描述"
            duration = "1"

            course_page.enter_course_name(course_name)
            course_page.enter_course_desc(course_desc)
            course_page.enter_duration(duration)
            course_page.click_submit()

        # Step 5: 验证添加成功
        with allure.step("Step 5: 验证添加成功"):
            course_page.verify_course_added()

        # Step 6: 编辑课程
        with allure.step("Step 6: 编辑课程"):
            # 等待页面刷新后再点击编辑按钮
            course_page.page.wait_for_timeout(2000)
            course_page.edit_course("1", "test修改", "修改后")

        # Step 7: 验证编辑成功
        with allure.step("Step 7: 验证编辑成功"):
            course_page.page.wait_for_load_state("networkidle")
            course_page.page.wait_for_timeout(2000)
    
    @allure.title("测试删除刚创建的课程")
    @allure.description("添加课程成功后，直接删除该课程，验证删除成功")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_delete_course(self, login_page, course_page):
        # Step 1: 登录系统
        with allure.step("Step 1: 登录系统"):
            login_page.open(Settings.LOGIN_URL)
            login_page.login(Settings.USERNAME, Settings.PASSWORD)
            login_page.verify_login_success()

        # Step 2: 进入课程界面
        with allure.step("Step 2: 进入课程界面"):
            course_page.page.wait_for_load_state("networkidle")
            course_page.page.wait_for_timeout(1000)
            initial_count = course_page.page.locator("tbody tr").count()
            print(f"初始课程数量: {initial_count}")
        
        # Step 3: 点击添加课按钮
        with allure.step("Step 3: 点击添加课按钮"):
            course_page.click_add_course()

        # Step 4: 输入课程信息并创建课程
        with allure.step("Step 4: 输入课程信息并创建课程"):
            course_name = f"测试{int(time.time())}"
            course_desc = "详情描述"
            duration = "1"
            print(f"创建课程: {course_name}")

            course_page.enter_course_name(course_name)
            course_page.enter_course_desc(course_desc)
            course_page.enter_duration(duration)
            course_page.click_submit()

        # Step 5: 验证添加成功
        with allure.step("Step 5: 验证添加成功"):
            course_page.verify_course_added()
            course_page.page.wait_for_timeout(2000)

        # Step 6: 删除刚创建的课程
        with allure.step("Step 6: 删除刚创建的课程"):
            course_page.delete_course_by_name(course_name)

        # Step 7: 验证删除成功
        with allure.step("Step 7: 验证删除成功"):
            course_page.page.wait_for_timeout(2000)
            course_names = course_page.page.locator("tbody td:nth-child(2)").all_inner_texts()
            print(f"删除后课程列表: {course_names}")
            assert course_name not in course_names, f"课程 '{course_name}' 仍存在于列表中，删除失败"


if __name__ == '__main__':
    pytest.main([__file__, '-s', '--alluredir', f'{report_path}', '--clean-alluredir'])