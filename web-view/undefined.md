---
description: スクリーンキャプチャー防止によるコンテンツ保護方法についてご案内します。
icon: camera-slash
---

# コンテンツ保護

## ANDROID
トレジャーアイランドを包含するActivityにFLAG_SECUREを適用することで、簡単にスクリーンキャプチャーを防止できます。

{% tabs %}
{% tab title="KOTLIN" %}
<pre class="language-kotlin" data-line-numbers><code class="lang-kotlin">override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
<strong>    window.addFlags(WindowManager.LayoutParams.FLAG_SECURE)
</strong>    //..
    // code
    //..
}
</code></pre>
{% endtab %}

{% tab title="JAVA" %}
<pre class="language-java" data-line-numbers><code class="lang-java">@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
<strong>    getWindow().addFlags(WindowManager.LayoutParams.FLAG_SECURE);
</strong>    //..
    // code
    //..
}
</code></pre>
{% endtab %}
{% endtabs %}

***

## iOS
ANDROIDプラットフォームとは異なり、システムでの個別サポートがないため、`UITextField`のisSecureTextEntry属性を使用してユーザーがスクリーンキャプチャーを行えないように迂回処理する必要があります。

<pre class="language-swift" data-line-numbers><code class="lang-swift"><strong>private let preventedView = UITextField()
</strong>
func applySecureContent() {
    self.addSubview(self.preventedView)
<strong>    self.preventedView.backgroundColor = .clear
</strong><strong>    self.preventedView.isSecureTextEntry = true
</strong><strong>    self.preventedView.isUserInteractionEnabled = false
</strong>    self.preventedView.translatesAutoresizingMaskIntoConstraints = false
    self.preventedView.centerYAnchor.constraint(equalTo: self.centerYAnchor).isActive = true
    self.preventedView.centerXAnchor.constraint(equalTo: self.centerXAnchor).isActive = true
    self.preventedView.leftView = UIView(frame: CGRect(x: 0, y: 0, width: self.preventedView.frame.self.width, height: self.preventedView.frame.self.height))
    self.preventedView.leftViewMode = .always
<strong>    self.layer.superlayer?.addSublayer(self.preventedView.layer)
</strong><strong>    self.preventedView.layer.sublayers?.last?.addSublayer(self.layer)
</strong>}
//..
//..
<strong>override func viewDidAppear(_ animated: Bool) {
</strong>    DispatchQueue.main.async {
        applySecureContent()
    }
}
</code></pre>
