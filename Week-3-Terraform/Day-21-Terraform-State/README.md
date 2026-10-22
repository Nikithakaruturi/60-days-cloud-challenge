**Week 3 – Day 21: Terraform State**

**Objective**

Understand how Terraform state tracks infrastructure and how Terraform reconciles configuration changes with existing resources.

**Topics Practiced**

- Terraform state
- `terraform.tfstate`
- Terraform resource tracking
- `terraform state list`
- Terraform plan
- Updating an existing resource
- Terraform apply

**Existing Resources**

The Day 19 Terraform configuration was used for this practice.

Resources tracked by Terraform included:

- `aws_instance.terraform_vm`
- `aws_security_group.terraform_sg`
- AWS VPC data source
- AWS AMI data source

**State File**

Verified that `terraform.tfstate` exists in the Day 19 Terraform project.

The state file allows Terraform to keep track of the infrastructure managed by the configuration.

**Change Practiced**

Added a `Purpose` tag to the existing security group:

`Purpose = "Week3-State-Practice"`

**Commands Practiced**

- `terraform state list`
- `terraform fmt`
- `terraform validate`
- `terraform plan`
- `terraform apply`

**Terraform Plan Result**

Terraform detected:

- 0 resources to add
- 1 resource to change
- 0 resources to destroy

Only the existing security group was updated.

**Terraform Apply Result**

`Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`

This demonstrated that Terraform used the existing state and updated only the required resource instead of creating a new EC2 instance.

**What I Learned**

I learned that Terraform state keeps track of resources managed by Terraform. When the configuration changes, Terraform compares the desired configuration with the existing infrastructure and determines the required changes.

**Status**

**Week 3 – Day 21: Completed**
