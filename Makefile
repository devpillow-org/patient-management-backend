# .PHONY purpose
# to avoid a conflict with a file of the same name, and to improve performance
# with .PHONY, you declare explicit which the target is not a file but a action to be executed.

.PHONY: startapp
startapp:
	docker compose run --rm django python manage.py startapp $(app_name)
	sudo chown -R ${USER}:${USER} $(app_name)/
	rm $(app_name)/models.py
	rm $(app_name)/views.py 
	rm $(app_name)/tests.py 
	rm $(app_name)/apps.py
	mkdir $(app_name)/api  \
		$(app_name)/api/views  \
		$(app_name)/domain \
		$(app_name)/domain/models \
		$(app_name)/infrastructure \
		$(app_name)/tests
	touch $(app_name)/api/__init__.py \
		$(app_name)/api/permissions.py \
		$(app_name)/api/serializers.py \
		$(app_name)/api/urls.py \
		$(app_name)/api/views/__init__.py  \
		$(app_name)/domain/__init__.py \
		$(app_name)/domain/services.py \
		$(app_name)/domain/models/__init__.py  \
		$(app_name)/infrastructure/__init__.py \
		$(app_name)/infrastructure/interfaces.py \
		$(app_name)/infrastructure/repositories.py \
		$(app_name)/infrastructure/utils.py \
		$(app_name)/tests/__init__.py
	cp ./contrib/app_config.py $(app_name)/apps.py
	@sed -i '/^    default_auto_field/a\    name = "$(app_name)"' $(app_name)/apps.py

.PHONY: migrate
migrate:
	docker compose run --rm django python manage.py migrate $(app_name)

.PHONY: migrations
migrations:
	docker compose run --rm django python manage.py makemigrations $(app_name)

.PHONY: show_urls
show_urls:
	docker compose run --rm django python manage.py show_urls
