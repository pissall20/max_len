# max_len

### Install the following libraries

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev 
libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev postgresql libpq-dev
```

### Install python requirements

```markdown
# Boot up your favorite virtual environment
pip install -r requirements.txt
```

### Setup the database:

```
sudo -u postgres psql postgres

# \password postgres

Enter new password: 
# Enter "postgres"

CREATE DATABASE mldbv1;
```
```markdown
# Back to the shell
python manage.py makemigrations; python manage.py migrate
# To run the server
python manage.py runserver 127.0.0.1:8000

```