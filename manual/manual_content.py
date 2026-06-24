# -*- coding: utf-8 -*-
"""Bilingual HTML body for the TypixNode (CyberFly) manual.
Placeholders {base_cn} {fn_cn} {base_en} {fn_en} filled by build_manual.py.
Keep free of stray { } braces (str.format is used)."""

PART_HEAD = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>TypixNode 蓝牙键盘使用说明书 / Manual</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<section class="cover">
  <div class="kicker">CyberFly · nRF52840 · ZMK</div>
  <h1>TypixNode</h1>
  <div class="sub">BLE + USB 双模便携键盘 · 使用说明书</div>
  <div class="sub2">BLE + USB Dual-mode Portable Keyboard · User Manual&nbsp;&nbsp;|&nbsp;&nbsp;中文 / English</div>
  <img class="hero" src="images/keymap_render.png" alt="TypixNode">
  <div class="specstrip">
    <div><div class="k">MCU</div><div class="v">nRF52840</div></div>
    <div><div class="k">无线 / LINK</div><div class="v">BLE + USB</div></div>
    <div><div class="k">蓝牙 / BT</div><div class="v">6 设备</div></div>
    <div><div class="k">飞鼠 / AIR</div><div class="v">6 轴 IMU</div></div>
    <div><div class="k">固件 / FW</div><div class="v">ZMK</div></div>
  </div>
</section>
"""

PART_CN = r"""
<div class="langbar"><span class="tag">CN</span> 中文使用说明</div>

<p class="lead">TypixNode 是一款卡片大小的 <b>BLE + USB 双模</b> 便携键盘，基于 <b>nRF52840</b>（Nice!Nano v2 引脚兼容）+ <b>ZMK</b> 固件。
支持 <b>最多 6 台蓝牙设备</b> 切换，板载 <b>QMI8658A 6 轴 IMU</b> 可作空间飞鼠，带 RGB 状态灯与白色背光。
BLE 下 macOS / iOS 原生显示电量。约 <b>69 键</b>，含一个 <b>Fn 功能层</b>。</p>

<h2><span class="num">1</span> 产品概览</h2>
<div class="cols">
  <div>
    <table class="kv">
      <tr><td>产品名称</td><td>TypixNode（CyberFly 硬件）</td></tr>
      <tr><td>类型</td><td>BLE + USB 双模便携键盘</td></tr>
      <tr><td>主控</td><td>nRF52840（Nice!Nano v2 兼容）</td></tr>
      <tr><td>固件</td><td>ZMK（定制分支）</td></tr>
      <tr><td>蓝牙</td><td>BLE 5.0，最多 <b>6 台设备</b> 配对切换</td></tr>
      <tr><td>飞鼠</td><td>QMI8658A 6 轴 IMU（加速度计 + 陀螺仪）</td></tr>
      <tr><td>背光</td><td>白色，仅 USB 通电可用</td></tr>
      <tr><td>电池</td><td>锂聚合物 LP301060（约 250&nbsp;mAh）</td></tr>
    </table>
  </div>
  <div>
    <figure>
      <img src="images/hero_lit.jpg" alt="TypixNode 背光实拍">
      <figcaption>透明亚克力 + 白色背光实拍；底部红 / 白 LED 为充电 / USB 指示</figcaption>
    </figure>
  </div>
</div>

<h2><span class="num">2</span> 指示灯一览</h2>
<table>
  <tr><th>位置</th><th>灯</th><th>含义</th></tr>
  <tr><td>键盘板<b>上方</b></td><td><span class="dot rgb"></span><b>RGB 灯</b></td><td>工作状态（开机动画、USB 循环、BLE 心跳、飞鼠切换）</td></tr>
  <tr><td>RGB 旁</td><td><span class="dot r"></span><b>红灯</b></td><td>充电中常亮，充满自动熄灭</td></tr>
  <tr><td>键盘板<b>下方</b></td><td><span class="dot w"></span><b>白灯</b></td><td>USB 5V 供电指示，插线就亮</td></tr>
</table>
<h3>RGB 状态详解</h3>
<table>
  <tr><th>场景</th><th>效果</th></tr>
  <tr><td>开机</td><td>红 → 绿 → 蓝 顺序闪一次后熄灭（启动动画）</td></tr>
  <tr><td>USB 已连接</td><td>持续循环变换（三色轮换）</td></tr>
  <tr><td>BLE 待机</td><td><span class="dot b"></span><b>蓝色双闪</b>，每 5 秒一次心跳，代表随时可用</td></tr>
  <tr><td>飞鼠切换</td><td>OFF=<span class="dot r"></span>红闪 / M1=<span class="dot g"></span>绿闪 / M2=<span class="dot b"></span>蓝闪（双闪后回归原状态）</td></tr>
