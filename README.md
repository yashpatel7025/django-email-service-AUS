# django-email-service-AUS

access webapp from -> http://django-email-service-aus.centralindia.cloudapp.azure.com/

## description

- django-email-service-AUS is email service which sends email via any of the service providers Amazon SES, Google SMTP or SendGrid, if one of the services goes down, it can quickly failover to a another provider without affecting customers, service uses yashi-multi-email-service-AUS library which take cares of sending emails via one of the service providers
- so instead of relying on 1 service provider or platform we are providing customers a platform where multiple providers are integrated
- Backend -> 
      - backend of project mainly consist of one POST API which simply calls yashi-multi-email-service-AUS library to send email, and GET API to view all sent emails and its status
      - redis is used: this is used to cache the emails sent for 1 hour, this is added bcoz one user usually comes back to 'view page' to view past emails sent, and keeping in mind that there would be many customers using this platform, to avoid redundent GET API calls to database, the result is stored in cache for 1 hour
      - pagination is added: pagination is added to get only top 10 recent emails sent, its very likely that user want to see only last email sent or last few emails 
- Frontend -> additionall there is capability added to view all sent emails and thier status on web portal from which user can see the status of all email sent and also the past emails sent
- additionally user can send email directly using email-form from web portal as well as email can be send using API client e.g postman, also all sent emails can be fetched from API client

## tools/technology/frameworks used

- Backend -> Python, Django Framework
- Frontend -> HTML, CSS, Bootstrap
- Database -> MySQLite, Redis(for caching)

## leftout implementation due to time constraints

- unit tests
- could not add mailgun and mandrill provider mentioned in project description as one of them was asking payment details on sign up and other do not support free emails like gmail.com and yahoo.com

## things i would have improved or added if had more time

- adding Registration and Login functionality -> Currently, the application do not support multiple users/customers, so all the configuration related to all 3 providers are hardcoded at backend only for 1 particular user, email can be sent from 1 email id only
- in future, differnt user can add thier API keys from all these integrated providers and save to this platform, and we can make this platform as "all in 1" kind of platform, developers could be the potential users for this platform as most of the time developers integrate one of the service to its software and it many times goes down and results in failure of delivering the emails
- adding proper Authentication -> currently web_token and api_token are configured at backend directly to access APIs using web portal and using API respectively, would have used JWT token authentication if we are sending emails by API only and not from frontend
- functionality to attcach documents(pdf,images), adding cc, bcc data in email
- Storing extra information -> storing the failure reason incase of email could not sent by any of the provider, which can be shown to user at frontend

## Link to other code I'm particularly proud of

- learned about DevOps tools -> jenkins, ansible and gunicorn, nginx etc while implementing this
- codebase mostly has ansible implementation to deploy the django app to jenkins server and from there to multiple servers[dev,QA,prod], everything on one click
- https://github.com/yashpatel7025/django_project_CICD_automation-using-github_actions-jenkins-ansible-azure_cloud
- there are many projects/codebase that I'm proud of but most of them are private (as it was dveloped for organizations)

## Link to your resume or public profile.

- Resume
- Public Profile


### Contact for any difficulties accessing the webapp or related to setup

- email:- yashpatel7025@gmail.com
- call: 7021875166, whatsapp:9730039951

## Hosting

- hosted on Microsoft Azure
- can be accessed at-> http://django-email-service-aus.centralindia.cloudapp.azure.com/


### Demo

<img src="./demo-images/1.png" width="1000" height="430">
---
<img src="./demo-images/2.png" width="1000" height="430">
