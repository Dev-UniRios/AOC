for ($i=0; $i -le 10; $i++) {
    # Passo 1: Obtém todos os processos em execução no sistema com o comando Get-Process.
    # Passo 2: Filtra os processos, mantendo apenas aqueles cujo nome contém "chrome" 
    # e que estejam utilizando mais de 300 MB de memória (WorkingSet).
    Get-Process | where {($_.ProcessName -like "chrome") -and ($_.ws -gt 300000000)}

    # Passo 3: Faz uma pausa de 3 segundos antes de executar a próxima iteração do loop.
    Start-Sleep 3
}
