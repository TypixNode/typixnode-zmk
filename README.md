# TypixNode Keyboard

A compact BLE mechanical keyboard powered by the nRF52840 running [ZMK](https://zmk.dev/) firmware.

## Features

- nRF52840 BLE 5.0 + USB-C dual mode
- 6-row compact QWERTY layout with PlayStation-style function keys
- 6-axis QMI8658A IMU air-mouse
- Up to 6 paired Bluetooth devices, native battery on macOS / iOS
- Built-in Li-battery with charging
- Open-source hardware and firmware ([MIT](LICENSE))
- USB VID:PID `1209:0001` ([pid.codes](https://pid.codes/1209/))

## Manual

Full bilingual (中文 / English) manual: [manual/MANUAL.md](manual/MANUAL.md) · PDF: [manual/TypixNode_Manual.pdf](manual/TypixNode_Manual.pdf)

## Photos

| Front (backlight on) | Front (daylight) |
|---|---|
| ![TypixNode Keyboard - Backlight](images/cyberfly_keyboard_front_lit.jpg) | ![TypixNode Keyboard - Daylight](images/cyberfly_keyboard_front.jpg) |

## Firmware

This repository is a fork of [ZMK Firmware](https://zmk.dev/) with TypixNode-specific board definitions and keymap configurations.

[![Build](https://github.com/TypixNode/typixdeck-zmk/workflows/Build/badge.svg)](https://github.com/TypixNode/typixdeck-zmk/actions)

Check out the ZMK website to learn more: https://zmk.dev/
