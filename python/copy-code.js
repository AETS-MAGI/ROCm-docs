// copy-code.js — コードブロックのコピーボタン
document.addEventListener('click', function (e) {
	var btn = e.target.closest('.copy-btn');
	if (!btn) return;
	var wrap = btn.closest('.code-wrap');
	if (!wrap) return;
	var code = wrap.querySelector('code');
	if (!code) return;

	var text = code.textContent;
	navigator.clipboard.writeText(text).then(function () {
		btn.textContent = 'Copied!';
		btn.classList.add('copied');
		setTimeout(function () {
			btn.textContent = 'Copy';
			btn.classList.remove('copied');
		}, 1500);
	});
});
