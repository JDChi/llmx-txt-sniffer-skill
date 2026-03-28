# llms-txt-sniffer

探测文档站点 `llms.txt` 索引文件的 AI 工具，帮助快速定位 AI 友好的文档资源。

## 使用

```bash
python3 sniffer.py <URL>
```

## 安装

```bash
clawhub install llms-txt-sniffer
```

## 示例

```bash
python3 sniffer.py https://docs.example.com
# -> {"found_index": "https://docs.example.com/llms.txt", "type": "llms.txt"}
```

> 详细文档：[SKILL.md](./SKILL.md)
