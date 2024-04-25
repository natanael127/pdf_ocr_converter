# Checking for administrative privileges
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
{
    # Re-launch the script with administrator rights
    $arguments = "& '" + $myinvocation.mycommand.definition + "'"
    Start-Process powershell -Verb runAs -ArgumentList $arguments
    Exit
}

# Install chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install tesseract and ghostscript
choco install tesseract ghostscript -y

# Add Portuguese language support to the data dir of Tesseract (using environment variable for program files)
$TessdataDir = "$env:ProgramFiles\Tesseract-OCR\tessdata"
$Url = "https://github.com/tesseract-ocr/tessdata/raw/main/por.traineddata"
$DestFile = Join-Path -Path $TessdataDir -ChildPath "por.traineddata"

# Ensure the tessdata directory exists
if (-not (Test-Path -Path $TessdataDir)) {
    New-Item -ItemType Directory -Path $TessdataDir
}

# Download the traineddata file if it does not exist
if (-not (Test-Path -Path $DestFile)) {
    Invoke-WebRequest -Uri $Url -OutFile $DestFile
}

