// Terraform provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

// Set region variable - pull from terraform.tfvars
variable "region" {
  type = string
}

// Setup AWS Provider and variables
provider "aws" {
  region = var.region
}