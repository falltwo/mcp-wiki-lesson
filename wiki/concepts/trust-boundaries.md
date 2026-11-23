---
title: MCP不會自動保證安全
created: 2026-11-23
updated: 2026-11-23
type: concept
confidence: high
contested: false
tags: ["security"]
sources: [1, 2, 6, 7]
claims:
  - id: least-privilege
    text: "MCP的安全仍依賴實作。限制可用工具、縮小資料範圍與權限，並讓使用者看得懂將執行什麼，能減少不必要的風險。"
    sources: [1, 2, 7]
  - id: token-boundary
    text: "MCP Server應驗證入站Token的有效性與適用對象；呼叫下游API時應另行取得下游所需的Token，不得把收到的Token原樣轉送。這項禁令不會因為入站Token已驗證就消失。"
    sources: [6, 7]
  - id: conversation-boundary
    text: "架構設計要求Server只取得必要情境，而非看遍完整對話；這個邊界仍要由Host與實作落實，不是貼上MCP標籤就自動成立。"
    sources: [1]
---

# MCP不會自動保證安全

MCP的安全仍依賴實作。限制可用工具、縮小資料範圍與權限，並讓使用者看得懂將執行什麼，能減少不必要的風險。[1][2][7]

MCP Server應驗證入站Token的有效性與適用對象；呼叫下游API時應另行取得下游所需的Token，不得把收到的Token原樣轉送。這項禁令不會因為入站Token已驗證就消失。[6][7]

架構設計要求Server只取得必要情境，而非看遍完整對話；這個邊界仍要由Host與實作落實，不是貼上MCP標籤就自動成立。[1]

## 相關頁面

- [[authorization]]
- [[tools]]

## Sources

[1] https://modelcontextprotocol.io/specification/2025-11-25/architecture — Architecture
[2] https://modelcontextprotocol.io/specification/2025-11-25/server/tools — Tools
[6] https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization — Authorization
[7] https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices — Security Best Practices
