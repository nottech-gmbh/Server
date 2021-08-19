#[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$Script = Invoke-RestMethod -uri https://api.github.com/repos/nottech-gmbh/Client/contents/Get-Date.ps1?access_token=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 -Headers @{”Accept”= “application/vnd.github.v3.raw”}

Invoke-Expression $Script

