# EC 500 Project - User Authorization Module

The User Auth module allows users to register, login, and logout of their session.

## Setup on AWS

- Install the [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) tools to connect to your instance on AWS.
  - You can also use the EB CLI instructions on Amazon's [GitHub Repo](https://github.com/aws/aws-elastic-beanstalk-cli-setup).
- Code to assist in getting module working on AWS after creating the environment. Issues regarding flask-mysqldb and not having the development environment installed on the virtual machine.

```
sudo yum install -y mysql-devel
sudo yum install gcc
```

## Notes

- Main apps are named `application.py` to conform to Amazon Elastic Beanstalk requirements.
- Previoulsy deployed module on AWS. Taken down due to cost constraints.
