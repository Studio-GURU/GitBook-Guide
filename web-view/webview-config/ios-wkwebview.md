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

```swift
// MARK: - Javascript window.open { WKUIDelegate }
func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration, for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {    
    let viewControllerToPresent = UIViewController()
    viewControllerToPresent.view.backgroundColor = UIColor.white
    viewControllerToPresent.modalPresentationStyle = .automatic
    if let sheet = viewControllerToPresent.sheetPresentationController {
        sheet.prefersGrabberVisible = true
    }
    // 웹뷰를 생성하여 리턴하면 현재 웹뷰와 parent 관계가 형성됩니다.
    let modalView = WKWebView(frame: CGRect(x: 0, y: 12, width: self.bounds.width, height: self.bounds.height), configuration: configuration)
    // set delegate
    modalView.uiDelegate = self
    modalView.navigationDelegate = self
    // setup scrollview
    modalView.scrollView.bounces = false
    modalView.scrollView.isPagingEnabled = false
    modalView.scrollView.alwaysBounceVertical = false
    modalView.scrollView.showsVerticalScrollIndicator = false
    modalView.scrollView.showsHorizontalScrollIndicator = false
    modalView.scrollView.contentInsetAdjustmentBehavior = .never
    // addview
    viewControllerToPresent.view.addSubview(modalView)
    viewControllerToPresent.presentationController?.delegate = self
    // present
    self.viewController.present(viewControllerToPresent, animated: true);
    return modalView
}
```

***

### javascript window.close

WKWebView javascript window.close()コマンドの処理方法について案内します。

{% hint style="success" %}
**public protocol UIWebViewDelegate**

***

`func webViewDidClose(_ webView: WKWebView)`
{% endhint %}

```swift
/ MARK: - window.close { UIWebViewDelegate }
func webViewDidClose(_ webView: WKWebView) {
    webView.removeFromSuperView()
    //webView = nil
}
```

***

### Javascript Alert

Javascriptアラートポップアップウィンドウの処理についてのガイド

<pre class="language-swift"><code class="lang-swift"><strong>// MARK: - Javascript Alert Controll { UIWebViewDelegate }
</strong>func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping @MainActor () -> Void) {
    let alertController = UIAlertController(title: nil, message: message, preferredStyle: .actionSheet)
    alertController.addAction(UIAlertAction(title: "확인", style: .default, handler: { (action) in
        completionHandler()
    }))
    DispatchQueue.main.async{
        self.viewController?.present(alertController, animated: true, completion: nil)
    }
}
</code></pre>

***

### Javascript Confirm

javascriptコンファームポップアップウィンドウの処理についてのガイド

// MARK: - Javascript Confirm Controll { UIWebViewDelegate }

```swift
func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping @MainActor (Bool) -> Void) {
    let alertController = UIAlertController(title: nil, message: message, preferredStyle: .actionSheet)
    alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: { (action) in
        completionHandler(true)
    }))
    alertController.addAction(UIAlertAction(title: "キャンセル", style: .default, handler: { (action) in
        completionHandler(false)
    }))
    self.viewController?.present(alertController, animated: true, completion: nil)
}
```

***

### Javascript Alert(Confirm) TextInput

javascriptテキスト入力が必要なポップアップウィンドウの処理についてのガイド

// MARK: - Javascript InputText Controll { UIWebViewDelegate }

```swift
func webView(_ webView: WKWebView, runJavaScriptTextInputPanelWithPrompt prompt: String, defaultText: String?, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping @MainActor (String?) -> Void) {
    let alertController = UIAlertController(title: nil, message: prompt, preferredStyle: .actionSheet)
    alertController.addTextField { (textField) in
        textField.text = defaultText
    }
    alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: { (action) in
        if let text = alertController.textFields?.first?.text {
            completionHandler(text)
        } else {
            completionHandler(defaultText)
        }
    }))
    alertController.addAction(UIAlertAction(title: "キャンセル", style: .default, handler: { (action) in
        completionHandler(nil)
    }))
    self.viewController?.present(alertController, animated: true, completion: nil)
}
```

***

### Mailto, Tel

mailto, telスキーム処理方法についての案内

```swift
// MARK: - mailto:, tel: { UIWebViewDelegate }
func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping @MainActor (WKNavigationActionPolicy) -> Void) {
    // check url
    guard let url = navigationAction.request.url else {
        self.error(stackMessage: "scheme -> url is null")
        decisionHandler(.allow)
        return
    }
    // check scheme
    guard let scheme = url.scheme else {
        self.error(stackMessage: "scheme -> protocol is null")
        decisionHandler(.allow)
        return
    }
    // check mailto, tel
    let schemeOpenUrl = switch scheme {
    case "mailto": url.absoluteString.replacingOccurrences(of: "mailto:", with: "")
    case "tel": url.absoluteString.replacingOccurrences(of: "tel:", with: "")
    default: ""
    }
    // check empty
    if schemeOpenUrl.isEmpty {
        decisionHandler(.allow)
        return
    }
    // create URLComponents
    var components = URLComponents()
    components.scheme = url.scheme
    components.path = schemeOpenUrl
    guard let componentUrl = components.url else {
        decisionHandler(.allow)
        return
    }
    // open application
    if UIApplication.shared.canOpenURL(componentUrl) {
        UIApplication.shared.open(componentUrl)
        decisionHandler(.cancel)
    } else {
        decisionHandler(.allow)
    }
}
```
