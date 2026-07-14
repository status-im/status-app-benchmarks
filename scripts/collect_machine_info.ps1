# Collect Windows system metadata for benchmark.py parse --machine-info.
# Usage: powershell -File scripts/collect_machine_info.ps1 [-OutputPath machine_info.json]

param(
    [string]$OutputPath = "machine_info.json"
)

function Get-OsBuild {
    try {
        $reg = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
        $build = $reg.CurrentBuild
        if ($null -ne $reg.UBR) {
            return "$build.$($reg.UBR)"
        }
        return [string]$build
    } catch {
        return $null
    }
}

function Get-WindowsVersion {
    try {
        $reg = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
        $name = $reg.ProductName
        $display = $reg.DisplayVersion
        if ($display) {
            return "$name $display".Trim()
        }
        return [string]$name
    } catch {
        return $null
    }
}

function Get-CpuName {
    try {
        return (Get-CimInstance Win32_Processor | Select-Object -First 1).Name.Trim()
    } catch {
        return $null
    }
}

function Get-RamGb {
    try {
        $bytes = (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory
        return [string]([math]::Round($bytes / 1GB))
    } catch {
        return $null
    }
}

$windowsVersion = Get-WindowsVersion
$osBuild = Get-OsBuild

if (-not $windowsVersion) {
    try {
        $os = Get-CimInstance Win32_OperatingSystem
        $windowsVersion = $os.Caption
        if (-not $osBuild) {
            $osBuild = [string]$os.BuildNumber
        }
    } catch {
        $windowsVersion = $null
    }
}

$machineInfo = [ordered]@{
    hostname        = $env:COMPUTERNAME
    windows_version = $windowsVersion
    os_build        = $osBuild
    cpu             = Get-CpuName
    ram_gb          = Get-RamGb
}

$json = $machineInfo | ConvertTo-Json
Set-Content -Path $OutputPath -Value $json -Encoding utf8
Write-Output "Wrote machine info to $OutputPath"
