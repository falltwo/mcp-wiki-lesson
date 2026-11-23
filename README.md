# MCP Wiki → 教學 HTML 簡報

以七篇官方文件整理成七個概念頁，再從十八項可追溯claim產生十四張入門投影片。固定採2025-11-25規格版，不宣稱是最新規格。

- 教學網站：https://falltwo.github.io/mcp-wiki-lesson/
- Wiki頁面：https://falltwo.github.io/mcp-wiki-lesson/#wiki=mcp-overview
- 來源對照：https://falltwo.github.io/mcp-wiki-lesson/#map
- 執行紀錄：https://falltwo.github.io/mcp-wiki-lesson/#run

## 內容

`wiki/concepts/` 是有來源的概念頁；`slides_plan.json` 決定教學順序；`templates/lesson.html` 是版面與互動；`scripts/pipeline.py` 讀Wiki、檢查引用和連結、產生HTML與對照。`AGENTS.md` 與 `wiki/SCHEMA.md` 保存後續新增內容的規則。

工具呼叫與圖書館時間是純前端教學模擬，不會連線MCP服務或真的查詢圖書館。三題問答只用來檢查概念，不上傳作答。

## 重建與測試

Python 3.12。HTML不依賴外部CDN，生成後可直接以瀏覽器開啟。

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/pipeline.py --output docs
.venv/bin/python tests/test_pipeline.py
```

公開來源manifest已包含在 `evidence/ingest.json`，所以重建不需帳號、密鑰或Hermes。首次想重新擷取原文時可執行：

```sh
.venv/bin/python scripts/ingest.py
```

原文快照是本機資料，不在repo重印；腳本會保存來源URL、版本、SHA256與唯讀快照。若raw已存在會停止，不覆寫原批次；要做新來源批次請另存專案。第三方原文版權仍屬原作者。

## 查核範圍

Python驗的是結構與來源編號，不是語義。初稿另做隔離上下文的原文審查，五項具體修訂與修正版的父代理查核範圍記在 `evidence/content-review.json`。九種負測是刻意修改資料副本，不是自然錯誤率。公開站只有本作品，沒有私人筆記、原始對話或憑證。

## English

A beginner MCP lesson built from a seven-document, version-pinned concept wiki. Fourteen slides link back to eighteen claims and their official sources. The page includes a simulated tool-call walkthrough, a three-question quiz, and a slide-to-wiki-to-source map. It does not run a live MCP server or call an LLM API.

Rebuild with Python 3.12 using the commands above. The published manifest is sufficient for rendering; raw third-party documents are deliberately excluded from the repository and can be fetched locally. Structural validation, controlled negative tests, and the scope of the independent draft review are recorded separately.
