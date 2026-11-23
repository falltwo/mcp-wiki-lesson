---
title: 先協商，再使用支援的能力
created: 2026-11-23
updated: 2026-11-23
type: concept
confidence: high
contested: false
tags: ["lifecycle"]
sources: [1, 5]
claims:
  - id: handshake
    text: "連接開始時以initialize交換協定版本及能力，再以notifications/initialized表示Client已準備好，之後進入正常操作。"
    sources: [5]
  - id: capabilities
    text: "能力協商讓雙方知道哪些功能可以使用。不能看到一個Server叫做MCP Server，就假設它提供所有工具、資源與提示。"
    sources: [1, 5]
---

# 先協商，再使用支援的能力

連接開始時以initialize交換協定版本及能力，再以notifications/initialized表示Client已準備好，之後進入正常操作。[5]

能力協商讓雙方知道哪些功能可以使用。不能看到一個Server叫做MCP Server，就假設它提供所有工具、資源與提示。[1][5]

## 相關頁面

- [[architecture]]
- [[tools]]

## Sources

[1] https://modelcontextprotocol.io/specification/2025-11-25/architecture — Architecture
[5] https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle — Lifecycle
