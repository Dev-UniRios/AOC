# Define o caminho do arquivo de saída
$arquivoSaida = "C:\Monitoramento\Relatorio_Processos.txt"

# Limpa o conteúdo anterior do arquivo
Clear-Content $arquivoSaida

# Adiciona um cabeçalho ao arquivo
Add-Content $arquivoSaida "Monitoramento de Processos - Uso de CPU e Memória"
Add-Content $arquivoSaida "==========================================="
Add-Content $arquivoSaida "Data/Hora: $(Get-Date)"
Add-Content $arquivoSaida ""

# Obtém os processos em execução e filtra os que estão usando mais de 10% de CPU ou mais de 100MB de memória
$processos = Get-Process | Where-Object {
    $_.CPU -gt 10 -or $_.WorkingSet64 -gt 100MB
}

# Adiciona os resultados ao arquivo
foreach ($processo in $processos) {
    $nome = $processo.ProcessName
    $usoCPU = [math]::Round($processo.CPU, 2)
    $memoriaMB = [math]::Round($processo.WorkingSet64 / 1MB, 2)

    Add-Content $arquivoSaida "Nome do Processo: $nome"
    Add-Content $arquivoSaida "Uso de CPU: $usoCPU %"
    Add-Content $arquivoSaida "Memória Usada: $memoriaMB MB"
    Add-Content $arquivoSaida "-------------------------------------------"
}

# Exibe uma mensagem de conclusão
Write-Host "Monitoramento concluído! Os resultados foram salvos em $arquivoSaida"
