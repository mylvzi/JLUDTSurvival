#!/usr/bin/env python3
"""
尝试使用 wechat-article-exporter 的 API 爬取公众号文章
"""

import json
import os
import sys
import requests
from typing import Dict, List, Optional

# 从 .data 文件读取 cookie 信息
def load_cookie_data():
    cookie_file = "/tmp/wechat-exporter-install/wechat-article-exporter/.data/kv/cookie/47be499f7abd48e2ae2dad5f3d546e72"
    if not os.path.exists(cookie_file):
        print(f"Cookie 文件不存在: {cookie_file}")
        return None

    with open(cookie_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

def build_cookie_string(cookie_data: Dict) -> str:
    """构建 Cookie 头部字符串"""
    cookies = []
    for cookie in cookie_data.get('cookies', []):
        if cookie['value'] != 'EXPIRED':
            cookies.append(f"{cookie['name']}={cookie['value']}")

    # 添加其他可能需要的 cookie
    return '; '.join(cookies)

def search_public_account(keyword: str) -> Optional[Dict]:
    """搜索公众号"""
    url = "http://localhost:3000/api/web/mp/searchbiz"
    params = {
        'keyword': keyword,
        'begin': 0,
        'size': 10
    }

    # 尝试不同的认证方式
    headers = {
        'Accept': 'application/json',
        'Referer': 'http://localhost:3000',
    }

    # 尝试使用 auth-key cookie
    cookies = {'auth-key': '47be499f7abd48e2ae2dad5f3d546e72'}

    try:
        response = requests.get(url, params=params, headers=headers, cookies=cookies, timeout=30)
        print(f"搜索公众号响应状态: {response.status_code}")
        print(f"响应内容: {response.text[:200]}")

        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"搜索公众号失败: {e}")

    return None

def get_article_list(biz_id: str, keyword: str = "", begin: int = 0, size: int = 10) -> Optional[Dict]:
    """获取文章列表"""
    url = "http://localhost:3000/api/web/mp/appmsgpublish"
    params = {
        'id': biz_id,
        'keyword': keyword,
        'begin': begin,
        'size': size
    }

    headers = {
        'Accept': 'application/json',
        'Referer': 'http://localhost:3000',
    }

    cookies = {'auth-key': '47be499f7abd48e2ae2dad5f3d546e72'}

    try:
        response = requests.get(url, params=params, headers=headers, cookies=cookies, timeout=30)
        print(f"获取文章列表响应状态: {response.status_code}")
        print(f"响应内容: {response.text[:500]}")

        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"获取文章列表失败: {e}")

    return None

def main():
    print("尝试使用 wechat-article-exporter API 爬取文章...")

    # 1. 加载 cookie 数据
    cookie_data = load_cookie_data()
    if not cookie_data:
        print("无法加载 cookie 数据")
        return

    print(f"Token: {cookie_data.get('token')}")
    print(f"Cookies 数量: {len(cookie_data.get('cookies', []))}")

    # 2. 搜索公众号
    account_name = "吉林大学地球探测科学与技术学院"
    print(f"\n搜索公众号: {account_name}")
    result = search_public_account(account_name)

    if result:
        print(f"搜索结果: {json.dumps(result, ensure_ascii=False, indent=2)[:500]}")

        # 3. 如果找到公众号，获取文章列表
        # 注意：需要从结果中提取 biz/fakeid
        # 暂时跳过，先测试 API 连通性
    else:
        print("搜索公众号失败")

    # 测试直接获取文章列表（需要 biz_id）
    # 这里需要先获取公众号的 biz_id

    print("\nAPI 测试完成")

if __name__ == "__main__":
    main()