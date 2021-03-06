from bhjwt.assertions.main import AssertJwt
from bhjwt.exceptions import AuthorizationError
import pytest

# Super Admin claims


def test_pass_if_super_admin_claim_is_correct():
    asserter = AssertJwt({'brighthive-super-admin': True})
    asserter.is_super_admin()
    asserter.fail_if_none()


def test_fail_if_super_admin_assertion_not_present():
    asserter = AssertJwt({'brighthive-super-admin': None})
    asserter.is_super_admin()

    with pytest.raises(AuthorizationError):
        asserter.fail_if_none()


def test_fail_if_super_admin_not_true():
    asserter = AssertJwt({})
    asserter.is_super_admin()

    with pytest.raises(AuthorizationError):
        asserter.fail_if_none()

