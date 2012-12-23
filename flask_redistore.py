import redis

from flask import _request_ctx_stack

try:
    from flask import _app_ctx_stack
except ImportError:
    _app_ctx_stack = None


# Which stack should we use?  _app_ctx_stack is new in 0.9
connection_stack = _app_ctx_stack or _request_ctx_stack


class Redistore(object):

    def __init__(self, app=None, redis_class=redis.Redis):
        self.app = app
        self.redis_class = redis_class

        if not self.app is None:
            self.init_app(self.app)

    def __getattr__(self, name):
        return getattr(self.connection, name)

    def init_app(self, app):
        app.config.setdefault("REDIS_URI", "redis://localhost:6379/")

    def get_app(self, reference_app=None):
        """Helper method that implements the logic to look up an application.
        """
        if reference_app is not None:
            return reference_app
        if self.app is not None:
            return self.app
        ctx = connection_stack.top
        if ctx is not None:
            return ctx.app
        raise RuntimeError('application not registered on Redistore '
                           'instance and no application bound '
                           'to current context')

    def create_redis(self):
        return self.redis_class.from_url(self.get_app().config["REDIS_URI"])

    @property
    def connection(self):
        # Redirect to an instance of self.redis_class for this particular
        #   app
        app = self.get_app()

        if not hasattr(app, "_redis"):
            app._redis = self.create_redis()

        return app._redis
