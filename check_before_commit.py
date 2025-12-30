#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
提交前检查脚本
检查是否有敏感文件会被提交
"""

import os
from pathlib import Path

def check_sensitive_files():
    """检查敏感文件是否存在且未被忽略"""
    sensitive_files = [
        '.env',
        'dimension_config.json',
        'dimension_history.json',
    ]
    
    sensitive_dirs = [
        'archive',
        'raw',
        '.venv',
        'venv',
    ]
    
    print("=" * 60)
    print("🔍 提交前检查")
    print("=" * 60)
    
    issues = []
    
    # 检查敏感文件
    print("\n📄 检查敏感文件...")
    for file in sensitive_files:
        if Path(file).exists():
            issues.append(f"⚠️  发现敏感文件: {file} (应该被 .gitignore 忽略)")
            print(f"   ❌ {file} 存在")
        else:
            print(f"   ✅ {file} 不存在")
    
    # 检查敏感目录
    print("\n📁 检查敏感目录...")
    for dir_name in sensitive_dirs:
        if Path(dir_name).exists():
            issues.append(f"⚠️  发现敏感目录: {dir_name} (应该被 .gitignore 忽略)")
            print(f"   ❌ {dir_name} 存在")
        else:
            print(f"   ✅ {dir_name} 不存在")
    
    # 检查必需文件
    print("\n✅ 检查必需文件...")
    required_files = [
        'README.md',
        'requirements.txt',
        'env.example',
        '.gitignore',
        'search_youtube_mcp_videos.py',
        'write_report.py',
        'extract_dimensions.py',
        'dimension_analysis.py',
        'analyze_dimensions.py',
        'manage_themes.py',
        'daily_reminder.py',
    ]
    
    missing = []
    for file in required_files:
        if Path(file).exists():
            print(f"   ✅ {file}")
        else:
            missing.append(file)
            print(f"   ❌ {file} 缺失")
    
    # 总结
    print("\n" + "=" * 60)
    if issues:
        print("⚠️  警告：发现以下问题：")
        for issue in issues:
            print(f"   {issue}")
        print("\n💡 提示：这些文件/目录应该被 .gitignore 忽略")
        print("   如果它们出现在 git status 中，请检查 .gitignore 配置")
    else:
        print("✅ 未发现敏感文件问题")
    
    if missing:
        print("\n❌ 缺失以下必需文件：")
        for file in missing:
            print(f"   - {file}")
    else:
        print("\n✅ 所有必需文件都存在")
    
    print("=" * 60)
    
    if issues or missing:
        return False
    return True

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    success = check_sensitive_files()
    exit(0 if success else 1)

