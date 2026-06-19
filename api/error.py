from flask import (
    Blueprint, render_template
)

bp = Blueprint('error', __name__, url_prefix='/error')

@bp.route('/')
def simple_error():
    return render_template('/error.html')