"""生成Allure报告的脚本"""
import subprocess
import sys
import os

def generate_allure_report():
    # 获取脚本所在目录作为项目目录（相对路径）
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    # 检查 allure-results 目录是否存在
    if not os.path.exists("allure-results"):
        print("❌ allure-results 目录不存在")
        return False
    
    # 检查 allure-results 是否有内容
    result_files = os.listdir("allure-results")
    if not result_files:
        print("❌ allure-results 目录为空")
        return False
    
    print(f"✅ 找到 {len(result_files)} 个测试结果文件")
    
    # 生成报告
    print("\n正在生成Allure报告...")
    try:
        # 尝试使用系统 allure 命令
        result = subprocess.run(
            ["allure", "generate", "allure-results", "-o", "allure-report", "--clean"],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            print("✅ 报告生成成功！")
            
            # 检查报告目录
            if os.path.exists("allure-report/index.html"):
                print("✅ 报告文件已生成：allure-report/index.html")
                # 打开报告
                print("\n正在打开报告...")
                subprocess.Popen(["allure", "open", "allure-report"])
                return True
            else:
                print("⚠️ 报告目录存在但 index.html 未找到")
                return False
        else:
            print(f"❌ 报告生成失败：{result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ 未找到 allure 命令行工具")
        print("\n尝试安装 allure...")
        
        # 尝试使用 pip 安装 allure-pytest
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "allure-pytest"])
            print("✅ allure-pytest 安装成功")
            print("\n注意：需要单独安装 Allure 命令行工具才能生成HTML报告")
            print("请访问：https://docs.qameta.io/allure/#_installing_a_commandline")
            return False
        except Exception as e:
            print(f"❌ 安装失败：{e}")
            return False
    
    except subprocess.TimeoutExpired:
        print("❌ 报告生成超时")
        return False
    except Exception as e:
        print(f"❌ 发生错误：{e}")
        return False

if __name__ == "__main__":
    success = generate_allure_report()
    sys.exit(0 if success else 1)
