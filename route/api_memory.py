from flask import request
from controllers.MemoryCtrl import MemoryCtrl
from flask import Blueprint

api_memory = Blueprint('memory_api', __name__)


@api_memory.route('/get-ram-info')
def getRamInfo():
    n = request.args.get('n')

    # if n is None:
    #     return {
    #         'error':''
    #     }

    num = int(n) if n is not None else 0

    memory_ctrl = MemoryCtrl()
    return memory_ctrl.getRamInfo(num)