</table>

<h2><span class="num">3</span> 工作模式</h2>
<table>
  <tr><th>模式</th><th>连接</th><th>背光</th><th>飞鼠</th></tr>
  <tr><td><span class="badge usb">USB</span></td><td>USB-C 线</td><td>可用（Fn+空格调节）</td><td>可用</td></tr>
  <tr><td><span class="badge ble">BLE</span></td><td>蓝牙</td><td>自动关闭（省电）</td><td>需手动开启</td></tr>
</table>
<div class="tip"><b>背光仅 USB 通电时可用</b>，拔线自动熄灭（<code>AUTO_OFF_USB</code>）；空闲也会自动熄灭（<code>AUTO_OFF_IDLE</code>）。</div>

<h2><span class="num">4</span> 键位图 · 基础层 (Base)</h2>
<p>下图为按 PCB 丝印呈现的<b>物理键位</b>（标准 QWERTY）。左上角小字为 <b>Shift</b> 上档符号；标记 <b>··</b> 的键支持<b>双击</b>（见第 7 节）。</p>
{base_cn}
<div class="legend-row">
  <span>■ ▲ ✕ ● ♣ ◆ &nbsp;=&nbsp; 顶部 6 个彩色符号键 = <b>F1–F6</b></span>
  <span>·· = 双击有隐藏功能</span>
  <span>左上小字 = Shift 上档</span>
</div>

<h2><span class="num">5</span> 键位图 · Fn 层</h2>
<p>按住左侧 <b>Fn</b> 键（CapsLock 位）时，高亮键生效，灰色为透传。
<span class="badge ble">蓝色</span> = 蓝牙/输出相关，<span class="badge" style="background:#8b5cf6">紫色</span> = 其它功能。</p>
{fn_cn}
<table>
  <tr><th>按住 Fn +</th><th>功能</th></tr>
  <tr><td>Esc</td><td>切换 <b>USB / 蓝牙</b> 输出（<code>OUT_TOG</code>）</td></tr>
  <tr><td>■ ▲ ✕ ● ♣ ◆</td><td>切换到<b>蓝牙设备 1–6</b>（<code>BT_SEL 0–5</code>）</td></tr>
  <tr><td>Enter</td><td>清除<b>当前蓝牙设备</b>的配对（<code>BT_CLR</code>），用于重新配对该槽位</td></tr>
  <tr><td><code>1</code>~<code>0</code> / <code>-</code> / <code>=</code></td><td>F1 ~ F10 / F11 / F12</td></tr>
  <tr><td>⌫ Backspace</td><td>Delete</td></tr>
  <tr><td>↑ / ↓ / ← / →</td><td>PgUp / PgDn / Home / End</td></tr>
  <tr><td>空格 Space</td><td>循环切换背光亮度（<code>BL_CYCLE</code>）</td></tr>
  <tr><td>左 Alt / 右 Alt</td><td>开 / 关 <b>6 轴飞鼠</b>（OFF → M1 → M2 循环）</td></tr>
  <tr><td>右 Shift（按住）</td><td>软关机（<code>soft_off</code>）</td></tr>
  <tr><td>] </td><td>外接电源开关（<code>EP_TOG</code>）</td></tr>
  <tr><td>Q / A / M</td><td>截图宏 / 全选复制宏 / <code>() =&gt; {{}}</code> 宏</td></tr>
  <tr><td>C</td><td>重置全部设置（清 NVS）并重启 ⭐</td></tr>
  <tr><td>B</td><td>进入 Bootloader（UF2 刷机）</td></tr>
</table>

<h2><span class="num">6</span> 蓝牙多设备连接</h2>
<p>固件支持 <b>最多 6 台蓝牙设备</b>（<code>CONFIG_BT_MAX_PAIRED=6</code>），通过 Fn + 顶部符号键在 6 个槽位间切换。</p>
<table>
  <tr><th>操作</th><th>按键</th></tr>
  <tr><td>选择 / 切换到设备 1–6</td><td><b>Fn + ■ / ▲ / ✕ / ● / ♣ / ◆</b></td></tr>
  <tr><td>清除当前设备配对（重新配对该槽位）</td><td><b>Fn + Enter</b></td></tr>
  <tr><td>切换 USB / 蓝牙 输出</td><td><b>Fn + Esc</b></td></tr>
  <tr><td>重置全部设置（清空所有配对 + 重启）</td><td><b>Fn + C</b> ⭐</td></tr>
