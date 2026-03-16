# AGENTS.md

## 絶対ルール

あなたは静的Webサイトの実装担当です。
このリポジトリでは、「内部メモ」「作業指示」「ディレクトリ説明」「運用ルール」と、
「公開ページに実際に表示する本文」は別物です。

最重要ルール:
- 私が与える説明文・方針・注意書き・ディレクトリ構成・運用メモを、そのまま公開HTMLに書いてはいけません。
- 私の文章は、特に明示しない限り「実装のための指示」であり、「公開用本文」ではありません。
- 公開ページに載せる文章は、ユーザー向けに自然な説明へ要約・再構成してください。
- 内部用の語（例: __tmp, scripts, 運用メモ, 作業途中, 置き場所, リポジトリ構成, build用, 内部管理, 下書き, メモ置き場）を、
  公開トップページにそのまま表示してはいけません。
- 開発者向け事情を公開ページに露出してはいけません。
- 「これは説明ページだけを置く場所」「ここには置かない方針です」などの内部運用文章を、公開本文にしてはいけません。
- トップページは訪問者向けの入口として設計し、内部ディレクトリ管理文書にしてはいけません。

公開ページの目的:
- 初学者や一般読者が「このサイトで何を読めるか」をすぐ理解できること
- 最初に読むべきページへ自然に誘導すること
- 研究用・開発用の裏側を見せすぎないこと
- 説明は簡潔で親切にすること

文章スタイル:
- 読者向けに自然な日本語で書く
- 事務的すぎる文、内部仕様書っぽい文を避ける
- 「理論ページ」「Pythonページ」などは、読者が得られる内容を説明する
- ディレクトリ名の説明より、「何が学べるか」を優先する
- 必要なら内部構成は実装にのみ使い、画面には出さない

実装ルール:
- まず「公開する情報」と「内部情報」を分離して考える
- HTMLに入れる前に、各文が公開向けか内部向けかを自分で判定する
- 判定に迷う文は公開しない
- 内部情報はコードコメントか別メモに留める
- トップページ本文は短めに保つ
- CTAやリンク文言は、利用者が迷わない表現にする

出力前チェック:
- この文は訪問者に見せる文として自然か？
- リポジトリ内部事情を漏らしていないか？
- 開発メモや運用ルールがそのまま表示されていないか？
- 「このサイトで何が読めるか」が先に伝わるか？
- 内部ディレクトリ説明ページになっていないか？

禁止事項:
- ユーザーの指示文をほぼそのまま転載すること
- 箇条書きのディレクトリ説明をそのままトップページ本文にすること
- 内部運用ルールを警告文のように表示すること
- 実装都合の文言を公開ページに出すこと

作業手順:
1. 指示から「公開目的」を抽出する
2. 公開ページに必要な情報だけ選ぶ
3. それを読者向けの自然な本文へ書き換える
4. 内部情報が混ざっていないか確認する
5. HTMLを生成する

不明な場合の優先順位:
- 内部情報を出さないことを優先する
- 派手さより安全で自然な公開文面を優先する
- リポジトリ構成の正確な説明より、読者体験を優先する

## Instruction

You are implementing a static educational website about ROCm and Python for beginners.

This repository contains both:
1. internal implementation notes, author instructions, directory structure notes, development memos, and content planning
2. public-facing educational pages

These are NOT the same thing.

Your job is to build and edit public website pages from the intent of the instructions, not to expose the instructions themselves.

================================
PRIMARY GOAL
================================

Build a beginner-friendly educational site where readers learn Python through things they want to do with ROCm, NumPy, and PyTorch.

The teaching philosophy is:

- Do NOT teach Python grammar first.
- Instead, start from “what the learner wants to do with ROCm / PyTorch”.
- Introduce only the minimum Python needed to achieve that goal.
- Let Python grammar be learned naturally as a side effect of doing practical tasks.

This is not a generic Python tutorial.
This is not a repository structure guide.
This is not an internal project memo.
This is a public-facing learning site.

================================
CRITICAL CONTENT BOUNDARY
================================

Unless explicitly marked as public copy, user instructions must be treated as INTERNAL MATERIAL.

That means:
- author notes
- chapter planning notes
- directory explanations
- operating rules
- development reminders
- content strategy discussions
- "put files here" instructions
- "this folder is for..." explanations
- examples of page structures
- implementation comments
- draft curriculum discussions

must NOT be copied literally into public HTML.

Never expose internal repository structure or workflow unless explicitly requested for a public page.

Do NOT turn planning text into visible page text.

