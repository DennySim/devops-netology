provider "aws" {
  profile = "default"
  region  = "eu-central-1"
}


data "aws_caller_identity" "current" {}
data "aws_region" "current" {}


data "aws_ami" "ubuntu" {
  most_recent = true
  owners = ["aws-marketplace", "amazon"]
  
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu*21.10*"] 
  }
}

resource "aws_instance" "net_test" {
  ami = "${data.aws_ami.ubuntu.id}"
  #ami = "ami-06465d49ba60cf770"
  count = 1
  #ami-0233214e13e500f77
  #i-02d83db7d0451b342 (MyAWSinstance)  172.31.32.143 54.93.247.217 vpc-c0922eaa 
  instance_type = "t2.micro"
  tags = {
    name        = "X-${count.index}"
    TimeCreated = timestamp()
  }
}  