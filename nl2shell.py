#!/usr/bin/env python3
"""nl2shell —— 自然语言 -> shell 命令文本（绝不执行）。

把常见意图映射为 shell 命令字符串，只打印/返回，绝不真正调用系统 shell；
危险命令（rm -rf / mkfs / shutdown 等）会标记 warning。
零第三方依赖。

用法：
    from nl2shell import to_shell
    print(to_shell("列出当前目录文件"))
"""
from __future__ import annotations

import argparse
import sys

DANGEROUS = ["rm -rf", "mkfs", "shutdown", "reboot", "dd if=", ":(){", "> /dev/sda"]

RULES = [
    (["列出", "目录", "文件"], "ls -lah"),
    (["当前路径", "pwd"], "pwd"),
    (["创建目录"], "mkdir -p "),
    (["查看", "进程"], "ps aux"),
    (["磁盘", "空间"], "df -h"),
    (["内存"], "free -h"),
    (["主机名"], "hostname"),
    (["日期"], "date"),
]


def to_shell(query: str) -> dict:
    cmd = None
    for kws, base in RULES:
        if any(k in query for k in kws):
            cmd = base
            break
    if cmd is None:
        return {"command": None, "warning": None, "note": "未匹配到命令模板"}
    dangerous = any(d in cmd for d in DANGEROUS)
    return {
        "command": cmd,
        "warning": "危险命令，禁止执行" if dangerous else None,
        "note": "仅生成命令文本，不会执行",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="自然语言 -> shell（只打印不执行）")
    p.add_argument("query", nargs="?")
    args = p.parse_args(argv)
    q = args.query or sys.stdin.read()
    r = to_shell(q)
    if not r["command"]:
        print(r["note"])
        return 1
    print(f"命令：{r['command']}")
    if r["warning"]:
        print(f"警告：{r['warning']}")
    print("（本工具绝不执行该命令）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
