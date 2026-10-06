import unittest

from nl2shell import to_shell


class TestNl2Shell(unittest.TestCase):
    def test_ls(self):
        r = to_shell("列出当前目录文件")
        self.assertIn("ls", r["command"])

    def test_pwd(self):
        r = to_shell("当前路径是什么")
        self.assertIn("pwd", r["command"])

    def test_unknown(self):
        r = to_shell("量子引力")
        self.assertIsNone(r["command"])

    def test_no_subprocess_execution(self):
        # 断言模块没有调用 subprocess / os.system
        import nl2shell
        import inspect
        src = inspect.getsource(nl2shell)
        self.assertNotIn("subprocess", src)
        self.assertNotIn("os.system", src)
        self.assertNotIn("os.popen", src)

    def test_never_executes(self):
        # 调用 to_shell 不产生任何副作用，仅返回字典
        r = to_shell("查看进程")
        self.assertIsInstance(r, dict)
        self.assertTrue(r["command"])


if __name__ == "__main__":
    unittest.main()
