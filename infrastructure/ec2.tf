resource "aws_instance" "app_server" {
  iam_instance_profile = "LabInstanceProfile"
  vpc_security_group_ids = [aws_security_group.server_security_group.id]
  ami = "ami-0cea098ed2ac54925"
  instance_type = "t2.micro"
  key_name = "vockey"
  subnet_id = aws_subnet.publicsubnet1.id
  associate_public_ip_address = "true"
  tags = {
  Name = "music2live_server"
  }
}

resource "aws_security_group" "server_security_group" {
  name        = "port22andport80"
  description = "allow port 22 and port 80"
  vpc_id      = aws_vpc.server_vpc.id
  ingress {
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "openport22andport80"
  }
}