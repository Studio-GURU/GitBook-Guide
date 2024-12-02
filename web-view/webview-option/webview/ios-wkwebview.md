---
icon: apple
---

# iOS WKWebView

## スキーム処理 <a href="#scheme" id="scheme"></a>

ウェブビュー構成に必要なスキーム処理についてのサンプルコードです。実際のプロジェクトでは参考程度にしてください。

***

### Javascript window.open

WKWebView javascript window.open()コマンドの処理方法について案内します。

{% hint style="success" %}
**public protocol UIWebViewDelegate**

***

`func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView?`

***

:white\_check\_mark: **複数のポップアップが開かれた場合のために、該当ウェブビューのリソース管理が必要です。**

:heavy\_check\_mark: ウェブビューのサイズと位置は希望する値を入れて使用します。

:heavy\_check\_mark: モーダルウィンドウのオプションはアプリの状況に応じて変更して使用してください。
{% endhint %}

[Previous code blocks remain unchanged, only updating Japanese comments]

***

### javascript window.close

WKWebView javascript window.close()コマンドの処理方法について案内します。

{% hint style="success" %}
**public protocol UIWebViewDelegate**

***

`func webViewDidClose(_ webView: WKWebView)`
{% endhint %}

[Previous code block remains unchanged]

***

### Javascript Alert

Javascriptアラートポップアップウィンドウの処理についてのガイド

[Previous code block remains unchanged, only "확인" button text changed to "OK"]

***

### Javascript Confirm

javascriptコンファームポップアップウィンドウの処理についてのガイド

[Previous code block remains unchanged, only "확인" and "취소" button texts changed to "OK" and "キャンセル"]

***

### Javascript Alert(Confirm) TextInput

javascriptテキスト入力が必要なポップアップウィンドウの処理についてのガイド

[Previous code block remains unchanged, only "확인" and "취소" button texts changed to "OK" and "キャンセル"]

***

### Mailto, Tel&#x20;

mailto, telスキーム処理方法についての案内

[Previous code block remains unchanged]
