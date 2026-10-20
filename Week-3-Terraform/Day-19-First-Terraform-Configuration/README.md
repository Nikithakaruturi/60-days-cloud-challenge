**Week 3 – Day 19: Create First Terraform Configuration**

**Objective**

Create and deploy a basic AWS infrastructure configuration using Terraform.

**Topics Practiced**

- Terraform
- Terraform AWS Provider
- Infrastructure as Code
- Amazon EC2
- Security Groups
- AWS VPC
- Terraform Plan
- Terraform Apply

**Hands-on Practice**

- Configured Terraform to use AWS
- Used the AWS region `ap-south-1`
- Used the existing AWS default VPC
- Selected an Ubuntu AMI using a Terraform data source
- Created a security group using Terraform
- Configured SSH access on port 22
- Created a `t3.micro` EC2 instance using Terraform
- Associated the security group with the EC2 instance
- Added tags to the AWS resources
- Used `terraform fmt` to format the configuration
- Used `terraform validate` to validate the configuration
- Used `terraform plan` to preview the infrastructure changes
- Used `terraform apply` to create the AWS resources

**Terraform Resources Created**

- Security Group: `terraform-day19-sg`
- EC2 Instance: `terraform-day19-vm`

**Terraform Commands Practiced**

`terraform fmt`

`terraform validate`

`terraform plan`

`terraform apply`

**Result**

Terraform successfully created:

- 1 Security Group
- 1 EC2 instance

**Terraform Output**

`Apply complete! Resources: 2 added, 0 changed, 0 destroyed.`

**What I Learned**

I learned how Terraform can be used as Infrastructure as Code to define and create AWS resources. I also learned the basic Terraform workflow of formatting, validating, planning, and applying infrastructure configurations.

**Status**

**Week 3 – Day 19: Completed**

