Coverage: 95%
# Python Week 9 Project - Meal Planner

For week 9 in the QA Academy programme, we had to design a multi relationship database with at least two tables to perform a CRUD application. I have chosen to choose the tables of customers and meal plans, the customer table will be the primary and the meal plans will contain the foreign key (membership_id). Both tables successfully create, read, update and delete their inputs.

## Getting Started

If you wish to mimic or use a similar layout to what I have for this project, please follow the tools below. These steps and tools will help you deploy your app using python (visual studio code), GCP and Jenkins as a CI pipeline.

### Prerequisites

What things you need to install the software and how to install them -

```
Python 3.10.5 - https://www.python.org/downloads/
Google Cloud Platform (GCP) Account - https://cloud.google.com
gitbash - https://git-scm.com/downloads
Visual Studio Code - https://code.visualstudio.com/Download
Jira - https://www.atlassian.com/software/jira/guides/getting-started/basics
Jenkins - https://www.jenkins.io/doc/pipeline/tour/getting-started/
Workbench - https://www.mysql.com/products/workbench/

```

### Installing

A step by step series of examples that tell you how to get a development env running on a Virtual Machine and coding in Python.
You're more than welcome to fork this repository down or use as a template for your own.


```
1. Download all software above and set up accounts, all with the same email to avoid conflicts.

2. Create an account with Google Cloud Platform and set up a free trial, input your card details and ensure not to exceed the $300 credit limit. Create a firewall on port:5000 and open it to all IP addresses for access anywhere. Opening a port on port:8080 could be useful to do now for Jenkins later.

3. With your port:5000 firewall, set up a VM. I recommend using small on your settings and using Ubuntu, make note of the user name and the IP address, these are needed for setting up a VM in VSC.

4. In VSC, use the user name and IP address in your config file to launch your personal VM and run the ssh-keygen.

5. Connect VM and launch connect to host, this will put your VM online in VSC, make sure all credentials are correct - you can check these on your VM in GCP.

6. The Jenkins file has already been supplied in this repo, follow this link to launch Jenkins on port:8080 of your application IP address. https://qa-community.co.uk/~/_/learning/jenkins-introduction/jenkins--installation-wizard
If you have trouble getting an intial password, reset your PC and try again.

7. When creating a Jenkins account, make note of your username and password - these are linked to your particular VM on port:8080.

8. Creating a Jenkins job ensures you are launching your app online - creating a webhook also continuously updates and connects your VM, Jenkins and repository. Follow this tutorial to set up a Jenkins job https://qa-community.co.uk/~/_/learning/jenkins-introduction/jenkins--freestyle-project

9. Build the application to launch it online.

10. To view the application visit port:5000, to visit Jenkins go on your port:8080.

My application is here - http://35.246.105.40:5000/home

Note: Switch off your VMs everday to avoid extra spending on credit!

```

## Running the tests

I have already provided tests that have 95% coverage in the test_app.py file, but on Jenkins the console output is also 95% after running the below commands in the execute shell - 

```
#!/bin/bash
export ${DATABASE_URI}
export ${SECRET_KEY}
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 -m pytest --cov
python app.py

```

### Unit Tests 

Supplied in the test_app.py file.

```
def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)
```

### Integration Tests 
The Update function for the customer, if customer userName, firstName, lastName or primeMembership status needed to be updated.

```
class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(
            url_for('update', id=1),
            data = dict(firstName="Gaz", lastName = "Watkins", userName = "gazwatkins")
        )
        assert len(Memberships.query.all()) == 1
        assert Memberships.query.filter_by(firstName="Gaz").first().id ==1

```
## Future Imrpovements - Further Sprints

1. The test_delete_get and test_delete_customer aren't yet passing and there wasn't time to debug for this sprint, further work needs to be done to reach 100% coverage in testing.

2. Further HTML work will be done (aesthetics and layout) and therefore I won't be merging to main at this point in time, at least until the next sprint as I want to work further on this project.

3. dtep1-startproject is the equivalent to dev branch, the project will be on this branch for the near future.


## Built With

* [Python](https://www.python.org/) 
* [Jenkins](https://www.jenkins.io/) 

## Versioning

We use [Github](https://github.com) for versioning.

## Authors

**Elina McGlinchey** - [elinamcglinchey](https://github.com/elinamcglinchey)

## License

This project is licensed under the MIT license - see the [LICENSE.md](LICENSE.md) file for details 

*For help in [Choosing a license](https://choosealicense.com/)*

## Acknowledgments

* QA Academy
