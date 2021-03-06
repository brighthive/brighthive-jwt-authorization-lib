"""Access Token Decorator

This decorator can be used to wrap any endpoint that needs to be protected.

"""

from bhjwt.providers import OAuth2Provider


def token_required(
    provider: OAuth2Provider, api_type: str = "graphql", scopes: list = []
):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            # if provider.validate_token(scopes=scopes):
            #     return f(*args, **kwargs)
            # NOTE: 'scopes' is not currently being utilized. Deprecate?
            asserter = provider.validate_token(scopes=scopes)
            if asserter:
                if api_type == "graphql":
                    args[1].context.asserter = asserter
                    return f(*args, **kwargs)

        return wrapped_f

    return wrap