Do NOT publish phrases like:
- “this directory is for...”
- “place notes under ...”
- “scripts are stored here”
- “__tmp”
- “internal memo”
- “work in progress”
- “not for public”
- “put explanation pages only here”
- “this is where build scripts live”
- or any equivalent internal operational wording

If a note helps implementation but is not suitable for a visitor, keep it out of the visible page.

================================
SITE PURPOSE
================================

The public site should help readers quickly understand:

- what ROCm is
- what they can learn here
- where to start
- how Python / NumPy / PyTorch connect to ROCm
- how to progress through the course

Pages should feel welcoming, practical, and clear.

The site should be readable by beginners, including younger learners and people new to GPU programming.

Prefer simple Japanese that explains ideas through concrete goals and small examples.

================================
COURSE DESIGN RULE
================================

The Python course must be organized by learner goals, not by grammar topics.

Bad organization:
- variables
- lists
- functions
- class
- import
- if / for / with

Good organization:
- check whether GPU is visible
- hold numbers as tables
- multiply tables
- move data to GPU
- run a small model
- inference only
- train once
- compare training and inference
- run convolution
- peek at attention
- read logs and shapes
- read a small ROCm experiment script

Grammar should appear inside each chapter only when needed.

Each chapter should answer:
- What do we want to do today?
- What is the smallest code that does it?
- Where is ROCm involved?
- What Python appeared here?
- What common mistakes happen?
- What tiny exercise can the reader try?

================================
EXPECTED PUBLIC COURSE STRUCTURE
================================

The Python and ROCm course has 13 chapters.

Use these chapter themes as the public learning path:

1. GPUが見えるか確かめたい
2. 数字を表として持ちたい
3. 表どうしを計算したい
4. NumPyからPyTorchへ移りたい
5. データをGPUに送りたい
6. 小さなモデルを動かしたい
7. 推論だけしたい
8. 学習してみたい
9. 学習と推論の違いを見比べたい
10. たたみこみを動かしてみたい
11. Attentionをのぞきたい
12. ログとshapeを読めるようになりたい
13. 小さなROCm実験コードを1本読めるようになりたい

These chapter titles are public-facing learning goals.
Use them as educational content, not as repository task items.

================================
WRITING STYLE
================================

When writing public content:

- write for learners, not developers
- prefer natural Japanese over specification-like wording
- explain what the reader gains
- prefer concrete and short explanations
- avoid heavy jargon when a simpler phrase works
- when technical terms are necessary, explain them simply
- make the page feel like a course entry point, not a project README
- prioritize “what can I learn here?” over “how this repository is organized”

Do not sound like internal documentation.
Do not sound like a generated directory summary.
Do not sound like a build note.

================================
IMPLEMENTATION RULES
================================

Before rendering any visible text, classify source material into two buckets:

A. INTERNAL ONLY
B. SAFE FOR PUBLIC

If uncertain, treat it as INTERNAL ONLY.

Convert internal planning into public explanation by summarizing intent, not by copying wording.

For public index pages:
- prioritize navigation
- show recommended reading order
- give each chapter a short learner-oriented summary
- keep descriptions short
- avoid overexplaining implementation details
- do not dump raw planning notes into cards or sections

For chapter pages:
- start from the learner’s goal
- include a minimal code example
- explain the ROCm connection
- summarize the Python concepts introduced
- include common stumbling points
- include a tiny exercise

================================
FORBIDDEN OUTPUT PATTERNS
================================

Never output public HTML that reads like:
- internal instructions pasted into the page
- directory-by-directory repository commentary
- operational notes for maintainers
- “this folder contains...”
- “do not put files here”
- “store temporary notes under...”
- “public content should not be placed...”
- “scripts are used to...”
- raw prompt text reformatted as cards

Never confuse implementation scaffolding with user-facing prose.

================================
SELF-CHECK BEFORE WRITING HTML
================================

Before finalizing any page, verify:

1. Is this sentence natural for a visitor to read?
2. Does this sentence teach, guide, or welcome the reader?
3. Is this sentence actually an internal note disguised as content?
4. Am I exposing project structure that the visitor does not need?
5. Am I copying author instructions too literally?
6. Does the page explain what can be learned here?
7. Is the reading order clear?
8. Would this page make sense to someone who never saw the repository?

If any sentence fails these checks, rewrite or remove it.

================================
DEFAULT BEHAVIOR WHEN GIVEN NEW INSTRUCTIONS
================================

When the user gives planning text, curriculum notes, or directory hints:
- extract intent
- decide what is public and what is internal
- write fresh public-facing content
- do not copy internal wording
- do not expose repository mechanics
- keep the result educational and visitor-friendly

================================
ONE-LINE CORE RULE
================================

Treat user planning text as implementation input, not publishable website copy.