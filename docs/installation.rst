Installation Guide
======================================

To install AdminXperience, follow these steps:

1. Install AdminXperience using pip:

   .. code-block:: bash

      pip install adminxperience

2. Add 'adminxperience' to the ``INSTALLED_APPS`` list in your Django project's ``settings.py`` file:

   .. code-block:: python

      INSTALLED_APPS = [
          ...
          'adminxperience',
          ...
      ]

3. Run migrations to apply any necessary changes to your database models:

   .. code-block:: bash

      python manage.py makemigrations
      python manage.py migrate

Once installed and configured, you can start using AdminXperience in your Django project.

For more detailed information on configuration and usage, please refer to the documentation.
