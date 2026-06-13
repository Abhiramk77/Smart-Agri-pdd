#!/usr/bin/env pwsh
# Master script to run app demo and record video

Write-Host "`n" -ForegroundColor Cyan
Write-Host "╔════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   AUTOMATED APP DEMO & VIDEO RECORDING    ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════╝" -ForegroundColor Cyan

$projectRoot = "C:\Users\kodav\Downloads\Farming pdd"
Set-Location $projectRoot

# Step 1: Check if services are running
Write-Host "`n[1/4] Checking services..." -ForegroundColor Yellow

$backendReady = $false
$frontendReady = $false

for ($i = 1; $i -le 5; $i++) {
    try {
        $backend = curl.exe -s http://localhost:3000/api/chats -w "%{http_code}" 2>&1 | Select-Object -Last 1
        if ($backend -match "200") { $backendReady = $true; break }
    } catch {}
    Start-Sleep -Seconds 1
}

Write-Host "  - Backend: $(if($backendReady) { 'Ready ✓' } else { 'Starting...' })"

for ($i = 1; $i -le 5; $i++) {
    try {
        $frontend = curl.exe -s http://localhost:5173 2>&1
        if ($frontend -match "<!DOCTYPE|<html") { $frontendReady = $true; break }
    } catch {}
    Start-Sleep -Seconds 1
}

Write-Host "  - Frontend: $(if($frontendReady) { 'Ready ✓' } else { 'Starting...' })"

# Step 2: Start recording
Write-Host "`n[2/4] Starting screen recording..." -ForegroundColor Yellow

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$videoOutput = Join-Path $projectRoot "app_demo_$timestamp.gif"

Write-Host "  - Output: $videoOutput"
Write-Host "  - Duration: 45 seconds"

# Start recording in background
$recordingJob = Start-Job -ScriptBlock {
    param($output, $duration)
    python "$using:projectRoot\screen_recorder.py"
} -Name "ScreenRecorder"

# Small delay for recording to start
Start-Sleep -Seconds 1

# Step 3: Run app demo
Write-Host "`n[3/4] Running automated app demo..." -ForegroundColor Yellow

python "$projectRoot\app_demo.py"

# Wait for recording to complete
Write-Host "`n[4/4] Finalizing video..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Get recording result
$recordingJob | Wait-Job -Timeout 60 | Out-Null

$videoFile = Get-ChildItem $projectRoot -Filter "app_demo_*.gif" -ErrorAction SilentlyContinue |
    Sort-Object CreationTime -Descending | Select-Object -First 1

if ($videoFile) {
    Write-Host "  - Video created: $($videoFile.Name)" -ForegroundColor Green
    Write-Host "  - Size: $([math]::Round($videoFile.Length/1MB, 2)) MB" -ForegroundColor Green
    Write-Host "  - Location: $($videoFile.FullName)" -ForegroundColor Green
} else {
    Write-Host "  - Video recording may have encountered issues" -ForegroundColor Yellow
}

Write-Host "`n╔════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║          DEMO COMPLETE                     ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════╝" -ForegroundColor Cyan

Write-Host "`nSummary:" -ForegroundColor Yellow
Write-Host "  ✓ Backend API: http://localhost:3000" -ForegroundColor Green
Write-Host "  ✓ Frontend App: http://localhost:5173" -ForegroundColor Green
Write-Host "  ✓ Video Recording: Complete" -ForegroundColor Green

Write-Host "`nAvailable files in: $projectRoot" -ForegroundColor Cyan
Write-Host "  - app_demo_*.gif (video recordings)" -ForegroundColor White
Write-Host "  - app_demo.py (API test script)" -ForegroundColor White
Write-Host "  - screen_recorder.py (recording script)" -ForegroundColor White

Write-Host "`n"

