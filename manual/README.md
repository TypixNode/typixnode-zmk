# TypixNode — 说明书（改版）/ Manual (redesigned)

中文 + English 双语 PDF 使用说明书。键位与功能均从 ZMK 固件源码反推生成。

- **成品 PDF / Output:** `../TypixNode_Manual.pdf`（仓库根目录，覆盖旧版）
- 数据来源 / Source: `app/boards/shields/cyberfly_keyboard/cyberfly_keyboard.keymap`（+ `.overlay` / `.conf`）

## 文件 / Files

| 文件 | 说明 |
|---|---|
| `build_manual.py` | 单一键位数据源 → 渲染基础层 / Fn 层键位图 + 组装 HTML |
| `manual_content.py` | 中 / 英双语正文模板 |
| `style.css` | 打印样式（cyber 主题：靛蓝 / 紫 / 青）|
| `images/` | 封面渲染图、背光实拍图 |

## 重新生成 / Rebuild

```bash
brew install weasyprint     # 仅首次
./build.sh                  # -> ../TypixNode_Manual.pdf
```

## 与旧版的主要变化 / Key changes vs old MANUAL.md

- **蓝牙改为多设备**：固件 `CONFIG_BT_MAX_PAIRED=6`，`Fn + 符号键` 切换 6 台设备；
  `Fn + Enter` 清当前配对，`Fn + C` 重置全部设置。（旧版描述的「单设备绑定」已过时。）
- 全新视觉：封面、CSS 键帽键位图（基础层 + Fn 层）、徽章、指示灯色点。
- 双语（中 / 英）合并为同一 PDF。
