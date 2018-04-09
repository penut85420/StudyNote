# Chapter 3 - Authorization 授權

## Lampson's Access Control Matrix
+ User多、Object多，就很難管理
+ 分割矩陣增加管理效率

## ACLs
+ 只有存 Column 的部分，實作上會變成 Linked List

## Capabilities
+ 只有存 Row 的部分，Subject 為主

## 混淆的代理者 Confused Deputy
+ Ex: Compiler本身是Object也是Subject
+ 雖然 A 不能 Write B，但 A 可以操作 Compiler Write B
+ 使用 ACLs 比較難避免這個問題
+ 使用 C-List，則這個動作的權限就根據 A 的存取權限來決定