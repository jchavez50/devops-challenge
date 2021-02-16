# Devops-challenge

### Overview
In this DevOps Challenge, I've created a pipeline with Deploying a Flask app on AWS with Gitlab CI/CD. 

# Tools: AWS (EC2, S3, ElasticBeanstalk, Gitlab), Flask, Python, Jinja, Docker, 

### Application 
(Not Complete) The application will allow a user to input numerical values and input numerical measure to target a unit of measure in comparisons of a users response. This data will be authoritative and return on whether the users response is correct, incorrect, or invalid.  

### Prerequites
* AWS account
* GitLab project/repo for the CI/CD
* Virtualenv to isolate the Python version and packages needed
* Git installed 

### Steps to setup the AWS Elastic Beanstalk (EB) 
1. Install EB CLI on your local machne (For more information on EB CLI)(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)
```
pip install awsebcli --upgrade --user
```
2. Setting your AWS credentials on your local machine (For more information on IAM service) (https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
To run EB CLI, you have to provide credentials. (Not recommended to use your root account)
For best practice use a specific IAM user/service account to manage EB CLI/Configs "ebadmin".
Now you can configure your AWS credentials using the following commands, 
```
aws configure
```
...which will ask for both your, 
```
aws-access-id
aws-secret-key
```

3. Initialize  EB CLI(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)
Install EB CLI
```
pip install awsebcli --upgrade --user
```
Initialize the EB config files 
```
eb init -p python-3.7 app-name --region us-west-2
```
This will generate an .elasticbeanstalk directory with the config file which is important for the CI/CD pipeline. Be sure to remove these lines below in your .gitignore file before proceeding. 
```
# Elastic Beanstalk Files
.elasticbeanstalk/*
!.elasticbeanstalk/*.cfg.yml
!.elasticbeanstalk/*.global.yml
```
4. Create a Gitlab project/repo to host your code
Go to Gitlab (https://gitlab.com/) to create a new project and run git init. 
Now you can push your code: 
```
git add .
git commit -m "init commit"
git remote add origin https://gitlab.com/<your-username>/<repo-name>
git push -u origin master
```
5. Create the EB environment and deploy your code
Run these three commands: 
 When creating the EB environment, you will be asked for the environment name, DNS CNAME, and Load Balancer type, just hit enter to keep the default. 

```
eb create <name-of-environment>
```
This will deploy your code that was git init to your GitLap repo in a previous step. 
```
eb deploy
```
Open your running environment by executing this command
```
eb open
```
To avoid any ongoing fees run this command to terminate your running environment
```
eb terminate
```
6. Create Gitlab CI/CD pipeline 
Gitlab  has CI/CD feature which creates an empty .gitlab-ci.yml file at the root of your project. Inside this project
is where we can add the code (manifest) to this file with similar contents below. 
```
image: python:3.7-stretch

stages: 
    - test
    - deploy
 ....dependancies below
```
What's going on under-the-hood, is Gitlab runner pulls a Docker image to install the dependancies. 

Two step pipeline: 
* First step for unit tests
* Create a new python packages tests\ at the root of the project and a file test_app.py. 
```
import unitttest

class testClassUnit.TestCase): 
 ...
```
* Commit/push your code and in your Gitlab project, you should see a job running automatically and eventually pass the test. 

* Secondly the deployment - We can now deploy with a few additons to the yaml file

```
deploy_code: 
    stage: deploy
    before_script: 
    ...dependancies
```
Note: You need to add your ```aws_access_id``` and ```aws_secret_access_key``` to Gitlabs variables which can be used in your CI/CD pipeline. Go to Settings > CI/CD" menu. You should fill the "Variables" section with these two variables. 

### Current Issues
* NGINX server not publishing throwing to error 502 (HTTP PROXY) 
* Flask app with Python temp conversion modules not resolving, additional lint testing required
* Jinja system throwing exception errors 400 Bad request (proxy) or server connection

### Possible improvements
* For simplicity, this is a POC app and should not be used in production. It requires additional resources or layers added
* when using NGINX/uWSGI backend servers, and security parameters. But for this case the pipeline does work! 
* An alternative pipeline could be developed from source > github > cloud-build > container registry > cloud run. 