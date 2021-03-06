# django-email-service-AUS

## Description

- ```django-email-service-AUS``` is email service which sends email via any of the service providers **Amazon SES**, **Google SMTP** or **SendGrid** using library called [multi-email-service-yashpatel-AUS](https://test.pypi.org/project/multi-email-service-yashpatel-AUS/), user can select the default service provider to send email, if it fails it will failover to other provider
- so instead of relying on 1 service provider or platform we are providing customers a platform where multiple providers are integrated
- **Backend** 
    * Backend of project mainly consist of 1 POST API which simply calls [multi-email-service-yashpatel-AUS](https://test.pypi.org/project/multi-email-service-yashpatel-AUS/) library to send email, and 1 GET API to view all sent emails and its status
    * **Redis** is used: this is used to cache sent emails, this is added bcoz one user usually comes back to 'view page' to view sent emails in past, keeping in mind that there would be many customers using this platform, to avoid redundent GET API calls to database the result is stored in cache for 1 hour
    * **Pagination** is added: pagination is added to get only top 10 recent emails sent, its very likely that user want to see only last email sent or last few emails
      
- **Frontend** 

    * Additionally there is capability added to view all sent emails and thier status on web portal from which user can see the status of all email sent and also the past sent emails
    * irrespective of email id passed in ```from_email``` field, email will be sent from ```yashwadia7025@gmail.com``` currently
  
- Also user can send email directly using email-form from web portal as well as email can be send using API client e.g Postman,all sent emails can also be fetched by calling API from API client

## Tools/ Technology / Frameworks used

- **Backend** -> Python, Django Framework
- **Frontend** -> HTML, CSS, Bootstrap
- **Database** -> SQLite, Redis(for caching)

## Technical Choices

- **Django Framework** -> for quick devlopment withing deadline, Django's **motto** says it all **???the framework for developers with deadlines???**
- **SQLite** -> as application has only one table which store emails sent, also SQLite is suitable for small applications like this
- **HTML, CSS, Bootstrap** -> haven't really done much frontend dev, these are only frameworks i have used in past other than JS
- **Redis** -> best out there, very fast, more data types supported when compared to many key-value data stores

## Leftout implementation due to time constraints

- Unit Tests
- Could not add **Mailgun** and **Mandrill** provider mentioned in project description as one of them was asking payment details on sign up and other do not support free emails like @gmail.com and @yahoo.com

## Things I would have improved or added if had more time

- **adding Registration and Login functionality** -> Currently, the application do not support multiple users/customers, so all the configuration related to all 3 providers are configured at backend only for 1 particular user, email can be sent from 1 email id only
- In future, differnt user can add thier API keys from all these integrated providers and save to this platform, and we can make this platform as "all in 1" kind of platform, developers could be the potential users for this platform as most of the time developers integrate one of the service to its software,many times  it goes down and results in failure of delivering the emails
- **adding proper Authentication** -> Currently web_token and api_token are configured at backend directly to access APIs using web portal and using API client respectively, would have used JWT token authentication if we are sending emails by API only and not from frontend
- **Storing extra information** -> Storing the failure reason incase of email could not sent by any of the provider, which can be shown to user at frontend

## Link to other code I'm particularly proud of

- Learned about **DevOps tools** -> **Jenkins**, **Ansible** and **Gunicorn**, **Nginx** etc while implementing this
- Codebase mostly has ansible implementation to deploy the django app to jenkins server and from there to multiple servers[dev,QA,prod], everything on one click
- https://github.com/yashpatel7025/django_project_CICD_automation-using-github_actions-jenkins-ansible-azure_cloud
- There are many projects/codebase that I'm proud of but most of them are private (as it was dveloped for organizations)

## Link to my Resume and Public Profile.

- [Resume](./extra/Resume_Yash_Patel_SDE.pdf)
- [Public Profile](https://github.com/yashpatel7025)

## Hosting

- Hosted on **Microsoft Azure**
- Can be accessed at-> http://django-email-service-aus.centralindia.cloudapp.azure.com/

## link to multi-email-service-yashpatel-AUS

- https://github.com/yashpatel7025/yashi-multi-email-service-AUS

### Contact for any difficulties accessing the webapp

- **Email**:- yashpatel7025@gmail.com
- **call**: 7021875166, **whatsapp**:9730039951

## API Contract

Send Email

```
curl --location --request POST 'http://django-email-service-aus.centralindia.cloudapp.azure.com/send_email/' \
--header 'Cookie: messages=.eJyLjlaKj88qzs-Lz00tLk5MT1XSMdAxMtVRcs1NzMxRKE7NK1EoLk1OBkqmlebkVCrF6gxKHbEAW75FtQ:1lvQ02:Vfu3RU9Qh3_JlHB8cTpZqM6y70Ptk99-N6OkK4bCsuU; messages=.eJyLjlaKj88qzs-Lz00tLk5MT1XSMdAxMtVRcs1NzMxRKE7NK1EoLk1OBkqmlebkVCrF6gwTHbEApChW_w:1lvaXo:zA74UTujO7PemphsR72GN83kQOLjp_WdF9IRu0Edl30' \
--form 'to_email=yashpatel7025@gmail.com' \
--form 'from_email=yashwadia7025@gmail.com' \
--form 'subject=Job application' \
--form 'body_text=Hi, How are u? Regards,Yash' \
--form 'sent_via=3' \
--form 'status=1' \
--form 'TOKEN=ef16fd3e-d271-11eb-b8bc-0242ac130003'
```
get sent emails

```
curl --location --request GET 'http://django-email-service-aus.centralindia.cloudapp.azure.com/view_sent_emails/?TOKEN=ef16fd3e-d271-11eb-b8bc-0242ac130003'
```