</table>
<h3>配对流程</h3>
<ol>
  <li><b>Fn + 符号键</b> 选一个空槽位（如设备 1 = Fn + ■）。</li>
  <li>键盘进入广播，在主机蓝牙设置里搜索 <code>TypixNode KBD</code> 并配对。</li>
  <li>连接后，系统「我的设备」即显示电量。</li>
  <li>换主机：<b>Fn + 另一个符号键</b> 切到别的槽位再配对即可——<b>各设备互不覆盖</b>。</li>
</ol>
<div class="key-cta"><b>两种清除的区别：</b><br>
• <b>Fn + Enter</b> = 只清<b>当前</b>这台的配对（其它设备保留）。<br>
• <b>Fn + C</b> = <b>核弹级</b>，清空<b>全部</b>配对、设备名缓存等所有设置并重启，配对全乱时用它。</div>
<h3>电量显示</h3>
<ul>
  <li><b>macOS</b>：系统设置 → 蓝牙 → 「我的设备」卡片。</li>
  <li><b>iOS / iPadOS</b>：桌面加「电池」小组件。</li>
  <li>协议：标准 <b>BLE Battery Service (0x180F)</b>。</li>
</ul>
"""

PART_CN2 = r"""
<h2><span class="num">7</span> 隐藏技巧：双击 / Combo / 宏</h2>
<h3>双击（Tap-dance）</h3>
<table>
  <tr><th>键</th><th>单击</th><th>双击</th></tr>
  <tr><td><b>Esc</b></td><td>Esc</td><td>Caps Word（一次性大写，遇空格退出）</td></tr>
  <tr><td><b>左 Shift</b></td><td>Shift</td><td>锁定 Caps Lock</td></tr>
</table>
<h3>Combo 组合键（同时按）</h3>
<table>
  <tr><th>同按</th><th>触发</th><th>判定窗口</th></tr>
  <tr><td><b>J + K</b></td><td>Esc</td><td>50 ms</td></tr>
  <tr><td><b>D + F</b></td><td>Tab</td><td>50 ms</td></tr>
  <tr><td><b>F + J</b></td><td>Enter</td><td>50 ms</td></tr>
  <tr><td><b>J + K + L</b></td><td>Caps Word</td><td>50 ms</td></tr>
  <tr><td><b>Fn + 右 Shift</b></td><td>开 / 关飞鼠</td><td>75 ms</td></tr>
</table>
<h3>宏（Fn 层）</h3>
<table>
  <tr><th>键</th><th>宏效果</th></tr>
  <tr><td>Fn + Q</td><td>截屏（⌘ + Shift + 4）</td></tr>
  <tr><td>Fn + A</td><td>全选 + 复制（Ctrl+A → 50ms → Ctrl+C）</td></tr>
  <tr><td>Fn + M</td><td>输入 <code>() =&gt; {{}}</code> 箭头函数</td></tr>
</table>
<div class="warn"><b>关于 Fn + 右 Shift：</b>75ms 内<b>同时</b>按下触发飞鼠切换；<b>分前后</b>按则走 Fn 层的<b>软关机</b>。想关机就慢点按，想切飞鼠就同时按下。</div>

<h2><span class="num">8</span> 6 轴飞鼠（Air Mouse）</h2>
<p>板载 <b>QMI8658A</b> 6 轴 IMU（加速度计 + 陀螺仪，I²C）。三档循环切换：</p>
<table>
  <tr><th>模式</th><th>算法</th><th>状态灯</th><th>风格</th></tr>
  <tr><td><b>OFF</b></td><td>关闭，IMU 进省电</td><td><span class="dot r"></span>红闪</td><td>纯键盘</td></tr>
  <tr><td><b>M1</b></td><td>Kalman 滤波 + 状态空间融合</td><td><span class="dot g"></span>绿闪</td><td>稳</td></tr>
  <tr><td><b>M2</b></td><td>加速度倾角映射（简易回退）</td><td><span class="dot b"></span>蓝闪</td><td>跟手</td></tr>
</table>
<p><b>三种切换方式：</b>Fn + 右 Shift（75ms 同按）、Fn + 左 Alt、Fn + 右 Alt。切换时 RGB 对应颜色双闪确认。</p>
<h3>Smart Space：飞鼠开启后空格键变鼠标</h3>
<table>
  <tr><th>位置</th><th>OFF</th><th>ON（M1/M2）</th></tr>
  <tr><td>左空格</td><td>空格</td><td><b>鼠标左键</b></td></tr>
  <tr><td>中空格</td><td>空格</td><td>空格（保持）</td></tr>
  <tr><td>右空格</td><td>空格</td><td><b>鼠标右键</b></td></tr>
