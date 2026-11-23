---
title: MCP解決什麼問題
created: 2026-11-23
updated: 2026-11-23
type: concept
confidence: high
contested: false
tags: ["intro"]
sources: [1, 5]
claims:
  - id: definition
    text: "MCP是讓AI應用與外部能力交換訊息的協定。它規範連接及訊息格式，不是大型語言模型本身。"
    sources: [1]
  - id: integration
    text: "Server把特定能力整理成一致介面；Host管理AI整合與多個Client。共用協定有利於整合，但實際可用功能仍取決於雙方支援的能力。"
    sources: [1, 5]
---

# MCP解決什麼問題

MCP是讓AI應用與外部能力交換訊息的協定。它規範連接及訊息格式，不是大型語言模型本身。[1]

Server把特定能力整理成一致介面；Host管理AI整合與多個Client。共用協定有利於整合，但實際可用功能仍取決於雙方支援的能力。[1][5]

## 相關頁面

- [[architecture]]
- [[tools]]

## Sources

[1] https://modelcontextprotocol.io/specification/2025-11-25/architecture — Architecture
[5] https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle — Lifecycle
