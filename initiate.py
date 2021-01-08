from sanic import response
from sanic import Blueprint

my_bp = Blueprint('set_direction')

@my_bp.route('/set_direction')

def my_bp_func(request):
    return response.text('set directions')
