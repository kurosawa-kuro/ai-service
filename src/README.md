# AIサービス個人カタログ

増え続ける AI サービス / 技術を、契約数の増減ではなく「比較可能な能力資産」として管理する。

このカタログは、サービス一覧ではなく、黒澤用途での使い分け判断を育てるための台帳。

## 入口

| パス | 役割 |
|---|---|
| `services/` | サービス / 技術ごとの台帳。基本情報、ハーネス適性、黒澤用途、評価ログを持つ |
| `usecases/` | 用途から逆引きするページ。第一候補、補助、ローカル検証、破綻条件を持つ |
| `evaluations/` | 実タスクの評価ログ。印象ではなく再利用判断の根拠を残す |
| `candidates/` | 未検証候補。採用済み・契約対象・推奨ではない |
| `routing-rules.md` | 使い分け判断の正本 |
| `現在の契約.md` | 今実際に払っているコーディング系サービスの契約台帳 |
| `将来方針.md` | 契約の将来の目標形（現契約とは疎結合で管理） |
| `services/coding-plans.md` | コーディング系サービスの料金プラン横比較（選択肢） |
| `education-links.md` | `ai-tool` への教材化ルールと対応表 |

## 運用ルール

- まず `candidates/` に置き、必要なものだけ `services/` へ昇格する。
- `services/` に作っただけでは採用済み扱いにしない。評価ログがついて初めて判断材料になる。
- 用途で迷ったら `usecases/` を見る。
- 使い分けが固まったら `routing-rules.md` に反映する。
- 料金、利用規約、API、CLI、MCP、ローカル可否は変わるため、サービス台帳へ昇格する時点で確認する。
- 教材・比較記事として外に出す内容は `/Users/kurosawa/Dev/ai-tool` へ置く。ここには判断根拠と評価ログを残す。

## 初期優先領域

| 領域 | 理由 |
|---|---|
| CLI / ハーネス | Codex / Claude Code / Cline / Aider など。実作業に直結する |
| 検索 / 調査 | Perplexity / NotebookLM / Tavily / Exa など。出典取得と調査に効く |
| ローカル / 秘匿 | Ollama / LM Studio など。機密、検証、低コスト大量処理の保険 |
| APIルーター | OpenRouter / GroqCloud / Together AI など。将来の自作ルーターに直結 |
| 講座 / 発信 | Gamma / Midjourney / Sora / ElevenLabs など。資料・動画・音声素材に効く |

## 現在の登録状況

| 種別 | 件数 | 入口 |
|---|---:|---|
| サービス台帳 | 18 | `services/README.md` |
| 用途逆引き | 8 | `usecases/README.md` |
| 評価計画 / ログ | 5 | `evaluations/README.md` |
| 候補棚 | 2 | `candidates/README.md` |

## 今すぐ使う順番

1. 用途が決まっているなら `usecases/` を見る。
2. 具体サービスの性質を見るなら `services/README.md` から個別台帳へ行く。
3. 未登録の候補を探すなら `candidates/category-shelves.md` を見る。
4. 実際に使ったら `evaluations/` にログを作る。
5. 判断が固まったら `routing-rules.md` を更新する。

## 次に増やす台帳

| 優先 | 候補 | 理由 |
|---|---|---|
| 1 | LangGraph | 自作AIルーター、状態ありワークフローの中核候補 |
| 2 | LlamaIndex | RAG / ナレッジ接続の中核候補 |
| 3 | Midjourney | 講座・発信用画像生成の基準候補 |
| 4 | Sora | 動画生成の基準候補 |
| 5 | Helicone | LLM APIログ / コスト監視の比較候補 |

## 評価の型

```text
タスク
  -> 入力
  -> 使用サービス / 技術
  -> 結果
  -> 理由
  -> 再利用判断
  -> routing-rules へ反映
```

「Claude は賢い」「DeepSeek は安い」ではなく、
「認証レビューでは Claude が設計矛盾を拾ったので優先」のように残す。
