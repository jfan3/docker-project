## Project Description 
This project builds a logistic regression model that uses three independent variables to predict mortality rate for next year with the simulated Medicaid data 
(details about the data can be found in the `data` folder). It builds two docker images within a AWS EC2 instance, one for a webapp that asks for user input for the three variables,
and one for mounting the machine learning model.

## Model building 
Please refer to model.ipynb

## Deployment on AWS EC2
Note: This employs the default AWS Linux AMI. Make sure to open port 3838 with a security group so you will be able to access that port and see the Shiny application.

* SSH into the EC2 Node (I use t2.large)
```bash
ssh -i keyname.pem ec2-user@instance-DNS
```

* Install docker
```bash
sudo yum update -y
sudo yum install -y docker
sudo yum install -y git
```

* Start docker and give permissions to the ec2-user
```bash
sudo service docker start
sudo usermod -a -G docker ec2-user
```

* Close this SSH window and then run the SSH command again, restarting the user account with the updated permissions.

* Git Clone the Repository with the Dockerfile and the application:
```bash
git clone https://github.com/alexcengler/docker-shiny.git
```

* Run
```bash
docker-compose up
```

* Visit DNS:5000 and input the variables.

