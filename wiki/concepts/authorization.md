---
title: 連得上不等於有權限
created: 2026-11-23
updated: 2026-11-23
type: concept
confidence: high
contested: false
tags: ["authorization"]
sources: [6, 7]
claims:
  - id: auth-scope
    text: "此版本的MCP授權規範定義HTTP傳輸的授權流程；授權支援屬選用，支援時仍須遵循相關要求，不能說所有MCP連線都強制使用OAuth。HTTP也可以在本機執行，不能把HTTP和遠端服務畫上等號。"
    sources: [6, 7]
  - id: stdio-scope
    text: "STDIO透過程序的標準輸入與輸出交換訊息。這類本機程序不應照搬HTTP授權流程，而從環境取得憑證；如何隔離程序、給多少權限，仍是實作要處理的問題。"
    sources: [6, 7]
---

# 連得上不等於有權限

此版本的MCP授權規範定義HTTP傳輸的授權流程；授權支援屬選用，支援時仍須遵循相關要求，不能說所有MCP連線都強制使用OAuth。HTTP也可以在本機執行，不能把HTTP和遠端服務畫上等號。[6][7]

STDIO透過程序的標準輸入與輸出交換訊息。這類本機程序不應照搬HTTP授權流程，而從環境取得憑證；如何隔離程序、給多少權限，仍是實作要處理的問題。[6][7]

## 相關頁面

- [[trust-boundaries]]
- [[architecture]]

## Sources

[6] https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization — Authorization
[7] https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices — Security Best Practices
