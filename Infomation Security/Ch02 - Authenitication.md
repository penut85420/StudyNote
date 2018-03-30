# Chapter 2 - Authentication 認證

## 存取控制簡介 Basics of Access Control
+ 方法(Method)與物件(Component)的集合(Collection)
	+ 機密性(Confidentiality)
	+ 完整性(Integrity)
+ 存取控制的目標是在許可範圍內，去認證允許(Permitted)主體(Subject)存取物件(Object)的行為
+ 主體不一定是人，只要發出請求(Request)的都是主體

## 存取與控制 Access & Control
+ 包含了**存取**(Access)與**控制**(Control)兩個部分
+ 認證 Authentication
	+ 誰可以過去? (Who goes there?)
	+ 認證人對機器的存取
	+ 認證機器對機器的存取
+ 授權 Authorization
	+ 可不可以做這件事? (Are you allow to do that?)
	+ 有了存取權後可以做什麼?
	+ 對行為施加限制
+ <span style="color:red">**注意**</span>：
	存取控制常被當成授權的代名詞(Synonym)，但完整定義必須包含兩個部分
+ 主體 Subject
	+ 發出要存取資源需求的個體(Entity)
+ 對象 Object
	+ 主體試圖存取的資源
+ 最低存取原則 Least Privilege Philosophy
	+ 給予主體足夠完成所需工作的權限即可

## 控制 Control
+ 允許或禁止對象訪問的機制(Mechanisms)
	+ 也可以說是不合法存取的一種阻礙(Barrier)
+ 控制常見的種類
	+ 管理層面 Administrative
		+ 從**管理策略**來執行(Enforce)安全規則
		+ 例如：雇用策略 Hiring Practice，無不良紀錄才雇用
		+ 雇用後的狀況觀察：使用量監測和稽核(Usage Monitoring & Accounting)
	+ 邏輯與技術 Logic & Technical
		+ 對象存取的限制(Restrictions)
		+ 例如：
			+ 識別 Identification：多對一的比較
			+ 認證 Authentication：一對一的比較
			+ 加密 Encryption
	+ 實體 Physical
		+ 將存取限制施加在硬體上
		+ 例如：圍牆(Fence)、牆壁、上鎖的門

## 存取控制技術 Access Control Techniques
+ 選擇符合組織需求的技術
+ 也要考慮使用者的接受度

## 存取控制設計 Access Control Designs
+ ### Mandantory Access Control
	+ 指定安全標籤(Security Label)給每個主體和物件
	+ 由安全標籤來決定行為是否准許(Granted)
	+ 常見的應用方式為 **Rule-Based 存取控制**
		+ Rule-Base 是 Mandantory 的一種實作方式
		+ 需要知道給主體哪種等級的安全標籤
		+ 是一種強制的存取控制
	+ 常見軍方(Military)資料分級(Classifications)
		+ 未分類 Unclassified
		+ 敏感但未分類 Sensitive but Unclassified
		+ 機密 Confidential
		+ 秘密 Secret
		+ 最高機密 Top Secret
	+ 常見商業資料分級
		+ 公開 Public
		+ 敏感 Sensitive
		+ 私人 Private
		+ 機密 Confidential
+ ### Discretionary Access Control
	+ 依照物件所有者的喜好決定
	+ 商業操作上常見的設計
	+ 基本上比較彈性、易實作
	+ 基本上比 Mandantory 不安全
	+ 包含 Identity-Based 存取控制、Access Control Lists(ACLs)
+ ### Non-Discretionary Access Control
	+ 根據主體的角色與任務決定存取控制權
		+ 也可稱為 Role-Based, Task-Based Access Control
	+ Lattice-Based Control 是一種 Non-Discretionary Access Control 的變體(Variation)
		+ 主體和對象之間具有一組用於定義訪問規則和條件的邊界

## 存取控制的管理 Access Control Administration
+ 主要分為集中式、分散式、混合式
+ ### 集中式 Centralized
	+ 所有的需求都經過一個權力核心
	+ 管理政策相對單純
	+ 因為都經過一個點，所以會有效能瓶頸(Bottlenecks)
+ ### 分散式 Decentralized
	+ 物件的存取控制不是集中的
	+ 相對複雜的管理策略
	+ 效能相對穩定