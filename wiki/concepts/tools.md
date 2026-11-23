---
title: Tools：請外部系統做一件事
created: 2026-11-23
updated: 2026-11-23
type: concept
confidence: high
contested: false
tags: ["tools"]
sources: [2]
claims:
  - id: tool-schema
    text: "Tool用名稱、用途說明及輸入綱要描述可執行的操作。Client可透過tools/list取得清單，再以tools/call傳送工具名稱與參數；Server仍須驗證工具輸入並落實存取控制。"
    sources: [2]
  - id: tool-control
    text: "Tools的設計偏向由模型依情境選用，但協定不強制某種操作介面。應用仍應提供讓人拒絕工具呼叫的能力，不能把模型想呼叫視為使用者已授權。"
    sources: [2]
  - id: tool-result
    text: "Server回傳工具結果後，AI應用可以把結果交給模型繼續整理回答；回傳工具錯誤時，也應辨識錯誤而不是把它當成功結果。"
    sources: [2]
---

# Tools：請外部系統做一件事

Tool用名稱、用途說明及輸入綱要描述可執行的操作。Client可透過tools/list取得清單，再以tools/call傳送工具名稱與參數；Server仍須驗證工具輸入並落實存取控制。[2]

Tools的設計偏向由模型依情境選用，但協定不強制某種操作介面。應用仍應提供讓人拒絕工具呼叫的能力，不能把模型想呼叫視為使用者已授權。[2]

Server回傳工具結果後，AI應用可以把結果交給模型繼續整理回答；回傳工具錯誤時，也應辨識錯誤而不是把它當成功結果。[2]

## 相關頁面

- [[architecture]]
- [[trust-boundaries]]

## Sources

[2] https://modelcontextprotocol.io/specification/2025-11-25/server/tools — Tools