</table>
<div class="note"><b>提示：</b>飞鼠仍在调优（漂移滤波、加速度曲线），稳定版前仅作体验。</div>

<h2><span class="num">9</span> 背光</h2>
<ul>
  <li>白色背光，PWM 经 <b>AP3032 升压驱动</b>（P0.15），开机默认<b>关闭</b>，步进 20%。</li>
  <li><b>Fn + 空格</b> 循环切换亮度。</li>
  <li>仅 <b>USB 通电</b> 时可用；拔线或空闲自动熄灭（省电）。</li>
</ul>

<h2><span class="num">10</span> 电源 / 充电 / 开关</h2>
<ul>
  <li>充电口：<b>USB-C</b>，板载充电管理；<span class="dot r"></span>红灯充电中常亮，满电自动灭。</li>
  <li><span class="dot w"></span>白灯：USB 5V 供电指示，插线就亮。</li>
  <li>硬件电源拨动开关：<b>ON</b> = 电池供电、BLE 正常；<b>OFF</b> = 物理断电池，零功耗长期存放。</li>
  <li><b>Fn + 右 Shift</b>（按住）软关机；<b>Fn + ]</b> 切换外接电源（<code>EP_TOG</code>）。</li>
  <li>配对信息存 flash NVS，<b>断电不丢</b>。BLE 待机 &gt; 48 小时。</li>
</ul>

<h2><span class="num">11</span> Bootloader / 固件升级</h2>
<h3>进入 Bootloader 的两种方式</h3>
<ol>
  <li><b>Fn + B</b>（正常工作时）。</li>
  <li><b>板载 reset 按钮双击</b>（固件挂了或 Fn+B 失效时）。</li>
</ol>
<p>进入后：板子主 LED 慢速呼吸，出现名为 <code>NICENANO</code> 的 FAT 虚拟 U 盘，把 <code>.uf2</code> 拖进去即自动重启刷新。</p>
<h3>本地编译固件</h3>
<pre><code>cd cyberfly_zmk
rm -rf build &amp;&amp; .venv/bin/west build -s app -p \
  -b nice_nano/nrf52840/zmk -- -DSHIELD=cyberfly
# 产物: build/zephyr/zmk.uf2</code></pre>
<h3>固件栈</h3>
<ul>
  <li>Bootloader：Adafruit nRF52 UF2 <b>v0.10.0</b>（nice!nano fork）</li>
  <li>SoftDevice：Nordic <b>S140 v6.1.1</b>（BLE 协议栈）</li>
  <li>应用层：ZMK 定制分支（Smart Space、Toggle Mouse、RGB Status LED、Reset Settings 等自定义 behavior）</li>
</ul>

<h2><span class="num">12</span> 硬件规格</h2>
<table>
  <tr><th>项目</th><th>参数</th></tr>
  <tr><td>主控</td><td>nRF52840（Nice!Nano v2 兼容）</td></tr>
  <tr><td>无线</td><td>BLE 5.0（S140 v6.1.1）+ USB HID</td></tr>
  <tr><td>键盘矩阵</td><td>6 行 × 13 列，二极管方向 row2col</td></tr>
  <tr><td>去抖</td><td>按下 10 ms / 释放 10 ms</td></tr>
  <tr><td>IMU</td><td>QMI8658A 6 轴（I²C）</td></tr>
  <tr><td>外部 I²C / Qwiic</td><td>JST-SH 1.0mm 4-pin（GND / 3V3 / SDA / SCL），兼容 Qwiic / STEMMA QT</td></tr>
  <tr><td>背光</td><td>PWM 驱动 AP3032 升压 LED driver @ P0.15</td></tr>
  <tr><td>RGB 状态灯</td><td>PWM1 × 3 通道（R / G / B）</td></tr>
  <tr><td>外部电源控制</td><td>P0.13 → LDO CE（<code>Fn + ]</code> 切换）</td></tr>
  <tr><td>充电</td><td>USB-C，板载管理，红灯指示</td></tr>
  <tr><td>蓝牙绑定</td><td>最多 6 台设备（<code>CONFIG_BT_MAX_PAIRED=6</code>）</td></tr>
  <tr><td>电池</td><td>LP301060 锂聚合物（约 250 mAh）</td></tr>
  <tr><td>USB 标识</td><td>VID <code>0x1209</code> / PID <code>0x0001</code>，<code>TypixNode Keyboard</code></td></tr>
  <tr><td>BLE 设备名</td><td><code>TypixNode KBD</code></td></tr>
</table>

