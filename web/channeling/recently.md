---
description: 最近閲覧した作品を取得するAPIの使用方法を確認してください。
icon: rectangle-history-circle-user
---

# 最近閲覧した作品の取得

## バージョン

バージョン情報はURLパスには含まれず、ヘッダーの `accept-version` 属性値で定義します。

| Version | Date       | Description |
| ------- | ---------- | ----------- |
| 1.0.0   | 2024.08.23 | 作成        |

## 最近閲覧したコンテンツ

<mark style="color:green;">`GET`</mark> `https://api-{env}.treasurecomics.com/external/recentView?sign={value}`

ユーザーの最近閲覧したコンテンツリストを返します。

### Headers

| Name           | Value              |
| -------------- | ------------------ |
| Content-Type   | `application/json` |
| Authorization  | `Basic token`      |
| Accept-Version | `1.0.0`            |

### **Body**

{% hint style="info" %}
**Signatureの生成方法 (**<mark style="color:red;">**HmacSHA256生成に必要なキーは営業チームから提供されます。**</mark>**)**

***

:heavy\_check\_mark: $timeStamp$nonce$暗号化されたユーザー識別子

上記の値を HmacSHA256 Hash -> Base64 Url Encode に変換してSignatureを生成します。

***

* timeStamp -> UNIXタイムスタンプ（秒単位）
* nonce -> ランダムに生成された32文字の文字列
* user識別子 -> ユーザーを識別可能なID
{% endhint %}

<table data-full-width="false"><thead><tr><th width="127">Name</th><th width="141">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>sign</code></td><td>string</td><td><p><code>timestamp.nonce.encryptedUserId.signature</code></p><p><mark style="background-color:red;">timestamp、nonce、userid の値は<strong>Signature生成に使用した値</strong>を渡します。</mark></p></td></tr></tbody></table>

// 使用例 https://api-{env}.treasurecomics.com/external/recentView?sign=1724328195.3da08653e6c1420aac89eecdf5c20063.OGMzYjUzYTUyYjE1YTJiNDAyZGM3MGJiZmMzMDI2YWE1NDg0YWY2ZTdjNjMyZTJlMTdjMjQyOGU1NjZhYjdhYQ


### **Response**

<table><thead><tr><th width="270">Fields</th><th width="106">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>title</code></td><td>string</td><td>タイトル</td></tr><tr><td><code>description</code></td><td>string</td><td>内容</td></tr><tr><td><code>thumbnail</code></td><td>string</td><td>画像パス</td></tr><tr><td><code>contentType</code></td><td>string</td><td>ウェブトゥーン | ウェブ小説</td></tr><tr><td><code>contentCName</code></td><td>string</td><td>作品キー</td></tr><tr><td><code>episodeNo</code></td><td>number</td><td>エピソード番号</td></tr><tr><td><code>genre</code></td><td>string</td><td>ジャンル</td></tr><tr><td><code>link</code></td><td>string</td><td><p>提供されるリンクの後ろにsignを付けて送信</p><p>例: <code>&#x26;sign=1724328195.3da08653e6c1420aac89eecdf5c20063.OGMzYjUzYTUyYjE1YTJiNDAyZGM3MGJiZmMzMDI2YWE1NDg0YWY2ZTdjNjMyZTJlMTdjMjQyOGU1NjZhYjdhYQ</code></p></td></tr><tr><td><code>returnUrl</code></td><td>string</td><td>最終移動リンク（参考用）</td></tr><tr><td><code>isWaitFree</code></td><td>boolean</td><td>待てば無料かどうか</td></tr><tr><td><code>waitFreeInfo(optional)</code></td><td>object</td><td>待てば無料のチケット情報</td></tr><tr><td></td><td></td><td><p><code>{</code><br>  <code>chargedTicket: boolean,</code><br>  <code>baseDate: Date,</code><br>  <code>chargedDate: Date</code><br><code>}</code></p><p><mark style="background-color:purple;">chargedTicket: 無料チケットの所持状況</mark><br><mark style="background-color:purple;">baseDate: チケット計算基準日</mark><br><mark style="background-color:purple;">chargeDate: チケット充電日</mark></p></td></tr></tbody></table>

**Response Code**

{% tabs %}
{% tab title="200" %}
{% code lineNumbers="true" %}
```json
[  {    "title": "ドラゴンを育てる10の方法",    "description": null,    "thumbnail": "https://s.treasurecomics.com/images/test/webtoon/cw4357a295d0/thumbnail_1718174618.jpg",    "contentType": "ウェブトゥーン",    "contentCName": "cw4357a295d0",    "contentEpisodeTitle": "エピソード1",    "genre": "ドラマ,ホラー/スリラー",    "link": "https://test.treasurecomics.com/gateway/toss?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fcontent%2Flist%2Fcw4357a295d0",    "returnUrl": "https://test.treasurecomics.com/content/list/cw4357a295d0",    "isWaitFree": true,    "waitFreeInfo": {	    chargedTicket: true,	    baseDate: "2024-09-27T03:00:00Z",	    chargedDate: "2024-09-27T03:00:00Z"    }  }]

{% endcode %} {% endtab %}

{% tab title="499" %} {% code lineNumbers="true" %}

{
  "code": "err_already_used_signature",
  "message": "既に使用されたSignatureです。",
  "data": null,
  "appendix": {
    "reason": "既に使用されたSignatureです。",
    "stack": "Error: UNHANDLED\n    at _validateSignature (/var/app/current/build/controllers/external/toss/recentView/get.1.0.0.js:33:15)\n    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)"
  }
}

{% endcode %} {% endtab %} {% endtabs %}

レスポンスエラーコード
<table><thead><tr><th width="307">Code</th><th>Reason</th><th>Message</th></tr></thead><tbody><tr><td><mark style="color:red;"><code>err_invalid_signature</code></mark></td><td>Signature検証失敗</td><td>無効なSignatureです。</td></tr><tr><td><mark style="color:red;"><code>err_already_used_signature</code></mark></td><td>使用済みSignatureの再使用<br>-> 5分間制限</td><td>既に使用されたSignatureです。</td></tr></tbody></table>
最近閲覧した作品の取得例
<div align="left" data-full-width="false"><figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure></div> ```
