output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.terraform_vm.id
}

output "public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.terraform_vm.public_ip
}
