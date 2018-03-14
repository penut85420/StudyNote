# Chapter 1 - Computer Security Basics

## What is 電腦安全(Computer Security)

+ 答案根據使用者的角度(Perspective)有所不同
+ Garfinkel 和 Spafford 兩位大師表示：「若這部電腦的運作與軟體的行為能按照你的期望進行，則稱之為安全。」  
(A computer is secure if you can depend on it and its software to behave as you expect)

## CIA Traid - 從使用者的角度
+ 機密性(Confidentiality)
	+ 防止被未授權(Unauthorized)的使用者**讀取**(Reading)機密資訊
+ 完整性(Integrity)
	+ 防止被未授權的使用者**修改**(Writing)資訊
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
	+ 現在是指企圖(Attempts)滲透(Penetrate)一個資訊系統安全的人，**無論其意圖為何**
+ 惡意代碼物件 Malicious Code Object
	+ 種類包含：
		+ 病毒(Virus)
			+ 無法獨立生存，**寄生**在其他檔案，並在特定時機攻擊癱瘓電腦
		+ 蠕蟲(Worm)
			+ 會大量**複製**自己
		+ 後門(Backdoor)
			+ **繞過**系統安全性，從比較隱密的地方取得系統存取權
			+ 特洛伊木馬(Trojan Horse)就是一種後門軟體，用以誤導使用者藉以騙取甚至遠端操作
+ 來自內部的惡意 Malicious Insider
	+ 系統安全要從**內部**做起
	+ 組織內部的人試圖超越他們合法擁有的權利(Right)和權限(Permissions)
	+ 安全專家和系統管理員(Administrators)特別危險

## 風險分析 Risk Analysis
+ 因為**資源有限**，所以無法採取所有保護措施
+ 
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

![風險 = 威脅 + 漏洞](https://i.imgur.com/emYkYkD.png)

## 質的風險評估 Qualitative Risk Assessment
+ 專心於分析資產的**無形**特性(Intangible Properties)而非金錢價值
+ 確定風險的優先級來協助分配安全資源
+ 相對容易進行的評估方式(?)

## 量的風險評估 Quantitative Risk Assessment
+ 根據資產價值、暴露風險的發生率以及資產的年度耗損做評估
+ 使用可能損失的金額決定是否值得實施安全措施

## Managing Risks
+ 風險避免 Risk Avoidance
	+ 當獲利遠小於風險，禁不起任何一次虧損，需要採取風險避免
		+ 例如：騎車可能出車禍，可能有生命危險
	+ 完全避開所有可能發生風險的機率
		+ 例如：宅在家裡，完全不出門騎車
		+ 例如：完全不使用網路
+ 風險減緩 Risk Mitigation
	+ 當獲利大於風險，可以接受這些損失
	+ 採取預防措施來降低風險
		+ 例如：騎車騎慢一點
		+ 例如：使用防火牆
+ 風險轉移 Risk Transference
	+ 當風險發生時，把損失轉移到第三者身上
		+ 例如：買保險(Insurance)
+ 接受風險 Risk Acceptance
	+ 當風險造成的傷害非常低的時候
	+ 完全不做任何事情來避免風險
+ 組合多項管理風險的方式是常見的方法

## 安全性權衡的考量 Considering Security Tradeoffs
+ 安全性可以被視為風險與獲益之間的 Tradeoff
+ Tradeoff 要考量的部分包含：
	+ 安全性
	+ 使用者便利(Convenience)
		+ 使用者可能會因為系統安全過於**累贅**(Cumbersome)而降低使用意願(Willingness)
		+ 使用者為了規避安全可能會造成系統更不安全，例如：過於簡單的登入密碼
	+ 企業目標
	+ 費用(Expenses)
		+ 成本不可以大於企業利益

## 方針與教育 Policy and Education
+ 安全工作的基石
	+ 實施適當的方針
	+ 教育使用者這些方針
+ 資訊安全的方針
	+ 彈性(Flexible)，避免頻繁的修改
	+ 全面(Comprehensive)，確定所有情況都有考慮到
	+ 對所有組織內的成員都可用
	+ 可讀性(Readable)與可理解性(Understandable)

## 總結
+ CIA Triad - 資訊安全人員的目的
+ DAD Triad - 試圖逃避(Evade)安全措施的目的
+ 因為網路，安全問題從個人電腦移至保護所有互聯(Interconnected)電腦
+ 威脅包含：駭客、惡意代碼、內部的惡意
+ 風險分析決定成本與獲益的權衡
	+ 資產估價
	+ 識別風險
	+ 風險機率
	+ 選擇措施
+ 資訊安全的關鍵是設定有效率的方針與教育

## 練習題

<span color="white">c</span>
	1. _____ is a goal of information security that deals with keeping sensitive information from falling into the wrong hands.
		a) Integrity
		b) Availability
		c) Confidentiality
		d) Denial of service