<h2><span class="num">13</span> 常见问题（FAQ）</h2>
<p><b>Q：怎么把键盘连到第二台、第三台设备？</b><br>A：<b>Fn + 不同的符号键</b> 切到别的蓝牙槽位再配对即可，最多 6 台，互不覆盖。不再需要每次清除。</p>
<p><b>Q：某台主机配对抽风 / 连不上？</b><br>A：先 <b>Fn + Enter</b> 清掉<b>当前</b>这台的配对重配；还不行用 <b>Fn + C</b> 重置全部设置。</p>
<p><b>Q：背光不亮？</b><br>A：背光只在 USB 通电时可用，BLE 模式自动关闭。<b>Fn + 空格</b> 调亮度。</p>
<p><b>Q：电量显示不准？</b><br>A：首次连接等 1 分钟左右让 BLE 电池服务同步。</p>
<p><b>Q：Fn + B 后没出现 NICENANO 盘？</b><br>A：USB 线可能只通电不走数据，换一根 data 线，或双击 reset 键。</p>
<p><b>Q：按 Fn + 右 Shift 有时关机有时切飞鼠？</b><br>A：75ms <b>同按</b>切飞鼠；<b>分前后</b>按走软关机。想关机慢点按，想切飞鼠同时按。</p>
<p><b>Q：长期不用怎么处理？</b><br>A：硬件开关拨 OFF 物理断电，配对信息保留在 flash 不丢失。</p>
"""

PART_EN = r"""
<div class="langbar pagebreak"><span class="tag">EN</span> English Manual</div>

<p class="lead">The TypixNode is a card-sized <b>BLE + USB dual-mode</b> portable keyboard built on an <b>nRF52840</b>
(Nice!Nano v2 compatible) running <b>ZMK</b> firmware. It pairs with <b>up to 6 Bluetooth devices</b>,
carries a <b>QMI8658A 6-axis IMU</b> for an air-mouse, and has an RGB status LED plus white backlight.
On BLE it reports battery natively to macOS / iOS. About <b>69 keys</b> with one <b>Fn layer</b>.</p>

<h2><span class="num">1</span> Overview</h2>
<div class="cols">
  <div>
    <table class="kv">
      <tr><td>Product</td><td>TypixNode (CyberFly hardware)</td></tr>
      <tr><td>Type</td><td>BLE + USB dual-mode keyboard</td></tr>
      <tr><td>MCU</td><td>nRF52840 (Nice!Nano v2 compatible)</td></tr>
      <tr><td>Firmware</td><td>ZMK (custom fork)</td></tr>
      <tr><td>Bluetooth</td><td>BLE 5.0, up to <b>6 paired devices</b></td></tr>
      <tr><td>Air mouse</td><td>QMI8658A 6-axis IMU</td></tr>
      <tr><td>Backlight</td><td>White, USB-power only</td></tr>
      <tr><td>Battery</td><td>LiPo LP301060 (~250&nbsp;mAh)</td></tr>
    </table>
  </div>
  <div>
    <figure>
      <img src="images/hero_lit.jpg" alt="TypixNode backlit">
      <figcaption>Clear acrylic with white backlight; the red / white LEDs are charge / USB indicators</figcaption>
    </figure>
  </div>
</div>

<h2><span class="num">2</span> Indicator LEDs</h2>
<table>
  <tr><th>Location</th><th>LED</th><th>Meaning</th></tr>
  <tr><td><b>Top</b> of board</td><td><span class="dot rgb"></span><b>RGB</b></td><td>Status (boot animation, USB cycle, BLE heartbeat, mouse toggle)</td></tr>
  <tr><td>Next to RGB</td><td><span class="dot r"></span><b>Red</b></td><td>Solid while charging, off when full</td></tr>
  <tr><td><b>Bottom</b> of board</td><td><span class="dot w"></span><b>White</b></td><td>USB 5V power present</td></tr>
</table>
<h3>RGB status details</h3>
<table>
  <tr><th>Scene</th><th>Effect</th></tr>
  <tr><td>Boot</td><td>Red → Green → Blue flash once, then off</td></tr>
  <tr><td>USB connected</td><td>Continuous colour cycle</td></tr>
  <tr><td>BLE standby</td><td><span class="dot b"></span><b>Blue double-blink</b> every 5 s (heartbeat)</td></tr>
  <tr><td>Mouse toggle</td><td>OFF=<span class="dot r"></span>red / M1=<span class="dot g"></span>green / M2=<span class="dot b"></span>blue blink</td></tr>
</table>

