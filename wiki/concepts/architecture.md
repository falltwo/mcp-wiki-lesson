---
title: Host、Client與Server
created: 2026-11-23
updated: 2026-11-23
type: concept
confidence: high
contested: false
tags: ["architecture"]
sources: [1]
claims:
  - id: host
    text: "Host是使用者操作的AI應用，負責管理Client、整合模型，以及落實權限與使用者同意政策。"
    sources: [1]
  - id: client
    text: "Client是Host內的協定連接元件；每個Client與一個Server維持一對一連線。Host可建立多個Client來連接不同Server。"
    sources: [1]
  - id: server
    text: "Server提供特定的工具、資源或提示模板，可以是本機程序，也可以是遠端服務；Server不等於一定架在雲端。"
    sources: [1]
---

# Host、Client與Server

Host是使用者操作的AI應用，負責管理Client、整合模型，以及落實權限與使用者同意政策。[1]

Client是Host內的協定連接元件；每個Client與一個Server維持一對一連線。Host可建立多個Client來連接不同Server。[1]

Server提供特定的工具、資源或提示模板，可以是本機程序，也可以是遠端服務；Server不等於一定架在雲端。[1]

## 相關頁面

- [[mcp-overview]]
- [[lifecycle]]

## Sources

[1] https://modelcontextprotocol.io/specification/2025-11-25/architecture — Architecture
