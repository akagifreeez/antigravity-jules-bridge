# antigravity-jules-bridge

✅ API Verified

**Antigravity から Jules へのタスク委任ブリッジ**

AIコーディングアシスタント間の作業分担を自動化し、レート制限を回避しながら効率的なコード生成を実現します。

## 機能

- 🔄 **自動委任**: Antigravity のタスクを Jules に自動委任
- 🧠 **スマートデフォルト**: タスク内容からレート制限に最適な実行戦略を自動判断
- 📍 **自動検出**: ブランチ、リポジトリを自動検出
- 📦 **事前同期**: 委任前に自動でコミット・プッシュ
- 🔀 **ブランチ切替**: Jules が作成したブランチへ自動チェックアウト
- 🔌 **ポータブル**: どのプロジェクトにも1コマンドで導入可能

## クイックスタート

### 1. インストール

```bash
pip install -r requirements.txt
```

### 2. 設定

`config.example.json` を `config.json` にコピーし、APIキーを設定:

```json
{
  "jules_api_key": "YOUR_API_KEY_HERE"
}
```

### 3. 使用

```bash
# タスクを委任（スマートデフォルト適用）
python .agent/skills/jules-delegation/scripts/delegate.py "テストを作成"

# ステータス確認
python .agent/skills/jules-delegation/scripts/status.py --check
```

## スマートデフォルト

タスク内容を分析し、最適な実行戦略を自動選択:

| タスク           | 戦略            | 動作                 |
| ---------------- | --------------- | -------------------- |
| 実装系（大きい） | Fire & Forget   | 委任して即戻る       |
| バグ修正・テスト | Wait + Checkout | 完了まで待機         |
| その他           | Fire & Forget   | バックグラウンド実行 |

## 他プロジェクトへの導入

```bash
python install.py --target /path/to/project
```

## API

[Jules API Documentation](https://developers.google.com/jules/api/reference/rest)

## ライセンス

MIT
