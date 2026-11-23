---
title: Resources與Prompts不等於Tools
created: 2026-11-23
updated: 2026-11-23
type: concept
confidence: high
contested: false
tags: ["resources", "prompts"]
sources: [1, 2, 3, 4]
claims:
  - id: resources
    text: "Resources用來提供模型參考的上下文資料，例如檔案或資料庫結構。每個資源以URI識別，由應用決定如何放進上下文。"
    sources: [3]
  - id: prompts
    text: "Prompts是Server提供的結構化訊息模板，可以接受參數；設計上偏向由使用者明確選用，並非模型的私密思考。"
    sources: [4]
  - id: primitive-distinction
    text: "記憶方式：Tool對外執行操作，Resource提供上下文，Prompt提供互動模板。這是三種用途的區分，不表示每個Server都必須同時提供三種功能。"
    sources: [1, 2, 3, 4]
---

# Resources與Prompts不等於Tools

Resources用來提供模型參考的上下文資料，例如檔案或資料庫結構。每個資源以URI識別，由應用決定如何放進上下文。[3]

Prompts是Server提供的結構化訊息模板，可以接受參數；設計上偏向由使用者明確選用，並非模型的私密思考。[4]

記憶方式：Tool對外執行操作，Resource提供上下文，Prompt提供互動模板。這是三種用途的區分，不表示每個Server都必須同時提供三種功能。[1][2][3][4]

## 相關頁面

- [[tools]]
- [[mcp-overview]]

## Sources

[1] https://modelcontextprotocol.io/specification/2025-11-25/architecture — Architecture
[2] https://modelcontextprotocol.io/specification/2025-11-25/server/tools — Tools
[3] https://modelcontextprotocol.io/specification/2025-11-25/server/resources — Resources
[4] https://modelcontextprotocol.io/specification/2025-11-25/server/prompts — Prompts
