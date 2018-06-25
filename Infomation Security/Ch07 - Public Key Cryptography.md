# Chapter 7 - Public Key Cryptography

## Overview
+ 寄件人使用收件人的公鑰加密訊息。
+ 收件人使用他自己的私鑰解密訊息。
+ 基於 Trap Door, One Way Function
	+ 單向的計算很容易，但從其他方向很難推算回來。
	+ Trap Door 用來創建金鑰。
	+ 舉例：
		+ 給定一個 p 和 q 可以很輕鬆得到 N = p * q。
		+ 但給定一個 N 卻很難找到 p 跟 q 是誰。

## RSA
+ p 跟 q 是兩個很大的質數
+ N = p * q 為 Modulus
+ 選擇一個 e 跟 (p-1)(q-1) 互質
+ e * d = 1 mod (p-1)(q-1)
+ 公鑰是 (N, e)
+ 私鑰是 d
+ 加密訊息 M
	+ C = M^e mod N
+ 解密訊息 C
	+ M = C^d mod N
+ e 跟 N 是公開的
+ 如果攻擊者可以分解 N，他就可以用 e 輕鬆找到 ed = 1 mod (p-1)(q-1)
+ 將 Modulus 分解就可以破解 RSA

## Mod
+ a = b mod n
	+ a - b 是 n 的倍數
+ 38 = 14 mod 12
	+ 38 - 12 - 12 = 14

## Simpla RSA Example
+ 選擇大質數 p = 11, q = 3
+ N = pq = 33, (p-1)(q-1) = 20
+ e = 3 跟 20 互質
+ 找到一個 d 符合 ed = 1 mod 20
+ 我們選擇 d = 7
+ 公鑰：(N, e) = (33, 3)
+ 私鑰：d = 7
+ 假設訊息 M = 8
+ 密文 C = M^e mod N
	+ C = 8^3 mod 33 = 17
+ 解密 M = C^d mod N
	+ M = 17^7 mod 33 = 8

## Diffie-Hellman
+ 一種交換金鑰的演算法。
	+ 用來建立一個對稱式金鑰。
+ 不是用來加密或簽名的。
+ 安全性依賴在離散問題上。
	+ 給定 g, p, g^k mod p, 找到 k
+ 讓 p 是質數，g 是產生器，這兩個數是公開的
+ 在 x 屬於 {1, 2, ..., p-1} 存在一個 n 使得 x = g^n mod p
+ Alice 選擇 Secret Value a
+ Bob 選擇 Secret Value b
+ Alice 送出 g^a mod p 給 Bob
+ Bob 送出 g^b mod p 給 Alice
+ 兩人皆計算分享的 g^ab mod p
+ g^ab mod p 可以做為對稱式金鑰來用
+ 假設 Trudy 可以看見 g^a mod p 和 g^b mod p
+ 註記：g^a * g^b mod p = g^(a+b) mod p ≠ g^ab mod p
+ 如果 Trudy 知道 a 或 b，則系統被破解
+ 如果 Trudy 可以解開離散問題，則他可以找到 a 或 b
+ MiM, Man-In-The-Middle Attack
	+ (Alice, a) > g^a mod p > (Trudy, t) > g^t mod p > (Bob, b)
	+ (Alice, a) < g^t mod p < (Trudy, t) < g^b mod p < (Bob, b)
	+ Trudy 分享 g^at mod p 給 Alice
	+ Trudy 分享 g^bt mod p 給 Bob
	+ 這個過程中，Alice 跟 Bob 都不知道 Trudy 的存在
	+ 如何預防？
		+ 使用對稱金鑰加密 DH Exchange
		+ 使用公開金鑰加密 DH Exchange
		+ 使用私鑰簽名 DH Value

## ECC, Elliptic Curve Crypto
+ EC 不是一個密碼系統，是一種公鑰的數學方式。
+ 可能會更有效率
	+ 一樣的安全性，需要比較少的 Bits
	+ 但是操作更加複雜
+ 圖形 E 代表方程式 y^2 = x^3 + ax + b
+ 同時也包含在無限大的點
+ ![Elliptic Curve](https://i.imgur.com/YiAg5ms.png)
+ 如果 P1 跟 P2 都在 E 上，則定義 P3 = P1 + P2

## ECC Diffie-Hellman

## 公鑰系統的使用
+ 資料的傳輸必須經過不安全的頻道。
+ 保護資料與不安全的媒體。
+ 數位簽章提供完整性與不可否認性。

## Non-Non-Repudiation
+ Alice 從 Bob 那裡點了 100 張股票
+ Alice 使用對稱金鑰計算 MAC
+ 股票下跌，Alice 卻宣稱她沒有買股票
+ Bob 有辦法證明 Alice 下過訂單嗎?
+ 沒辦法，即便 Bob 知道金鑰，他也有可能忘記訊息
+ 所以 Bob 知道 Alice 有下過訂單，可是他無法證明

## Non-Repudiation
+ Alice 一樣買了 100 張股票
+ Alice 在訂單上使用私鑰簽名
+ 股價下跌，Alice 又宣稱他沒有下訂單
+ 這次 Bob 可以證明 Alice 有下單
+ 因為只有擁有 Alice 私鑰的人可以下單
+ 但這是建立在 Alice 的私鑰沒有被竊取的情況下

## 簽名再加密 VS 加密再簽名
+ 標記
	+ 以 Alice 的私鑰 Sign 訊息 M 
		+ [M]<sub>Alice</sub>
	+ 以 Alice 的公鑰 Encrypt 訊息 M
		+ {M}<sub>Alice</sub>
	+ {[M]<sub>Alice</sub>} = M
	+ [{M}<sub>Alice</sub>] = M
+ 

## 公鑰的基礎 Public Key Infrastructure
+ ### 公鑰憑證 Public Key Certificate
	+ 包含使用者的名稱與使用者的金鑰
	+ 憑證由發行人簽章
	+ 使用簽章者的公鑰驗證憑證上的簽章
+ ### 憑證頒發機構 Certificate Authority
	+ CA 是第三方信任機構 (TTP, Trusted Third Party)
	+ 專門發行與簽章憑證的
	+ 驗證簽章 Verifying Signature 
		+ 用來驗證私鑰所有者的身份
		+ 不會用來驗證憑證的來源
	+ 憑證是公開的
	+ 如果 CA 出錯將會造成很大的問題
	+ 常見的憑證格式是 X.509
+ ### PKI, Public Key Infrastructure
	+

## PKI Trust Model

## 真實世界的機密性
+ 對稱金鑰 VS 公開金鑰
+ 
