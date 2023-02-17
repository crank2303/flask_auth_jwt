from flask import Blueprint
from .roles import create_role, delete_role, change_role, roles_list

blueprint = Blueprint("api/v1", __name__)

blueprint.add_url_rule(
    '/create_role',
    methods=["POST"],
    view_func=create_role,
)
blueprint.add_url_rule(
    '/delete_role',
    methods=["DELETE"],
    view_func=delete_role,
)
blueprint.add_url_rule(
    '/change_role',
    methods=["PUT"],
    view_func=change_role,
)
blueprint.add_url_rule(
    '/roles_list',
    methods=["GET"],
    view_func=roles_list,
)
