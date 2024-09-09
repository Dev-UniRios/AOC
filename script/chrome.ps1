for ($i=0; $i -le 10; $i++) {
    Get-Process| where {($_.ProcessName -like "chrome") -and ($_.ws -gt 300000000)}
    Start-Sleep 3
}
