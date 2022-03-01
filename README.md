# bmb-drt
RestApi source code


<h2>RestApi</h2>
<p>
<ol>
    <li>PostgreSQL/PostGIS Install</li>
    <li>create database</li>
    <li>dbname: api_bmb_db</li>
    <br>
    <li>Then open setting.py config db</li>
    <li>'ENGINE': 'django.db.backends.postgresql',</li>
    <li>'NAME': 'api_bmb_db',</li>  
    <li>'USER': 'postgres',</li>  
    <li>'PASSWORD': '@dmin',</li>  
    <li> 'HOST': '127.0.0.1',</li>  
    <li> 'PORT': '5432'</li>
    
<br>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
<li>Python manage.py runserver</li><br>
<li>http://127.0.0.1:8000/admin/</li>
<li>username: admin</li>
<li>password: superadmin</li>
</ol> 
</p>