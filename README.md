# Owl & Hoot

The fourth and final project in Code Institute Full Stack Developer program features an e-commerce fashion retailer called Owl & Hoot. It is designed to provide the full experience that a real online store would such as registering and making a purchase. The product database includes three famous brands with different products and categories. There is a possibility of adding many additional features and they will be added depending on viability and importance as well as the available time.

## UX

### User Stories

- I want to be able to create an account.
- I want the option to delete my profile.
- I want to see the reviews and the posibility to leave one.
- I would like to search for products and filter the brands I desire.
- I want to be able to add a product to basket and view it before going to checkout.
- I wish the products had good images from different angles to get a better look of the product.

### Wireframes

[Homepage](static/images/readme_images/homepage.png)

[Product list](static/images/readme_images/product_list.png)

[Product page](static/images/readme_images/product_page.png)

[Basket](static/images/readme_images/basket.png)


### Colors
### Fonts

## Technologies used

##### Languages, frameworks and more
![HTML5 icon](static/images/readme_images/html-icon.png) HTML5 - webpage markup language for basic structure

![CSS3 icon](static/images/readme_images/css-icon.png) CSS3 - HTML document styling language 

![Bootstrap icon](static/images/readme_images/bootstrap.png) Bootstrap - CSS framework with focus on responsive design

![JavaScript icon](static/images/readme_images/javascript-icon.png) JavaScript - behavior of elements on the website 

![jQuery icon](static/images/readme_images/jquery-icon.png) jQuery - JavaScript library

![Python icon](static/images/readme_images/python.png) Python - backend programming language working together with Flask, MongoDB and Heroku

![Heroku icon](static/images/readme_images/heroku.png) Heroku - cloud deployment platform

##### Repository, coding environment and version control

- [Gitpod](https://www.gitpod.io/) - coding environment
- [Git](https://git-scm.com/) - used for version control
- [Github](https://www.gitpod.io/) - hosting platform for managing repositories and more

#####  Resources

- [Flaticon](https://www.flaticon.com/) - used for icons
- [Pexels](https://www.pexels.com/) - homepage images
- [Google Fonts](https://fonts.google.com/) - source for all fonts on the website
- [JD](https://www.jdsports.ie/) - source of all products including images and descriptions

## Testing

### User stories testing
### Features and tests

### Code validation
##### HTML
##### CSS
#### Javascript
##### Python
### Browser Compatibility


## Database schema
 
![UserProfile model](static/images/readme_images/userprofile-db.png)
The UserProfile model is a subclass of the Django [User model](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#fields) that sets default user information. As the information needs to be associated with a User, in case of deletion, the corresponding UserProfile instance is deleted as well. 

![Order model](static/images/readme_images/order-db.png)
The Order model has a ForeignKey of UserProfile. If a profile is deleted, the field will be set to null as we still need to keep the order in the system. The products in the order are set as a JSONField which shows quantities and sizes for each product. The field is formated in the admin by [django-json-widget](https://github.com/jmrivas86/django-json-widget) for better readability.

![Product model](static/images/readme_images/product-db.png)
The Product model has no relational keys as its needed values are transformed into a dictionary and saved. If a product gets deleted, it is automatically removed from all the carts that it was in via the context. The intention behind the rating fields is to enable users to rate the product, but I am unsure if I will have the time to add that functionality.



## Deployment

### Heroku
1. Create a new app on the Heroku website and choose the region in which most of your users reside.

2. Select the Add-ons window and add Heroku Postgres. To use Heroku Postgress make sure to `pip3 install dj_database_url` and `pip3 install psycopg2.binary` from your project terminal (don't forget to update the requirements file).

3. Go to the Heroku settings tab and copy your database URL from Config Vars section. Make it the default database in your project Django settings with `'default': dj_database_url.parse(your_url)`  
Make migrations and migrate. If you get the `django.db.utils.OperationalError: FATAL:  role "some_role"  does not exist`, you can fix it by using `unset PGHOSTADDR` command.  
Before pushing to GitHub make sure to change the default database to `'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))` as not to expose it.

4. Install gunicorn web server `pip3 install gunicorn`  
Create Procfile and add `web: gunicorn your_project.wsgi:application`

5. Log in to Heroku from the terminal `heroku login`. If error forbidden shows up, use `heroku login -i` instead.  
Temporarily disable Heroku's static file collection with `heroku config:set DISABLE_COLLECTSTATIC=1 --app your_heroku_app_name`
Add hostname of your Heroku app in settings: `ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost']`

6. If app created trough the website initialise git remote: `heroku git:remote -a owl-and-hoot`  
Push your changes to Github and then to Heroku: `git push heroku master` (could be main instead of master depending on your branch). 

### AWS

1. Create and verify an AWS account. After logging in search for S3 scalable storage and create a bucket selecting the apropriate region again. Make sure to unblock all public access and tick the confirmation box at the bottom.

2. After creation is confirmed select the created bucket to customize settings. Go to the bottom of the properties to Static website hosting. Enable it and under Hosting type select host a static website. Fill the index and error document sections with placeholders as it will not be needed.

3. Go to the permissions tab CORS section and paste the following configuration `[{"AllowedHeaders": ["Authorization"], "AllowedMethods": ["GET"], "AllowedOrigins": ["*"], "ExposeHeaders": []}]`

4. In the same tab, select Bucket policy section and then Policy generator. Set policy type as S3 Bucket Policy. Allow all Principals by entering a * in the field and select GetObject action. Go back to the Bucket policy section and copy your Bucket ARN, pasting it into the appropriate policy generator field. Add statement, generate policy and paste the result back in the Bucket policy section while adding a /* after your app name in the resource key.

5. After saving the policy, go to the Access control list section and tick the List box under Everyone (public access) section which will finish the setup.

6. In the search bar, search for Identity and Access Management (IAM). Select user groups from the dropdown, name and create a group. 

7. Select policies from left-side dropdown and create a policy. Select the JSON tab and import managed policy button. Select AmazonS3FullAccess policy and import it. Copy your ARN again from the Bucket policy section and replace the resource key with a list containing your ARN and the ARN followed by /* which will refer to all the files in your bucket. With that done, click review policy, name and create it.

8. Go back to the group created in step 6 and under Permissions tab, select add permissions - Attach Policies, attaching the created policy.

9. Select the users choice from dropdown to add a user to the group. Name the user and tick Access key - Programmatic access box. Clicking next add user to the needed group in the table. Finalize adding user and download csv file before closing.

### Connecting Django, Heroku and AWS

1. In the terminal `pip3 install boto3` and `pip3 install django-storages`. 

2. Add "storages" to your settings, installed apps. Also add the AWS variables which I will not list here, but you can find them my settings file. Remember to change your AWS region if needed. These variables also need to be added to Heroku and can be found in the downloaded csv file. Make sure to keep them secret. Also, remove the DISABLE_COLLECSTATIC variable.

3. Create custom storages file, you can refer to my own and add static files config in settings file.

4.  just confirm your superuser email and add Stripe keys to Heroku. With that done, deployment is complete,

## Commit messages

The commit messages follow conventional commit format: **type(optional scope): description**. Here are the commit message types used in this project:  

- fix: bug fixes
- feat: new features
- docs: adding content to README
- style: adding comments, spaces and other style changes
- refractor: editing code but not functionality e.g. renaming a variable

## Credits