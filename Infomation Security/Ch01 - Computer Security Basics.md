# Chapter 1 - Computer Security Basics

## What is 電腦安全(Computer Security)

+ 答案根據使用者的角度(Perspective)有所不同
+ Garfinkel 和 Spafford 兩位大師表示：「若這部電腦的運作與軟體的行為能按照你的期望進行，則稱之為安全。」  
(A computer is secure if you can depend on it and its software to behave as you expect)

## CIA Traid - 從使用者的角度
+ 機密性(Confidentiality)
	+ 防止被未授權(Unauthorized)的使用者讀取(Reading)機密資訊
+ 完整性(Integrity)
	+ 防止被未授權的使用者修改(Writing)資訊
+ 可用性(Availability)
	+ 授權的使用者可以正常的存取資料、使用服務

## DAD Traid - 從攻擊者的角度
+ 洩漏(Disclosure)
	+ 未授權的使用者存取到機密性的資訊
	+ 破壞了 CIA 的機密性
+ 竄改(Alteration)
	+ 未授權的使用者竄改了資訊
	+ 破壞了 CIA 的完整性與機密性
+ 阻斷(Denial)
	+ 授權的使用者無法存取資料
	+ 破壞了 CIA 的可用性

## 網路資訊安全 Network Security
+ 原本只需要關注獨立系統的安全
+ 區域網路(LANS - Local Area Network)與網際網路(Internet)的發展使資訊安全的問題變得更困難
+ 注意事項(Considerations)包含：
	+ 保護 TCP/IP 協定(Protocol)
	+ 防火牆(Firewalls)
	+ 入侵檢測系統(Intrusion Detection Systems)

## 網路對安全的威脅 Threat to Security
+ 黑客 Hacker
	+ 黑客原意為熟練的電腦使用人員
	+ 現在是指企圖(Attempts)滲透(Penetrate)一個資訊系統安全的人，無論其意圖為何
+ 惡意代碼物件 Malicious Code Object
	+ 種類包含：
		+ 病毒(Virus)
			+ 無法獨立生存，寄生在其他檔案
		+ 蠕蟲(Worm)
			+ 會大量複製自己
		+ 後門(Backdoor)
			+ 繞過系統安全性，從比較隱密的地方取得系統存取權
			+ 特洛伊木馬(Trojan Horse)就是一種後門軟體，用以誤導使用者藉以騙取甚至遠端操作
+ 來自內部的惡意 Malicious Insider
	+ 系統安全要從內部做起
	+ 組織內部的人試圖超越他們合法擁有的權利(Right)和權限(Permissions)
	+ 安全專家和系統管理員(Administrators)特別危險

## 風險分析 Risk Analysis
+ 因為資源有限，所以無法採取所有保護措施
+ 風險分析所涉及(Involved)的行動：
	+ 決定有價值的資產(Assets)
	+ 識別(Identify)資產可能面臨的風險
	+ 確定每個風險發生的可能性(Likelihood)
	+ 採取保護措施來管理(Manage)風險
+ 資安專家所規定的風險分析過程

## 資產價值 Identifying and Valuing Assets
+ 資產價值是權衡(Tradeoffs)成本與收益(Cost & Benefit)的基礎(Foundation)
+ 資產的價值可以用的評估(Valuation)方法：
	+ **取代價評估法** Replacement Cost Valuation
		+ 使用取代物的價格作為資產的價格
	+ **原始價評估法** Original Cost Valuation
		+ 使用資產當初購入的價格作為資產的價格
	+ **折舊價評估法** Depreciated Valuation
		+ 使用取代物與原價的價差作為資產的價格
	+ **優先度評估法** Qualitative Valuation
		+ 無論該資產的金錢價值(Dollar Values)為何，優先度(Priorities)高的資產就是比較重要

## 識別與評估風險 Identifying and Assessing Risks
+ 兩種主要的風險評估技術：
	+ 值 Qualitative
	+ 量 Quantitative
+ 漏洞 Vulnerability
	+ 系統**內部**可能(Potentially)被利用(Exploited)的弱點(Weakness)
	+ 例如：沒有安裝防毒軟體的電腦
+ 威脅 Threat
	+ 來自**外部**可能利用系統漏洞的情況(Circumstance)
	+ 例如：網路上存在著電腦病毒
+ 風險 Risk
	+ 等於**威脅**加上**漏洞**