<h2><span class="num">3</span> Operating Modes</h2>
<table>
  <tr><th>Mode</th><th>Link</th><th>Backlight</th><th>Air mouse</th></tr>
  <tr><td><span class="badge usb">USB</span></td><td>USB-C cable</td><td>Available (Fn+Space)</td><td>Available</td></tr>
  <tr><td><span class="badge ble">BLE</span></td><td>Bluetooth</td><td>Auto-off (saving)</td><td>Manual enable</td></tr>
</table>
<div class="tip"><b>Backlight is USB-power only</b> — it turns off when unplugged (<code>AUTO_OFF_USB</code>) and when idle (<code>AUTO_OFF_IDLE</code>).</div>

<h2><span class="num">4</span> Keymap · Base Layer</h2>
<p>The diagram shows the <b>physical layout</b> as silk-screened (standard QWERTY). Small top-left = <b>Shift</b> symbol; keys marked <b>··</b> have a <b>double-tap</b> action (see §7).</p>
{base_en}
<div class="legend-row">
  <span>■ ▲ ✕ ● ♣ ◆ &nbsp;=&nbsp; six coloured symbol keys = <b>F1–F6</b></span>
  <span>·· = double-tap action</span>
  <span>top-left small = Shift</span>
</div>

<h2><span class="num">5</span> Keymap · Fn Layer</h2>
<p>Hold the left <b>Fn</b> key (CapsLock position). Highlighted keys change; grey ones pass through.
<span class="badge ble">Cyan</span> = Bluetooth / output, <span class="badge" style="background:#8b5cf6">violet</span> = other functions.</p>
{fn_en}
<table>
  <tr><th>Hold Fn +</th><th>Function</th></tr>
  <tr><td>Esc</td><td>Toggle <b>USB / BLE</b> output (<code>OUT_TOG</code>)</td></tr>
  <tr><td>■ ▲ ✕ ● ♣ ◆</td><td>Switch to <b>Bluetooth device 1–6</b> (<code>BT_SEL 0–5</code>)</td></tr>
  <tr><td>Enter</td><td>Clear the <b>current device</b>'s bond (<code>BT_CLR</code>) to re-pair that slot</td></tr>
  <tr><td><code>1</code>–<code>0</code> / <code>-</code> / <code>=</code></td><td>F1–F10 / F11 / F12</td></tr>
  <tr><td>⌫ Backspace</td><td>Delete</td></tr>
  <tr><td>↑ / ↓ / ← / →</td><td>PgUp / PgDn / Home / End</td></tr>
  <tr><td>Space</td><td>Cycle backlight (<code>BL_CYCLE</code>)</td></tr>
  <tr><td>Left Alt / Right Alt</td><td>Toggle <b>6-axis air mouse</b> (OFF → M1 → M2)</td></tr>
  <tr><td>Right Shift (hold)</td><td>Soft off (<code>soft_off</code>)</td></tr>
  <tr><td>] </td><td>External power toggle (<code>EP_TOG</code>)</td></tr>
  <tr><td>Q / A / M</td><td>Screenshot / select-all+copy / <code>() =&gt; {{}}</code> macro</td></tr>
  <tr><td>C</td><td>Reset all settings (erase NVS) and reboot ⭐</td></tr>
  <tr><td>B</td><td>Enter bootloader (UF2)</td></tr>
</table>

<h2><span class="num">6</span> Multi-device Bluetooth</h2>
<p>The firmware supports <b>up to 6 paired devices</b> (<code>CONFIG_BT_MAX_PAIRED=6</code>), switched with Fn + the top symbol keys.</p>
<table>
  <tr><th>Action</th><th>Keys</th></tr>
  <tr><td>Select / switch to device 1–6</td><td><b>Fn + ■ / ▲ / ✕ / ● / ♣ / ◆</b></td></tr>
  <tr><td>Clear current device's bond (re-pair slot)</td><td><b>Fn + Enter</b></td></tr>
  <tr><td>Toggle USB / BLE output</td><td><b>Fn + Esc</b></td></tr>
  <tr><td>Reset all settings (wipe all bonds + reboot)</td><td><b>Fn + C</b> ⭐</td></tr>
</table>
<h3>Pairing</h3>
<ol>
  <li><b>Fn + symbol key</b> to pick an empty slot (e.g. device 1 = Fn + ■).</li>
  <li>The keyboard advertises; find <code>TypixNode KBD</code> in the host's Bluetooth settings and pair.</li>
  <li>Battery then shows up in the host's device card.</li>
  <li>To use another host, <b>Fn + a different symbol key</b> and pair — <b>slots don't overwrite each other</b>.</li>
