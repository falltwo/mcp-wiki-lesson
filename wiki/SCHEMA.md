# MCP Wiki 編輯規則

## 範圍
固定2025-11-25規格版的入門概念；不宣稱最新版本。不介紹私人帳號、真實憑證或未實測的工具接入。

## 結構與來源
raw/articles保存本次七篇官方文件的原文快照及SHA256，唯讀且不對外發布。concepts是AI讀來源後整理的概念頁；每頁至少兩個相關頁面連結。index列所有概念頁。log記本次討論、ingest、查詢、lint與生成的真實動作。

## Frontmatter
每頁有title、created、updated、type、tags、sources、claims、confidence及contested。每一claim包含id、text、sources。只能引用evidence/ingest.json已驗證的source_id，不得新增不存在的編號。語義是否符合原文需人工或獨立審查，Python只驗結構與來源存在。

## 標籤
intro、architecture、tools、resources、prompts、lifecycle、authorization、security。

## 生成規則
HTML簡報只能從概念頁的claim及已存來源manifest取材；自製例子另外標示為模擬，不冒充真實MCP服務。每張slide列claim_id、Wiki頁和source_id，方便反查。

## 版本與衝突
不同規格版不混用；未來要更新就重新擷取為新批次，不能修改本次raw快照。發現語義衝突先修Wiki，再重建HTML，不只在簡報端掩蓋問題。
