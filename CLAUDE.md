# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation-only Obsidian vault for JLU GIS (吉林大学地理信息科学) student survival guide. It contains markdown files organized by category:
- 00-项目缘起 - Project origin
- 01-学习篇 - Learning (培养方案, 实习, 课程, 毕设)
- 02-发展篇 - Development (保研, 就业, 考研, 考公, 出国)
- 03-生活篇 - Life
- 04-学长学姐们的家常话 - Alumni stories
- 05-如何给我们提建议 - Contribution guide
- 07-杂七杂八 - Miscellaneous (Windows tips)
- assets - Images and documents

## Image Convention

All images in markdown should use `/assets/` absolute paths (e.g., `![描述](/assets/image/xxx.png)`). Local image references should be converted to `/assets/` format before committing.

## Available Skills

This repository has several custom skills configured:
- `word-to-markdown`: Converts Word (.docx) to Markdown - triggered by "Word 转 Markdown", "docx 转 markdown", etc.
- `wechat-mp-publisher`: Publishes markdown to WeChat official account drafts - triggered by "发布到微信公众号", "发送到公众号", etc.
- `maptoposter`: Generates minimalist city map posters - triggered by "生成xx城市极简海报", "制作xx城市地图海报", etc.
- `ryfblogskill`: Fetches and saves 阮一峰 blog posts to Obsidian - triggered by URLs starting with "ryf:"
- `git-push-feature-lsq`: Pushes to remote after feature development - triggered by "推送", "提交推送", "推送到远程"

## Git Workflow

- Single main branch only (no feature branches typically)
- Submit changes via Pull Request or contact maintainer directly
- Email: 2314394028@qq.com
- PR process: Fork → Edit → Pull Request → Wait for review and merge

## No Build Commands

This is a documentation-only repository with no build, lint, or test commands. Claude should treat this as a content editing task rather than software development.
