from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.apis.teachers.schema import TeacherSchema
from core.models.teachers import Teacher

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)


@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of all teachers"""
    principal_teachers = Teacher.get_all_teachers()
    principal_teachers_dump = TeacherSchema().dump(principal_teachers, many=True)
    return APIResponse.respond(data=principal_teachers_dump)