</ol>
<div class="key-cta"><b>Two kinds of clearing:</b><br>
• <b>Fn + Enter</b> = clear only the <b>current</b> device (others kept).<br>
• <b>Fn + C</b> = <b>nuclear</b>: wipe <b>all</b> bonds, name cache and settings, then reboot. Use when pairing is fully stuck.</div>
<h3>Battery display</h3>
<ul>
  <li><b>macOS</b>: System Settings → Bluetooth → device card.</li>
  <li><b>iOS / iPadOS</b>: add the Batteries widget.</li>
  <li>Protocol: standard <b>BLE Battery Service (0x180F)</b>.</li>
</ul>

<h2><span class="num">7</span> Hidden Tricks: Double-tap / Combos / Macros</h2>
<h3>Tap-dance</h3>
<table>
  <tr><th>Key</th><th>Single</th><th>Double</th></tr>
  <tr><td><b>Esc</b></td><td>Esc</td><td>Caps Word (one-shot caps, ends on space)</td></tr>
  <tr><td><b>Left Shift</b></td><td>Shift</td><td>Caps Lock</td></tr>
</table>
<h3>Combos (press together)</h3>
<table>
  <tr><th>Together</th><th>Sends</th><th>Window</th></tr>
  <tr><td><b>J + K</b></td><td>Esc</td><td>50 ms</td></tr>
  <tr><td><b>D + F</b></td><td>Tab</td><td>50 ms</td></tr>
  <tr><td><b>F + J</b></td><td>Enter</td><td>50 ms</td></tr>
  <tr><td><b>J + K + L</b></td><td>Caps Word</td><td>50 ms</td></tr>
  <tr><td><b>Fn + Right Shift</b></td><td>Toggle air mouse</td><td>75 ms</td></tr>
</table>
<h3>Macros (Fn layer)</h3>
<table>
  <tr><th>Key</th><th>Macro</th></tr>
  <tr><td>Fn + Q</td><td>Screenshot (⌘ + Shift + 4)</td></tr>
  <tr><td>Fn + A</td><td>Select all + copy (Ctrl+A → 50ms → Ctrl+C)</td></tr>
  <tr><td>Fn + M</td><td>Type <code>() =&gt; {{}}</code></td></tr>
</table>
<div class="warn"><b>About Fn + Right Shift:</b> pressed <b>together</b> within 75 ms it toggles the air mouse; pressed <b>in sequence</b> it triggers <b>soft-off</b> on the Fn layer.</div>

<h2><span class="num">8</span> 6-axis Air Mouse</h2>
<p>On-board <b>QMI8658A</b> 6-axis IMU (accel + gyro, I²C). Three modes, cycled:</p>
<table>
  <tr><th>Mode</th><th>Algorithm</th><th>LED</th><th>Feel</th></tr>
  <tr><td><b>OFF</b></td><td>Off, IMU sleeps</td><td><span class="dot r"></span>red</td><td>keyboard only</td></tr>
  <tr><td><b>M1</b></td><td>Kalman filter + state-space fusion</td><td><span class="dot g"></span>green</td><td>steady</td></tr>
  <tr><td><b>M2</b></td><td>Accelerometer tilt-to-velocity (fallback)</td><td><span class="dot b"></span>blue</td><td>responsive</td></tr>
</table>
<p><b>Three ways to toggle:</b> Fn + Right Shift (within 75 ms), Fn + Left Alt, Fn + Right Alt. The RGB blinks the matching colour to confirm.</p>
<h3>Smart Space: spacebar becomes mouse buttons when the mouse is on</h3>
<table>
  <tr><th>Position</th><th>OFF</th><th>ON (M1/M2)</th></tr>
  <tr><td>Left space</td><td>Space</td><td><b>Left click</b></td></tr>
  <tr><td>Middle space</td><td>Space</td><td>Space (kept)</td></tr>
  <tr><td>Right space</td><td>Space</td><td><b>Right click</b></td></tr>
</table>
<div class="note"><b>Note:</b> the air mouse is still being tuned (drift filtering, accel curve) — experimental for now.</div>

<h2><span class="num">9</span> Backlight</h2>
<ul>
  <li>White backlight via an <b>AP3032 boost driver</b> (P0.15), <b>off</b> at boot, 20% steps.</li>
  <li><b>Fn + Space</b> cycles brightness.</li>
  <li>Only available on <b>USB power</b>; turns off when unplugged or idle.</li>
</ul>

<h2><span class="num">10</span> Power / Charging / Switch</h2>
<ul>
  <li>Charge port: <b>USB-C</b> with on-board charging; <span class="dot r"></span>red LED solid while charging, off when full.</li>
  <li><span class="dot w"></span>White LED = USB 5V present.</li>
  <li>Hardware slide switch: <b>ON</b> = battery on, BLE active; <b>OFF</b> = physically disconnect battery for zero-drain storage.</li>
  <li><b>Fn + Right Shift</b> (hold) soft-off; <b>Fn + ]</b> toggles external power (<code>EP_TOG</code>).</li>
  <li>Pairing data lives in flash NVS — <b>kept across power loss</b>. BLE standby &gt; 48 h.</li>
