pip3 install flask_sqlalchemy
pip3 install flask_cors
pip3 install flask --upgrade
pip3 uninstall flask-socketio -y
service postgresql start
su - postgres bash -c "psql < ~/Bureau/Cours-ALX-UDACITY/Cours-2-Creation_API-REST/Flask-Cors/plantsdb-setup.sql"
su - postgres bash -c "psql plants < ~/Bureau/Cours-ALX-UDACITY/Cours-2-Creation_API-REST/Flask-Cors/plant.psql"



#su - postgres bash -c "psql < /home/workspace/plantsdb/plantsdb-setup.sql"
#su - postgres bash -c "psql plants < /home/workspace/plantsdb/plant.psql"