output "florian_ec2_intence_public_ip_address" {
  value = aws_instance.florian_instance.public_ip

}