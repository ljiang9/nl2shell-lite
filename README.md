# nl2shell-lite

自然语言 → shell 命令文本。**只生成命令字符串，绝不执行**；危险命令给出警告。
零第三方依赖。

## 功能简介

- 常见意图映射为 `ls -lah` / `pwd` / `df -h` 等命令；
- 返回 `{command, warning, note}`；
- 代码不含 `subprocess`/`os.system`，物理上不执行。

## 快速开始

```bash
python3 nl2shell.py "列出当前目录文件"
```

## 无 API key 如何运行

纯模板，**不需要任何 API key**。

## 目录结构

```
nl2shell-lite/
├── nl2shell.py
├── tests/test_nl2shell.py
├── README.md / LICENSE / .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 许可证

[MIT](./LICENSE) © 2026 ljiang9
