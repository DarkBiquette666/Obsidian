# Setup RPG Engine Development Environment - Safe Build

$Source = "$PSScriptRoot\_Engine\PluginSource"
$Dest = "D:\Git\Obsidian Plugins\obsidian-rpg-engine"
$VaultPluginDir = "$PSScriptRoot\.obsidian\plugins\obsidian-rpg-engine"

Write-Host ">>> Starting RPG Engine Setup..." -ForegroundColor Cyan

# 1. Create Git Directory
if (-not (Test-Path $Dest)) {
    New-Item -ItemType Directory -Path $Dest -Force | Out-Null
    Write-Host "[OK] Created $Dest" -ForegroundColor Green
}

# 2. Copy Source Files
Copy-Item -Path "$Source\*" -Destination $Dest -Recurse -Force
Write-Host "[OK] Copied source files." -ForegroundColor Green

# 3. Create Vault Plugin Directory
if (-not (Test-Path $VaultPluginDir)) {
    New-Item -ItemType Directory -Path $VaultPluginDir -Force | Out-Null
}

# 4. NPM Install & Build
Write-Host ">>> Running NPM Install & Build in $Dest..." -ForegroundColor Cyan
Push-Location $Dest

try {
    npm --version | Out-Null
} catch {
    Write-Error "Node.js (npm) is not found in PATH."
    Pop-Location
    exit 1
}

# Run install
Write-Host "   - npm install..."
$installProcess = Start-Process -FilePath "cmd.exe" -ArgumentList "/c npm install" -Wait -PassThru -NoNewWindow
if ($installProcess.ExitCode -ne 0) {
    Write-Error "NPM INSTALL FAILED. Stopping."
    Pop-Location
    exit 1
}

# Run build
Write-Host "   - npm run build..."
$buildProcess = Start-Process -FilePath "cmd.exe" -ArgumentList "/c npm run build" -Wait -PassThru -NoNewWindow
if ($buildProcess.ExitCode -ne 0) {
    Write-Error "BUILD FAILED (TypeScript Errors). Deployment aborted."
    Pop-Location
    exit 1
}

# 5. Deploy to Vault
Write-Host ">>> Deploying to Vault..." -ForegroundColor Cyan
Copy-Item "main.js" -Destination $VaultPluginDir -Force
Copy-Item "manifest.json" -Destination $VaultPluginDir -Force
Copy-Item "styles.css" -Destination $VaultPluginDir -ErrorAction SilentlyContinue

Pop-Location

Write-Host "`n>>> SUCCESS! RPG Engine is installed." -ForegroundColor Green
