param(
    [string]$Repository = "che626/competition-ppt-template-first-skill"
)

$ErrorActionPreference = "Stop"
$skillFile = Join-Path $PSScriptRoot "..\SKILL.md"
$content = Get-Content -Raw -Encoding UTF8 $skillFile

if ($content -notmatch '(?s)^---\s*\r?\nname:\s*competition-ppt-template-first\s*\r?\ndescription:\s*["'']') {
    throw "SKILL.md front matter must expose the expected name and a quoted YAML description."
}

Write-Output "LOCAL_FRONT_MATTER=OK"
Write-Output "Checking Skills CLI discovery for $Repository ..."

npx -y skills@latest add $Repository --list
if ($LASTEXITCODE -ne 0) {
    throw "Skills CLI could not discover a valid skill in $Repository."
}

Write-Output "SKILLS_CLI_DISCOVERY=OK"
