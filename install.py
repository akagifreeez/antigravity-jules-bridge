#!/usr/bin/env python3
"""
プロジェクト導入スクリプト
他のプロジェクトにjules-delegationスキルを1コマンドで導入する
"""

import argparse
import shutil
import json
from pathlib import Path


def install_to_project(target_path: str, api_key: str = None):
    """
    対象プロジェクトにjules-delegationを導入
    
    Args:
        target_path: 対象プロジェクトのパス
        api_key: Jules APIキー（オプション）
    """
    source_dir = Path(__file__).parent
    target_dir = Path(target_path)
    
    if not target_dir.exists():
        print(f"エラー: 対象ディレクトリが存在しません: {target_path}")
        return False
    
    # .agent/skills/jules-delegation をコピー
    skills_source = source_dir / ".agent" / "skills" / "jules-delegation"
    skills_target = target_dir / ".agent" / "skills" / "jules-delegation"
    
    if skills_target.exists():
        print(f"警告: {skills_target} は既に存在します。上書きします。")
        shutil.rmtree(skills_target)
    
    skills_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skills_source, skills_target)
    print(f"✓ スキルをコピー: {skills_target}")
    
    # .agent/workflows/delegate.md をコピー
    workflow_source = source_dir / ".agent" / "workflows" / "delegate.md"
    workflow_target = target_dir / ".agent" / "workflows" / "delegate.md"
    
    workflow_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(workflow_source, workflow_target)
    print(f"✓ ワークフローをコピー: {workflow_target}")
    
    # src をコピー
    src_source = source_dir / "src"
    src_target = target_dir / ".agent" / "skills" / "jules-delegation" / "src"
    
    if src_target.exists():
        shutil.rmtree(src_target)
    
    shutil.copytree(src_source, src_target)
    print(f"✓ ソースをコピー: {src_target}")
    
    # config.json を生成
    config_target = target_dir / "config.json"
    
    if not config_target.exists():
        config = {
            "jules_api_key": api_key or "YOUR_API_KEY_HERE",
            "polling_interval_seconds": 30,
            "require_plan_approval": True,
            "history_path": ".jules_history.json"
        }
        
        with open(config_target, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 設定ファイルを生成: {config_target}")
        
        if not api_key:
            print("\n⚠ config.json の jules_api_key を設定してください")
    else:
        print(f"ℹ 設定ファイルは既に存在します: {config_target}")
    
    print("\n✅ インストール完了!")
    print("\n使い方:")
    print("  Antigravityから /delegate コマンドでタスクを委任できます")
    print("  または: python .agent/skills/jules-delegation/scripts/delegate.py \"タスク説明\"")
    print("\n※ ソース（リポジトリ）は自動検出されます")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="jules-delegation スキルを他のプロジェクトに導入",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
例:
  python install.py --target /path/to/project
  python install.py --target /path/to/project --api-key YOUR_KEY
        """
    )
    parser.add_argument(
        "--target", "-t",
        required=True,
        help="導入先プロジェクトのパス"
    )
    parser.add_argument(
        "--api-key", "-k",
        help="Jules APIキー"
    )
    
    args = parser.parse_args()
    
    success = install_to_project(
        target_path=args.target,
        api_key=args.api_key
    )
    
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
