# simple-infrastructure
[![Build Status](https://travis-ci.org/99stealth/simple-infrastructure.svg?branch=master)](https://travis-ci.org/99stealth/simple-infrastructure)

This project is created only for educational purposes. So, feel free to *fork* and use it

## High level architecture
Current infrastructure is deployed to AWS your AWS account using CloudFormation templates. There are two separate templates `network_components.yml` and `network_components.yml`.
`network_components.yml` deploys such components as:
- VPC
- Internet Gateway
- Two Private Subnets in two different AZs
- Two Public Subnets in two different AZs
- Two NAT Gateways in both Private Subnets
- Two Elastic IPs for NAT Gateways
- Route Tables for Subnets
`cluster_components.yml` deploys such components as:
- Two Security Groups. 
  - Security group for ALB 
  - Security group for ECS instances
- Four IAM roles and one Instance profile. 
  - EC2 role
  - ECS Autoscaling role
  - ECS Task execution role
  - ECS Service role
- ECS Cluste
- Launch configuration and AutoScaling group
- Application Load Balancer and its Listener (which listens on port 80)

![Simple infrastructure](.images/simple_random_infrastructure_diagram.png "Title")

_Figure 1. Simple random architecture_

## If you change infrastructure
If you desided to add or remove any component from infrastructure, please make that change also on diagram which is stored in .images/simple_random_infrastructure_diagram. Regenerate `png` file and update it in the `README.md` in [High level architecture](#high-level-architecture)