# run.ps1

# Путь к виртуальному окружению
$venvPath = ".\.venv\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    Write-Host "✅ Активация виртуального окружения..."
    & $venvPath

    # Теперь ты можешь запускать flask (или любые команды)
    Write-Host "💡 Введите команду, например: flask --app flaskr run"
}
else {
    Write-Host "❌ Виртуальное окружение не найдено по пути $venvPath"
    Write-Host "👉 Создай окружение командой: python -m venv .venv"
}
