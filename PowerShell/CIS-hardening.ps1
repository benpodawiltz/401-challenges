#
# Author:           ben podawiltz
# Date of Revision: 7.10.21
# Purpose:          CIS Benchmark configuration
# Comment:          - 1st draft needs a lot of work still...
#
#
#
#
function menu_select {
    Write-Output "Choose one of the following:"
    Write-Output "1. Password Complexity Settings"
    Write-Output "2. Smbv1 Protocol"
    $choice = Read-host "Choice" 
       if ($choice -eq 1){
       Get-ADDefaultDomainPasswordPolicy
    }
    
}
 menu_select

