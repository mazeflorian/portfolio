#!/bin/bash 

set -euo pipefail

apply_terraform_configuration(){
    if terraform apply; then 
        echo "terraform apply done"
    else
        echo "terraform apply failed"
    fi
}

apply_terraform_configuration(){
    if terraform plan; then 
        echo "terraform plan done"
        apply_terraform_configuration
    else
        echo "terraform plan failed"
    fi
}

apply_terraform_configuration