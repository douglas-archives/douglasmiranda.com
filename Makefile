clean:
	@find . -name "*.pyc" -delete

# deps:
# 	@pip install -qr requirements/test.txt

# test: deps clean
# 	@python manage.py test --settings=douglasmiranda.settings.test

run:
	@python manage.py runserver --settings=douglasmiranda.settings.dev