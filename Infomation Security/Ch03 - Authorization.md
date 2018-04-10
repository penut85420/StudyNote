# Chapter 3 - Authorization 授權

## Lampson's Access Control Matrix
+ User多、Object多，就很難管理
+ 分割矩陣增加管理效率

## ACLs
+ 只有存 Column 的部分，實作上會變成 Linked List
+ Ex: 紀錄 OS 可以被A rx, B rx, C rwx...
+ 屬於資料導向(Data-Oriented)，容易修改一個資源的權限

## Capabilities
+ 只有存 Row 的部分，Subject 為主
+ Ex: 紀錄 A 可以 rx OS, rx Program, rx Data...
+ 容易新增刪除使用者
+ 容易解決 Confused Deputy 的代表(Delegate)問題

## 混淆的代理者 Confused Deputy
+ Ex: Compiler本身是Object也是Subject
+ 雖然 A 不能 Write B，但 A 可以操作 Compiler Write B
+ 使用 ACLs 比較難避免這個問題
+ 使用 C-List 就比較容易預防這個問題
	+ 這個動作的權限就根據 A 的存取權限來決定

## 分類與許可 Classification & Clearances
+ 分類(Classification) → Objects
	+ 可能有 Secret, Top Secret 等
+ 許可(Clearances) → Subjects
	+ 越高機密的資料，取得許可就越需要詳細的檢查

## MLS - Mutilevel Security
+ 是一種存取控制的形式
+ Model 屬於描述性的(Descriptive)，不是規範性的(Prescriptive)
	+ 他只有叫你分(What to do)，但沒有說怎麼分(How to implement)
	+ 屬於 High-Level 的描述，不是實際的演算法

## 網路分層結構(參考)
1. 應用 Application
2. 傳輸 Transport
3. 網路 Network
4. 連結 Link
5. 實體 Physical

## 防火牆 Firewalls
+ 一種網路(Network)的存取控制
+ 決定什麼可以進來，什麼可以出去
+ 術語 Terminology
	+ 並沒有標準的術語
+ 防火牆的種類
	+ 封包過濾器 Packet Filter
		+ 在網路層(Network Layer)運作
		+ 基於雙方的 IP 和 Port 做過濾
		+ 優點：快
		+ 缺點：沒有狀態、無法追蹤 TCP 連接
	+ 有狀態封包過濾器 Stateful Packet Filter
		+ 在傳輸層(Transport Layer)運作
		+ 可以記得 TCP 連接，也能記得 UDP 的封包
		+ 優點：可以追蹤持續的連接
		+ 缺點：比較慢，無法看見應用程式的內容
		+ 雖然可以做到所有 Packet Filter 能做到的事情
			+ 但是不可以只留 Stateful Packet Filter，會造成效能瓶頸
			+ 相對的，有兩個 Filter 就能分散負擔
	+ 應用代理 Application Proxy
		+ 在應用層(Application Layer)運作
		+ 優點：可以直接看到程式內容，防止病毒
		+ 缺點：速度更慢
	+ 個人防火牆 Personal Firewall
		+ 保護個人使用者的網路
		+ 可能使用以上的任何方法

## 入侵預防 Intrusion Prevention
+ 防止壞人進入
+ 授權、防火牆和防毒軟體都是一種預防

## 入侵偵測 Intrusion Detection
+ 攻擊者已經入侵到你的系統了
+ 透過觀察是否有異常的行為來偵測
	+ 分析 Logs

## 入侵者 Who is likely intruder?
+ 想穿過防火牆的 Outsider
+ 邪惡的 Insider
