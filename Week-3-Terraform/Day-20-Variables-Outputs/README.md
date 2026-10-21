**Week 3 – Day 20: Terraform Variables and Outputs**

**Objective**

Learn how to use Terraform variables to configure AWS resources and outputs to display resource information.

**Topics Practiced**

- Terraform input variables
- AWS region variable
- EC2 instance type variable
- Terraform outputs
- Terraform formatting and validation
- Terraform plan

**Files Created**

- `main.tf` – Defines the AWS provider, security group, and EC2 instance configuration
- `variables.tf` – Defines the AWS region and EC2 instance type variables
- `outputs.tf` – Defines outputs for the EC2 instance ID and public IP
- `.terraform.lock.hcl` – Records the selected Terraform provider version

**Variables Practiced**

- `aws_region` – `ap-south-1`
- `instance_type` – `t3.micro`

**Outputs Defined**

- `instance_id` – Displays the EC2 instance ID after deployment
- `public_ip` – Displays the EC2 public IP address after deployment

**Commands Practiced**

- `terraform fmt`
- `terraform init`
- `terraform validate`
- `terraform plan`

**Result**

The Terraform configuration was formatted, initialized, validated, and reviewed using `terraform plan`.

The plan showed two resources would be created. I did not apply the Day 20 plan, avoiding a duplicate EC2 deployment.

**What I Learned**

I learned how variables make Terraform configurations easier to reuse and how outputs can display useful information about deployed resources.

**Status**

**Week 3 – Day 20: Configuration Completed**
