provider "aws" {
  region = "ap-east-1" # or your region
}

# create security group to allow inbound port 8000.
resource "aws_security_group" "uptime_sg" {
  name        = "uptime-logger-sg"
  description = "Allow port 8000 for FastAPI" 
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# launch EC2 with docker installed
resource "aws_instance" "uptime_logger" {
  ami           = "ami-0c55b159cbfafe1f0" # sample AMI
  instance_type = "t3.micro"
  vpc_security_group_ids = [aws_security_group.uptime_sg.id]
  key_name      = "my-keypair" # sample keypair name

  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update -y
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo docker run -d -p 8000:8000 YOUR_DOCKERHUB_USERNAME/uptime-logger:latest
              EOF

  tags = {
    Name = "uptime-logger"
  }
}
