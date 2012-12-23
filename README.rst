Flask Redistore
===============

.. image:: https://travis-ci.org/dstufft/Flask-Redistore.png
    :target: https://travis-ci.org/dstufft/Flask-Redistore

Adds Redis to your Flask Appliation.

Install
-------

.. code:: bash

    $ pip install Flask-Redistore

Usage
-----

.. code:: python

    import flask
    from flask.ext.redistore import Redistore

    app = flask.Flask(__name__)
    app.config["REDIS_URI"] = "redis://:password@localhost/0"

    redis = Redistore(app)
    redis.set("My key", "the value!")
    redis.get("My key")

Usage (advanced)
----------------

.. code:: python

    import flask
    import redis

    from flask.ext.redistore import Redistore

    redis = Redistore(redis_class=redis.StrictRedis)

    def create_app(name=__name__):
        app = flask.Flask(name)
        app.config["REDIS_URI"] = "redis://:password@localhost/0"

        redis.init_app(app)

        return app

    create_app()

    redis.set("My new key", "Another Value!")
    redis.get("My new key")