</ul>

<h2><span class="num">11</span> Bootloader / Firmware</h2>
<h3>Two ways into the bootloader</h3>
<ol>
  <li><b>Fn + B</b> (while running).</li>
  <li><b>Double-tap the reset button</b> (if firmware is stuck).</li>
</ol>
<p>Then the main LED breathes slowly and a FAT drive named <code>NICENANO</code> appears — drop a <code>.uf2</code> onto it to flash and auto-reboot.</p>
<h3>Build locally</h3>
<pre><code>cd cyberfly_zmk
rm -rf build &amp;&amp; .venv/bin/west build -s app -p \
  -b nice_nano/nrf52840/zmk -- -DSHIELD=cyberfly
# output: build/zephyr/zmk.uf2</code></pre>
<h3>Firmware stack</h3>
<ul>
  <li>Bootloader: Adafruit nRF52 UF2 <b>v0.10.0</b> (nice!nano fork)</li>
  <li>SoftDevice: Nordic <b>S140 v6.1.1</b></li>
  <li>App: custom ZMK fork (Smart Space, Toggle Mouse, RGB Status LED, Reset Settings behaviours)</li>
</ul>

<h2><span class="num">12</span> Hardware Specifications</h2>
<table>
  <tr><th>Item</th><th>Spec</th></tr>
  <tr><td>MCU</td><td>nRF52840 (Nice!Nano v2 compatible)</td></tr>
  <tr><td>Wireless</td><td>BLE 5.0 (S140 v6.1.1) + USB HID</td></tr>
  <tr><td>Matrix</td><td>6 rows × 13 cols, row2col diodes</td></tr>
  <tr><td>Debounce</td><td>press 10 ms / release 10 ms</td></tr>
  <tr><td>IMU</td><td>QMI8658A 6-axis (I²C)</td></tr>
  <tr><td>External I²C / Qwiic</td><td>JST-SH 1.0mm 4-pin (GND / 3V3 / SDA / SCL), Qwiic / STEMMA QT compatible</td></tr>
  <tr><td>Backlight</td><td>PWM AP3032 boost LED driver @ P0.15</td></tr>
  <tr><td>RGB status LED</td><td>PWM1 × 3 channels (R / G / B)</td></tr>
  <tr><td>External power</td><td>P0.13 → LDO CE (<code>Fn + ]</code>)</td></tr>
  <tr><td>Charging</td><td>USB-C, on-board, red LED</td></tr>
  <tr><td>BT bonding</td><td>up to 6 devices (<code>CONFIG_BT_MAX_PAIRED=6</code>)</td></tr>
  <tr><td>Battery</td><td>LP301060 LiPo (~250 mAh)</td></tr>
  <tr><td>USB IDs</td><td>VID <code>0x1209</code> / PID <code>0x0001</code>, <code>TypixNode Keyboard</code></td></tr>
  <tr><td>BLE name</td><td><code>TypixNode KBD</code></td></tr>
</table>

<h2><span class="num">13</span> FAQ</h2>
<p><b>Q: How do I connect to a 2nd / 3rd device?</b><br>A: <b>Fn + a different symbol key</b> selects another Bluetooth slot — pair there. Up to 6, none overwrite each other.</p>
<p><b>Q: A host won't connect / pairing is flaky?</b><br>A: <b>Fn + Enter</b> clears the <b>current</b> device's bond and re-pair; if still stuck, <b>Fn + C</b> resets everything.</p>
<p><b>Q: Backlight is off?</b><br>A: It's USB-power only and auto-off on BLE. <b>Fn + Space</b> adjusts brightness.</p>
<p><b>Q: Battery % looks wrong?</b><br>A: Wait ~1 min after connecting for the BLE battery service to sync.</p>
<p><b>Q: No NICENANO drive after Fn + B?</b><br>A: The cable may be charge-only — use a data cable, or double-tap reset.</p>
<p><b>Q: Fn + Right Shift sometimes powers off, sometimes toggles the mouse?</b><br>A: Together within 75 ms = mouse; in sequence = soft-off.</p>
<p><b>Q: Long-term storage?</b><br>A: Flip the hardware switch OFF — pairing data is retained in flash.</p>

</body>
</html>
"""

TEMPLATE = PART_HEAD + PART_CN + PART_CN2 + PART_EN

