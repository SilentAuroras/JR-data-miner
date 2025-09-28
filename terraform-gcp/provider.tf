// Provider declaration
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.38.0"
    }
  }
}

// Set region variable - pull from terraform.tfvars
variable "region" {
  type = string
}

// Set project name - pull from terraform.tfvars
variable "project_name" {
  type = string
}

// Set Home IP for Airflow ACLs - pull from terraform.tfvars
variable "home-ip" {
  type = string
}

// Setup GCP provider
provider "google" {
  region = var.region
}