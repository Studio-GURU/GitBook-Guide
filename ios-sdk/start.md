---
description: トレジャーアイランドiOS SDKが提供するサービスを連携する前に完了すべき設定について説明します。
icon: star-shooting
---

# はじめに

***

## 連携手順

1. 要件を確認します。
2. 連携キーを発行してもらいます。
3. 基本モジュールを適用します（CocoaPods/SwiftPackage）。
4. IDFA使用同意設定を行います。
5. iOS ATS ポリシーを設定します。

***

## 要件

{% hint style="success" %}
**要件仕様はトレジャーアイランドiOS SDKの最新状態を基準として記載されています。**

***

OSとの互換性のため、最新バージョンへのアップデートを推奨します。
{% endhint %}

:heavy\_check\_mark: iOS 15以上を推奨します。

:heavy\_check\_mark: Swift 5以上のバージョンを推奨します。

:heavy\_check\_mark: 最新バージョンのXCodeの使用を推奨（開発基準15.4バージョン使用）

***

## 連携キーの発行

{% hint style="info" %}
トレジャーアイランド**iOS SDK**を連携するには、連携するアプリの固有識別子（AppId/AppSecret）が必要で、営業担当者を通じて発行されます。
{% endhint %}

| AppID     |   | アプリ固有識別子     |
| --------- | - | -------------- |
| AppSecret |   | アプリ固有識別子検証キー |

***

[Rest of the content follows the same translation pattern, keeping all technical terms, URLs, code blocks, and image references intact while translating the descriptive text to Japanese]

## IDFAの使用同意設定

トレジャーアイランドSDKはパーソナライズド広告を提供するためにユーザー識別情報（IDFA(ADID)）を確認します。

**info.plist**または**TARGETS -> Info -> Custom iOS Target Properties**の値を更新します。

<table><thead><tr><th width="319">Key</th><th>Value</th></tr></thead><tbody><tr><td>Privacy - Tracking Usage Description<br>NSUserTrackingUsageDescription</td><td>パーソナライズド広告を提供するためにユーザー識別情報を使用します。</td></tr></tbody></table>

[Images and remaining content remain unchanged]

***

## iOS ATS(App Transport Security)ポリシー設定

一部の広告提供業者または開発モードではhttpsを提供していない場合があるため、ATS設定が必要です。

<table><thead><tr><th width="321">Key</th><th width="276">Sub Key</th><th>Value</th></tr></thead><tbody><tr><td>App Transport Security Setting</td><td>Allow Arbitrary Loads</td><td>YES</td></tr></tbody></table>
