# simple-infrastructure
[![Build Status](https://travis-ci.org/99stealth/simple-infrastructure.svg?branch=master)](https://travis-ci.org/99stealth/simple-infrastructure)

This project is created only for educational purposes. So, feel free to *fork* and use it

## Requirements
In order to use current build and deployment process you need to have:
- GitHub account (thanks captain obvious)
- AWS account and one existing KeyPair
- Travis CI account

## Travis CI setup
Continuous integration and deployment process for current project is running on Travis CI. 
- In order to proceed with Travis CI go to https://travis-ci.org and [Sign Up](https://travis-ci.org "TravisCI") using your GitHub account
- Now go to https://travis-ci.org/account/repositories and find `simple-infrastructure`. Switch on checkboxes it will allow you to build the project with Travis CI
- Now go to the job and press `More options > Settings`
- Here you need to add several environment variables like
  - `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` of your who has access to `ecs*`, `cloudformation*`, `ec2*`, `iam*`
  - `AWS_DEFAULT_REGION` where you specify AWS region where your cluster is deployed
  - `SSH_KEY_NAME` where you specify KeyPair name which will be used with your ECS Container instances
- Now run the build and enjoy the automation

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

## Changes in source code
It is obviously that you may want to make some changes in source code or other components. So, here are several things that you should know:
- After you make a `git push` build will be trigered
- If build is trigered from `master` branch it will also run a deploy process
- If you are changing files which are not affecting the application you may not need to run build. So, in order to make commit without build you need to run commit command with `[skip ci]` in message body, for example:
```
git add README.md
git commit -m "Commit with something important in README.md [skip ci]"
git push
```