.PHONY: clean
clean:
	@find ./ -name "*.pyc" -exec rm -f {} \;

.PHONY: db
db:
	@python ./manage.py migrate

.PHONY: install
install: clean
	@pip install -r requirements.txt
	@python ./manage.py migrate

.PHONY: run
run:
	@python ./manage.py runserver

.PHONY: test
test:
	@python manage.py test --traceback
