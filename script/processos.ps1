# Define o caminho do arquivo de log onde os dados de desempenho serão salvos
$arquivoLog = "C:\Monitoramento\Relatorio_Desempenho.txt"

# Limpa o conteúdo anterior do arquivo de log
Clear-Content $arquivoLog

# Cabeçalho do relatório
Add-Content $arquivoLog "Relatório de Desempenho de Processos Críticos"
Add-Content $arquivoLog "============================================="
Add-Content $arquivoLog "Data/Hora: $(Get-Date)"
Add-Content $arquivoLog ""

# Loop para monitorar desempenho por 10 iterações (10 medições) com intervalo de 5 segundos
for ($i=0; $i -le 10; $i++) {
    
    # Obtém os processos críticos que deseja monitorar (pode adicionar mais processos conforme necessário)
    $processos = Get-Process | Where-Object {
        $_.ProcessName -in @("chrome", "explorer", "notepad")
    }

    # Para cada processo encontrado, adiciona suas informações ao log
    foreach ($processo in $processos) {
        $nome = $processo.ProcessName
        $usoCPU = [math]::Round($processo.CPU, 2)  # Uso de CPU em segundos
        $memoriaMB = [math]::Round($processo.WorkingSet64 / 1MB, 2)  # Memória em MB

        # Adiciona as informações ao arquivo de log
        Add-Content $arquivoLog "Nome do Processo: $nome"
        Add-Content $arquivoLog "Uso de CPU: $usoCPU segundos"
        Add-Content $arquivoLog "Memória Usada: $memoriaMB MB"
        Add-Content $arquivoLog "-------------------------------------------"
    }

    # Adiciona uma linha de separação para cada medição
    Add-Content $arquivoLog "Medição concluída em: $(Get-Date)"
    Add-Content $arquivoLog "============================================="
    Add-Content $arquivoLog ""

    # Pausa de 5 segundos antes da próxima medição
    Start-Sleep 5
}

# Exibe uma mensagem de conclusão
Write-Host "Monitoramento concluído! O relatório foi salvo em $arquivoLog"
