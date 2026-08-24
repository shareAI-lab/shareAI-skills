# Lab Skills

[English](./README.md) | [简体中文](./README.zh-CN.md) | 日本語

Lab における実際のソフトウェア開発、技術調査、コンテンツ発信、チーム協働から抽出した Skill 集です。

再利用できる作業方法を、参照、議論、調整、継続的な改善のために共有しています。

AI コーディング Agent、および [Agent Skills 仕様](https://agentskills.io/specification)をサポートするシステム向けに設計されています。

## 対象範囲

このリポジトリは Skill のみを収録します。プラグイン、一般チュートリアル、無関係な記事は含みません。

各 Skill は単独で理解し、利用できることを目指しています。一部のパッケージには任意の Agent メタデータがありますが、中心となる指示は特定の製品 Runtime に依存しません。

このコレクションは実践から得られたものであり、普遍的な標準ではありません。各 Skill の description を読み、利用するツール、組織、作業環境に合わない前提は調整してください。

## インストール

利用可能な Skill を確認します：

```bash
npx skills add shareai-lab/lab-skills --list
```

検出された Agent 環境にすべての Skill をインストールします：

```bash
npx skills add shareai-lab/lab-skills --skill '*' -y
```

1 つの Skill をインストールします：

```bash
npx skills add shareai-lab/lab-skills --skill deep-architecture-research
```

インストールせずに、1 つの Skill を使うためのプロンプトを生成します：

```bash
npx skills use shareai-lab/lab-skills@understanding-first-report
```

## 上流の更新を同期する

記録された上流ソースから、現在のスコープにあるすべての Skill を更新します：

```bash
npx skills update
```

1 つの Skill だけを更新します：

```bash
npx skills update deep-architecture-research
```

プロジェクト Skill を確認なしで更新します：

```bash
npx skills update --project -y
```

グローバル Skill を確認なしで更新します：

```bash
npx skills update --global -y
```

改名前の Skill をインストールしている場合は、一度だけ移行してください：

```bash
npx skills remove boss-meet meet-work extract-agent-sessions -y
npx skills add shareai-lab/lab-skills \
  --skill meeting-coach-leader meeting-coach-worker \
          review-ai-conversations -y
```

## Skill カタログ

### 調査と分析

#### [review-ai-conversations](./research-analysis/review-ai-conversations/)

複数の AI Worker との最近の会話を振り返り、核心へ圧縮し、問題空間を整理して、Session をまたぐ新しい洞察を見つけます。

**推奨シナリオ**

- Claude Code、Codex、opencode、Grok Build、Cursor で最近進めていた作業を振り返る。
- 繰り返される質問をクラスタリングし、次元、重なり、依存関係、未解決の空白を整理する。
- 最近の文書、コード成果物、AI の結論を、唯一の真実ではなく参考資料として確認する。
- 新しい洞察、問題の再構成、ブレインストーミングの方向、価値の高い次の問いを生み出す。

**使用例**

```text
/review-ai-conversations 最近の AI Worker との会話を振り返り、
核心的な問題を分類し、問題空間と新しい洞察を整理してください。
```

#### [deep-architecture-research](./research-analysis/deep-architecture-research/)

広いシステム課題を最初に明確化し、ソースコード、履歴、公式ドキュメント、評価済みのコミュニティ情報から深く調査します。

**推奨シナリオ**

- Framework、Runtime、SDK、技術プロジェクトをソースレベルで比較する。
- 重要なアーキテクチャ変更、破壊的変更、難しい境界、議論のあるシナリオを追跡する。
- 新しいシステムの設計や実装方針の選択前に、信頼できる証拠を集める。

**使用例**

```text
/deep-architecture-research これらの Agent Runtime が Session、
Memory、Workspace、Deployment をどう管理するか整理して比較してください。
```

#### [understanding-first-report](./research-analysis/understanding-first-report/)

長時間・複数ターンの技術作業を、明確な問題空間、より深い洞察、専門的な報告へ再整理します。関連する文脈を戻し、何が判明し何が未確認かを示してから、判断しやすい順序で結論を伝えます。

**推奨シナリオ**

- Agent の長時間作業後に、以前の質問、範囲変更、合意済みの判断を再接続する。
- 分析前に関連するユーザーの原文を引用する。以前のターンに依存する場合はそれも引用し、全体が長い場合だけ省略箇所を明示する。
- 分析中は質問を平坦な一覧にせず、空間的な Markdown 図で依存、衝突、owner、問いの背後にある問いを示す。
- 質問群を整理し、より本質的な必要性や矛盾を見つけ、回答の成熟度を確認してから、明確な判断順序で報告する。

**使用例**

```text
/understanding-first-report 関連する複数ターンのユーザー原文を先に引用し、
問題空間と調査状況を整理してから、洞察と次の一歩を提示してください。
```

この 2 つの Skill は組み合わせて使えますが、それぞれ単独でも利用できます。

### ソフトウェアエンジニアリング

#### [vibe-coding](./software-engineering/vibe-coding/)

AI Agent を、判断を透明にし、適切に検証しながら品質を守る開発パートナーへ変えます。

**推奨シナリオ**

- 既存コードの規約を尊重して機能を追加する。
- 実際の失敗経路から Bug を診断して修正する。
- 適切な検証を伴ってリファクタリング、最適化、移行を行う。

**使用例**

```text
/vibe-coding 既存の規約に従ってこの機能をサービスへ追加し、
実際の統合経路を検証してください。
```

### チーム協働とコミュニケーション

#### [meeting-coach-leader](./team-collaboration/meeting-coach-leader/)

リーダーやマネージャーが、実際の仕事と意思決定を前進させる高帯域な会議を準備、運営、振り返ることを支援します。

**推奨シナリオ**

- 従業員の作業レビュー会議を準備または振り返る。
- 繰り返される低価値な議論と、欠けている意思決定の前提を診断する。
- 作業者の責任を引き取らずに、直接的で具体的なフィードバックを行う。

**使用例**

```text
/meeting-coach-leader この会議記録を振り返り、意思決定に到達する
より短いフォローアップ会議を設計してください。
```

#### [meeting-coach-worker](./team-collaboration/meeting-coach-worker/)

作業者が会議、フィードバック、作業メモを、より良い実行と明確な報告へ変換することを支援します。

**推奨シナリオ**

- 最近の会議証拠から、リーダーが本当に期待している結果を理解する。
- 現在の作業が報告可能か、何が不足しているかを確認する。
- 最も価値の高い次の行動を特定し、簡潔な更新を準備する。

**使用例**

```text
/meeting-coach-worker マネージャーが本当に期待していること、
現在不足していること、次回どう報告すべきか整理してください。
```

### Agent 開発

#### [agent-builder](./agent-development/agent-builder/)

AI Agent を設計、構築します。付属のスターターコードは現在 Anthropic Python SDK を使用しますが、アーキテクチャのガイダンスは Provider 非依存を目指しています。

**推奨シナリオ**

- Agent の目的、能力、知識、Context、信頼境界を定義する。
- 計画、Subagent、Skill、追加ツールが本当に必要か判断する。

**使用例**

```text
/agent-builder ポリシー検索、注文確認、返金エスカレーションができる
カスタマーサポート Agent を設計してください。
```

#### [skill-judge](./agent-development/skill-judge/)

実践から得られた診断基準で Agent Skill を評価し、改善します。

**推奨シナリオ**

- `SKILL.md` が適切に起動し、本当に必要な専門知識を提供するか確認する。
- 指示の肥大化、参照の弱さ、自由度の不一致、完了条件の曖昧さを診断する。

**使用例**

```text
/skill-judge この Skill をレビューし、最も影響の大きい
3 つの改善案を提示してください。
```

### コンテンツと発信

#### [media-writer](./content-publishing/media-writer/)

対象コミュニティの文化と表現習慣に合わせて技術コンテンツを書き換えます。

**推奨シナリオ**

- 同じ技術テーマを WeChat、Hacker News、Reddit、Medium、X/Twitter、Dev.to、LinkedIn 向けに書き分ける。
- 画一的なソーシャルメディア形式ではなく、各コミュニティの自然な語り口を保つ。

**使用例**

```text
/media-writer このアーキテクチャノートを、宣伝調の表現を使わずに
Hacker News のローンチ投稿へ書き換えてください。
```

## チーム協働に関する注意

2 つの meeting-coach Skill は、実際の仕事、明確な意思決定、報告準備、高帯域なコミュニケーション、明確な責任を重視します。

会議を通じて仕事を改善するためのものであり、普遍的なマネジメント文化を規定するものではありません。

他の組織へ適用する際は、階層、フィードバック方法、会議頻度、意思決定権、成果物の基準に関する前提を見直してください。

## メンテナンス

Skill は固定されたスナップショットではなく、継続的に更新する作業資産です：

- 実際の使用で欠落、曖昧さ、非効率な動作が見つかったら改善する。
- 現在のツール、Workflow、品質基準と整合させる。
- より単純な境界が有効なら、重複する Skill を統合する。
- 実際の利用が現在の分類と合わなくなったら再分類する。
- 安定して価値を提供できなくなった Skill は置き換えるか廃止する。

## コントリビューション

Skill の追加、改善、移動、統合、廃止を歓迎します。

1. 具体的なユースケース、または観察された失敗から始める。
2. 作者や実装技術ではなく、作業シナリオに合うディレクトリを選ぶ。
3. 有効な `name` と `description` frontmatter を持つ独立した Skill ディレクトリを追加する。
4. Skill に必要な references、scripts、assets、Agent metadata だけを含める。
5. 個別 Skill の構造と、リポジトリ全体のデフォルト検出を検証する。
6. Pull Request で、実践上の根拠、適用範囲、非目標を説明する。

## ライセンス

Apache-2.0
