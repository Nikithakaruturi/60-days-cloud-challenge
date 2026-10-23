**Week 3 – Day 22: Terraform Cleanup**

**Objective**

Learn how to safely remove infrastructure managed by Terraform and verify that the resources have been removed from Terraform state.

**Resources Cleaned Up**

The resources created during the Day 19 Terraform configuration were cleaned up:

- EC2 instance
- Security group

**Commands Practiced**

- `terraform plan -destroy`
- `terraform destroy`
- `terraform state list`
- `terraform plan`

**Destroy Plan**

Terraform showed:

`Plan: 0 to add, 0 to change, 2 to destroy.`

The plan contained only the EC2 instance and Terraform security group managed by the Day 19 state.

**Destroy Result**

`Destroy complete! Resources: 2 destroyed.`

The EC2 instance and security group were successfully removed.

**State Verification**

After destruction, `terraform state list` returned no resources.

This confirmed that Terraform no longer had any managed resources in the Day 19 state.

**Final Verification**

`terraform plan` showed that the resources would need to be created again if the configuration were applied.

I did not run `terraform apply` after cleanup.

**What I Learned**

I learned how Terraform can safely manage the complete lifecycle of infrastructure, including creating resources, tracking them through state, updating them, and destroying them when they are no longer needed.

**Status**

**Week 3 – Day 22: Completed**
